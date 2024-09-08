FROM python:3.12

RUN apt-get update && apt-get install -y zsh
COPY . /typer-autocomplete-bug
WORKDIR /typer-autocomplete-bug

ENTRYPOINT ["./setup.sh"]
