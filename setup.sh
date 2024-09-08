#!/usr/bin/env zsh

python3 -m pip install -r requirements.txt

autoload -Uz compinit
compinit

typer --install-completion
source /root/.zfunc/_typer
zsh
