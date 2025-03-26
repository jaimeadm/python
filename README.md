# Python

Programação Python

Instalar Python Ubuntu 22
```sh
sudo apt update -y
sudo apt upgrade -y
sudo apt install git curl build-essential -y
sudo apt install gcc make default-libmysqlclient-dev libssl-dev -y
sudo apt install python3.10-full python3.10-dev -y
```

Instalar pacotes
```sh
sudo apt install git curl build-essential dkms perl wget -y
sudo apt install gcc make default-libmysqlclient-dev libssl-dev -y
sudo apt install -y zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm \
  libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
```

Ambiente virtual do python
```sh
mkdir projeto && cd projeto
python -m venv venv
source venv/bin/activate
.\venv\Scripts\activate.ps1 # windows
which python
pip --version
pip list
pip freeze
pip index versions pymysql
pip install pymysql
pip install pymysql --upgrade
pip uninstall pymysql -y
pip install --force-reinstall pymysql==1.2.3
python -m pip install pip --upgrade
deactivate venv
deactivate
cd .. && rm -rf projeto
```

Gerar arquivo de dependências
```sh
pip freeze > requirements.txt
python -m venv venv
pip install -r requirements.txt
pip freeze
```

# Pyenv

O Pyenv é um gerenciador de ambientes Python, uma ferramenta que te permite escolher entre diversas versões do Python.
```sh
curl https://pyenv.run | bash
```

Configurar
```sh
vim ~/.bashrc

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

exec $SHELL
```

Atualizar as versões do Python e instalar versão específica
```sh
pyenv update
pyenv install -list
pyenv install 3.11.0
pyenv versions
pyenv global 3.11.0
exec $SHELL
which python
python -V
```