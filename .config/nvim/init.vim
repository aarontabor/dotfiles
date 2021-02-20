" Automatically reload files from disk (e.g., after git operations)
" Do not use swap files, as they are honestly more of a pain than help
set autoread
set noswapfile

" Represent existing <tab> characters as 2-spaces. Insert tabs as 2 space-characters
set tabstop=2
set shiftwidth=2
set expandtab

" When wrapping text, only break on word boundaries and preserve line's indentation
set linebreak
set breakindent

" Use comma as the main leader key
let mapleader = ","

" Fuzzy-finder file navigation utility
" Map to leader-t because I'm used to Command-T
nmap <leader>t :FZF<cr>
" TODO => make a leader-T key which autopopulates with the current cursor word (e.g., easily jump to components)


" Note that this mapping intentionally lacks a carrige return (this allows me to enter a search query)
nmap <leader>g :vimgrep 

" Use arrow keys to navigate the quickfix menu
nmap <left> :colder<cr>
nmap <right> :cnewer<cr>
nmap <up> :cprevious<cr>
nmap <down> :cnext<cr>

