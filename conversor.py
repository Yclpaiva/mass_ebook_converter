import os
import subprocess

def convert_to_mobi(option,delete_option):
    current_directory = os.getcwd()
    files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]

    processed_files = []

    extension = ""
    if option == 1:
        extension = ".mobi"
    elif option == 2:
        extension = ".epub"
    elif option == 3:
        extension = ".azw3"
    elif option == 4:
        extension = ".pdf"

    for file in files:
        output_file = os.path.splitext(file)[0] + extension

        print("Fazendo a conversão do arquivo: ", file)
        try:
            subprocess.run(
                ["ebook-convert", file, output_file],
                check=True,
                # Redireciona a saída padrão e de erro para o nulo, evita o spam no console
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            print(f"Arquivo convertido com sucesso: {file} -> {output_file}")
            processed_files.append(file)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao converter o arquivo {file}: {e}")
    if delete_option:
        for file in processed_files:
            os.remove(file)
            print(f"Arquivo original excluído: {file}")

    #processo finalizado
    print("\033c")
    print("-"*10)
    for i in range(len(processed_files)):
        print(f"{i+1} - {processed_files[i]}")

if __name__ == "__main__":
    print("Iniciando o programa de conversão dos arquivos de PDF")
    print("-"*10)
    print("Para qual formato deseja converter TODOS os arquivos dessa pasta?")
    print("1 - MOBI")
    print("2 - EPUB")
    print("3 - AZW3")
    print("4 - PDF")
    print("-"*10)
    option = int(input("Digite o número correspondente ao formato: "))
    print("-"*10)
    print("Após a conversão, deseja excluir os arquivos originais?")
    print("1 - Sim")
    print("2 - Não")
    print("-"*10)
    delete_option = bool(input("Digite o número correspondente à opção: "))
    convert_to_mobi(option, delete_option)

