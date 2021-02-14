# Load optional zsh options
autoload -Uz compinit promptinit up-line-or-beginning-search down-line-or-beginning-search

# add local binaries to path
export PATH=~/bin:$PATH

# use emacs keybindings 
bindkey -e

# enable ctrl-x-e to edit current command in $EDITOR
autoload -U edit-command-line
zle -N edit-command-line
bindkey '^xe' edit-command-line
bindkey '^x^e' edit-command-line

# enable command autocompletion
compinit

# autocompletion: highlight and cycle through matches
zstyle ":completion:*" menu select

# prompt to correct mis-spellings
setopt CORRECT_ALL

# configure history settings
HISTFILE=~/.zsh/history
HISTSIZE=100000
SAVEHIST=100000
HISTDUP=erase
setopt sharehistory
setopt appendhistory
setopt incappendhistory

# configure git-prompt widget
source /usr/share/git/completion/git-prompt.sh
GIT_PS1_SHOWDIRTYSTATE="true"
GIT_PS1_SHOWUNTRACKEDFILES="true"
GIT_PS1_SHOWCOLORHINTS="true"
GIT_PS1_SHOWUPSTREAM="auto"

# minimal prompt (fmt: "<cwd> (git-info) : ")
precmd () { __git_ps1 "%B%F{blue}%c%f " ":%b " "(%s) " }

# enable full-color support
TERM=xterm-256color

# set default editor
export EDITOR=vim

# load personal settings from ~/.config/zsh/
source ~/.config/zsh/aliases.sh
