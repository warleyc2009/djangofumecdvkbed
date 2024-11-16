import os

# Caminho raiz do projeto
root_dir = '/caminho/para/seu/projeto'

# Arquivo de saída
output_file = 'projeto_completo.txt'

# Função para ler e escrever arquivos
with open(output_file, 'w') as outfile:
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(('.py', '.html', '.css', '.js')):
                filepath = os.path.join(foldername, filename)
                outfile.write("###########################################################################################\n")
                outfile.write(f"File: {filepath}\n\n")
                with open(filepath, 'r') as infile:
                    code_lines = infile.readlines()
                    for line in code_lines:
                        outfile.write(f"    {line}")
                outfile.write("\n###########################################################################################\n\n")

print(f"Arquivo gerado com sucesso: {output_file}")