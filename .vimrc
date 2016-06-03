set relativenumber
set numberwidth=2

filetype plugin indent on
" show existing tab with 4 spaces width
set tabstop=4
" when indenting with '>', use 4 spaces width
set shiftwidth=4
" on pressing tab, insert 4 spaces
set expandtab

" change background for 80 col and  120+
let &colorcolumn=join(range(81,999),",")
let &colorcolumn="80,".join(range(120,999),",")
highlight ColorColumn ctermbg=200 guibg=#2ccd27

" highlight OverLength ctermbg=126 ctermfg=white guibg=#EF9A9A
" match OverLength /\%81v.\+/

" set color scheme
colorscheme molokai
syntax enable
let g:molokai_original = 1
