# Cria e ativa o ambiente virtual
python3 -m venv venv
source ./venv/bin/activate

# Instala as dependências
python3 -m pip install -r requirements.txt

# Instancia o banco de dados
cd ./ai
python3 manage.py migrate