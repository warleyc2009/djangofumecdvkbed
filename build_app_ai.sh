#!/bin/bash

# Habilita modo para interromper o script em caso de erro
set -e

echo "==============================="
echo "Iniciando o build do projeto..."
echo "==============================="

# 1. Cria e ativa o ambiente virtual
echo "Criando o ambiente virtual..."
python3 -m venv venv
echo "Ativando o ambiente virtual..."
source ./venv/bin/activate

# 2. Instala as dependências
echo "Instalando dependências..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# 3. Instancia o banco de dados
echo "Instanciando o banco de dados..."
cd ./ai

# Faz as migrações do Django
echo "Executando makemigrations..."
python3 manage.py makemigrations erp

echo "Aplicando migrações..."
python3 manage.py migrate

# Mensagem final de sucesso
echo "==============================="
echo "Build do projeto finalizado com sucesso! ✅"
echo "==============================="
