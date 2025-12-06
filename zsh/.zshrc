eval "$(oh-my-posh init zsh --config ~/.poshthemes/custom.omp.json)"

# ---------- aliasse ----------------

alias v="nvim"

alias cv="nvim ~/.config/nvim/init.lua"
alias ck="nvim ~/.config/kitty/kitty.conf"
alias cz="nvim ~/.zshrc"
alias cpo="nvim ~/.poshthemes/custom.omp.json"

alias reti="~/Documents/uni/betriebssysteme/RETI-Emulator/bin/reti_emulator_main"
alias retid="~/Documents/uni/betriebssysteme/RETI-Emulator/bin/reti_emulator_main -d"

alias py="python3 -q"
alias pyd="python3 -m doctest"

alias pdf='tdf -f true'

alias reload="exec zsh"
alias resume="fg"

alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias ....="cd ../../../.."

alias diffi_venv="source ~/Documents/uni/diffi/.venv/bin/activate"

alias linux="docker start -ai my-linux"

alias automate="echo \"Connecting to Automate, \nCMD+A D to exit, export TERM=xterm and screen -r to show\" && fsh pi@10.4.151.39"

# awrit
export PATH="/Users/jakobhaverkamp/.local/bin:$PATH"
alias preview="awrit http://127.0.0.1:8000"
previewp() {
  awrit "http://127.0.0.1:$1"
}
md() {
  awrit "http://localhost:8080/page/$1"
}

# ----------- zoxide -------------------
#zoxide
eval "$(zoxide init zsh --cmd cd)"


# Initialize completion system FIRST
autoload -Uz compinit
compinit

# Carapace configuration
export CARAPACE_BRIDGES='zsh,fish,bash,inshellisense'
source <(carapace _carapace)

zstyle ':completion:*:git:*' group-order 'main commands' 'alias commands' 'external commands'


# Autosuggestions configuration
source /opt/homebrew/share/zsh-autosuggestions/zsh-autosuggestions.zsh

# Syntax highlighting MUST be last
source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# ----------- zinit ----------------

if [[ ! -f $HOME/.local/share/zinit/zinit.git/zinit.zsh ]]; then
    print -P "%F{33} %F{220}Installing %F{33}ZDHARMA-CONTINUUM%F{220} Initiative Plugin Manager (%F{33}zdharma-continuum/zinit%F{220})…%f"
    command mkdir -p "$HOME/.local/share/zinit" && command chmod g-rwX "$HOME/.local/share/zinit"
    command git clone https://github.com/zdharma-continuum/zinit "$HOME/.local/share/zinit/zinit.git" && \
        print -P "%F{33} %F{34}Installation successful.%f%b" || \
        print -P "%F{160} The clone has failed.%f%b"
fi

source "$HOME/.local/share/zinit/zinit.git/zinit.zsh"
autoload -Uz _zinit
(( ${+_comps} )) && _comps[zinit]=_zinit

# Load a few important annexes, without Turbo
# (this is currently required for annexes)
zinit light-mode for \
    zdharma-continuum/zinit-annex-as-monitor \
    zdharma-continuum/zinit-annex-bin-gem-node \
    zdharma-continuum/zinit-annex-patch-dl \
    zdharma-continuum/zinit-annex-rust

zinit light https://github.com/matthiasha/zsh-uv-env.git

# ---------------------------------
