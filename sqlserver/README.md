# Python

Instalar o pacote pyodbc

```sh
pip install pyodbc
```

O Python via pyodbc usa o driver "ODBC Driver 17 for SQL Server"

```sh
# Adiciona o repositório da Microsoft
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
sudo apt-add-repository "$(curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list)"
sudo apt-get update

# Instala o driver
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Também pode ser necessário:
sudo apt-get install -y unixodbc-dev
```