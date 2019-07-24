#!/usr/bin/env python3
import re
import json
import subprocess

from PyInquirer import prompt


def main():
    # Load package lists from file
    packages = load_config('packages.json')

    # Generate questions based on loaded packages
    questions = generate_questions(packages)

    # Get install options from user
    options = inquire(questions)

    # Install packages
    for option in options:
        install(option, packages[option])


def load_config(filename: str) -> dict:
    with open(filename) as f:
        packages = json.load(f)

    return packages


def generate_questions(packages: dict) -> list:
    choices = []

    for category, packages in packages.items():
        package_list = ', '.join(packages[:5])
        choices.append({
            'name': f'{category.title()} ({package_list}...)',
            'checked': False,
        })

    questions = [
        {
            'type': 'checkbox',
            'name': 'packages',
            'qmark': '📦 ',
            'message': 'Which packages would you like to install?',
            'choices': choices,
        }
    ]

    return questions


def inquire(questions: list) -> list:
    print('\n')

    options = []
    answers = prompt(questions)

    for answer in answers['packages']:
        fword = answer.split(' ')[0].lower()
        options.append(fword)

    return options


def install(category: str, packages: list):
    print(f'\n[+] Installing {category} packages...')
    for package in packages:
        result = subprocess.Popen(
                f'sudo apt install {package} -y', 
                shell=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT
            )

        for line in result.stdout.readlines():
            if re.search(package, str(line)):
                print(line.decode().strip())

main()
