# Path to your oh-my-zsh installation.
  export ZSH=/home/macke/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
#ZSH_THEME="af-magic_custom-macke"
#ZSH_THEME="nicoulaj_custom-macke"
ZSH_THEME="wedisagree_custom-macke_mallard"
#ZSH_THEME="random"

# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
HIST_STAMPS="yyyy-mm-dd"

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git colorize ubuntu)

# User configuration

  export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
# export MANPATH="/usr/local/man:$MANPATH"

source $ZSH/oh-my-zsh.sh

# You may need to manually set your language environment
export LANG=sv_SE.UTF-8

# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='vim'
fi

alias 'home=cd ~/'
alias 'skola=cd ~/documents/skola/'
alias 'web=cd /var/www/html'

alias 'vimz=vim ~/.zshrc'
alias 'srcz=source ~/.zshrc'
alias 'nt=urxvt &'

alias 'hysus=systemctl hybrid-sleep'
alias 'hibernate=systemctl hibernate'
alias 'reboot=systemctl reboot'

alias 'binero=ssh 139580_mhrvatin@ssh.binero.se'
alias 'digm=ssh macke@vps.hrvatin.se'
alias 'digr=ssh root@vps.hrvatin.se'

alias 'copy=xclip -sel clip'

alias 'install=sudo apt-get install'
alias 'update=sudo apt-get update'
alias 'upgrade=sudo apt-get upgrade'
alias 'purge=sudo apt-get purge'
alias 'autorm=sudo apt-get autoremove'
