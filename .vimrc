set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'morhetz/gruvbox'
Plugin 'lilydjwg/colorizer'

call vundle#end()
filetype plugin indent on

autocmd vimenter * NERDTree
set relativenumber
set numberwidth=2

set tabstop=2     " show existing tab with 2 spaces width
set shiftwidth=2  " when indenting with '>', use 2 spaces width
set expandtab     " on pressing tab, insert 2 spaces

set colorcolumn=80
highlight ColorColumn ctermbg=white

" set color scheme
let g:airline_theme = 'gruvbox'
colorscheme gruvbox
set background=dark
syntax enable

" transparent background
hi Normal ctermbg=none
hi NonText ctermbg=none
