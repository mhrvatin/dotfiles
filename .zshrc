# Path to your oh-my-zsh installation.
export ZSH=/home/macke/.oh-my-zsh

# Look in ~/.oh-my-zsh/themes/
ZSH_THEME="wedisagree_custom-macke_flower"
#ZSH_THEME="random"

# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
HIST_STAMPS="yyyy-mm-dd"

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Add wisely, as too many plugins slow down shell startup.
plugins=(colorize last-working-dir colored-man-pages extract safe-paste)

export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"

source $ZSH/oh-my-zsh.sh

export LANG=sv_SE.UTF-8

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
alias 'chrome=google-chrome'
alias 'gping=ping google.com'
alias 'gdping=ping 8.8.8.8'

alias 'hysus=systemctl hybrid-sleep'
alias 'hibernate=systemctl hibernate'
alias 'reboot=systemctl reboot'
alias 'shutdown=systemctl poweroff'

alias 'digm=ssh macke@vps.hrvatin.se -X'
alias 'digr=ssh root@vps.hrvatin.se -X'
alias 'pi=ssh pi@192.168.0.113 -X'

alias 'copy=xclip -sel clip'
alias 'netup=/home/macke/scripts/network_up.sh'

alias 'install=sudo apt-get install'
alias 'update=sudo apt-get update'
alias 'upgrade=sudo apt-get upgrade'
alias 'purge=sudo apt-get purge'
alias 'autorm=sudo apt-get autoremove'
alias 'autoclean=sudo apt-get autoclean'
