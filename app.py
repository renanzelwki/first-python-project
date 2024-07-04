# Importando as bibliotecas para dentro do projeto.
import PyPDF2
import os

# Criando o masclador de PDF.
merger = PyPDF2.PdfMerger()

# Lista os arquivos dentro do diretorio "arquivos", e usa o .sort para ordenar.
lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

# Função para percorrer todos os arquivos dentro do diretorio, .append adiciona o arquivo que esta lendo no mesclador.
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")

# Salvando o pdf final.
merger.write("PDF Final.pdf")