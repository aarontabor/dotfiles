# Load optional zsh options
autoload -Uz compinit promptinit up-line-or-beginning-search down-line-or-beginning-search

# add local binaries to path
export PATH=~/bin:$PATH

# use emacs keybindings 
bindkey -e

# disabe <ctrl-s> "screen-locking" functionality
stty -ixon

# use delete key as intended
bindkey "^[[3~" delete-char

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
## save 10,000 history items, shared across all terminal sessions
HISTFILE=~/.zsh/history
HISTSIZE=10000
SAVEHIST=10000
setopt sharehistory
setopt appendhistory

## Do not add duplicates to the history list (i.e., the shell's local memory)
## All whitespace differences are ignored
setopt histignorealldups
setopt histreduceblanks

## Do not save duplicates in the history file (i.e., the global file shared across all sessions)
setopt histsavenodups

# configure git-prompt widget
source ~/.git-prompt.sh
GIT_PS1_SHOWDIRTYSTATE="true"
GIT_PS1_SHOWUNTRACKEDFILES="true"
GIT_PS1_SHOWCOLORHINTS="true"
GIT_PS1_SHOWUPSTREAM="auto"

# minimal prompt (fmt: "<cwd> (git-info) : ")
precmd () { __git_ps1 "%B%F{blue}%c%f " ":%b " "(%s) " }

# enable full-color support
TERM=xterm-256color

# set default editor
export EDITOR=nvim
export VISUAL=nvim

# load personal settings from ~/.config/zsh/
source ~/.config/zsh/aliases.sh
