# pip install python-dotenv

import os

# export SENHA=senha123
senha = os.getenv('SENHA')

print(senha)