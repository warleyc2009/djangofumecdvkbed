# 1 - Ativa o virtual env
echo "Ativando o ambiente virtual..."
source ./venv/bin/activate

# 2 - Cria os dados
python3 ./ai/clean_database.py