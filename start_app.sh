# 1 - Ativa o virtual env
echo "Ativando o ambiente virtual..."
source ./venv/bin/activate

# 2 - inicia o servidor
cd ./ai
python3 manage.py runserver