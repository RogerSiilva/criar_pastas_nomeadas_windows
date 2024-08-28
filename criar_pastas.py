import os
import shutil

diretorio = input('Digite o diretório: ')  # Substitua pelo caminho do diretório onde estão os arquivos

for filename in os.listdir(diretorio):
    arquivo_path = os.path.join(diretorio, filename)
    if os.path.isfile(arquivo_path):
        nome_sem_extensao = os.path.splitext(filename)[0]
        nova_pasta = os.path.join(diretorio, nome_sem_extensao)

        if not os.path.exists(nova_pasta):
            os.makedirs(nova_pasta)

        novo_caminho_arquivo = os.path.join(nova_pasta, filename)
        shutil.move(arquivo_path, novo_caminho_arquivo)
print()
print('Pastas criadas com Sucesso!')