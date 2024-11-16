# 1 - Ativa o virtual env
echo "Ativando o ambiente virtual..."
source ./venv/bin/activate

# 2 - Cria os dados
echo "Criando os dados de exemplo..."
python3 ./ai/create_initial_data.py