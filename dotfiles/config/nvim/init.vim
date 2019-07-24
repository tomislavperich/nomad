set nocompatible            " Diable compatibility to old-time vi
set showmatch               " Show matching brackets.
set ignorecase              " Do case insensitive matching
set mouse=v                 " middle-click paste with mouse
set hlsearch                " highlight search results
set tabstop=4               " number of columns occupied by a tab character
set softtabstop=4           " see multiple spaces as tabstops so <BS> does the right thing
set expandtab               " converts tabs to white space
set shiftwidth=4            " width for autoindents
set autoindent              " indent a new line the same amount as the line just typed
set relativenumber          " add line numbers
set wildmode=longest,list   " get bash-like tab completions
set cc=120                  " set a 120 column border for good coding style
set guifont=Ubuntu_Nerd_Mono

" Enable/disable spelling
" nnoremap <leader>s :set invspell<CR>

" Vim-plug
call plug#begin()

Plug 'vim-syntastic/syntastic'
Plug 'airblade/vim-gitgutter'
Plug 'scrooloose/nerdtree'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'ryanoasis/vim-devicons'

" Color schemes
Plug 'dylanaraps/wal.vim'
Plug 'joshdick/onedark.vim'
Plug 'arcticicestudio/nord-vim'
Plug 'ayu-theme/ayu-vim'

call plug#end()

" Color scheme
let ayucolor='dark'
colorscheme onedark

" Sytastic config
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:syntastic_python_pylint_exe = 'python3 -m pylint3'

" Keybindings
map <C-n> :NERDTreeToggle<CR>

