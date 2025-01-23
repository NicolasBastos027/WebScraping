import requests  # Biblioteca para realizar requisições HTTP
import os        # Biblioteca para interagir com o sistema operacional
import zipfile   # Biblioteca para manipular arquivos ZIP

# Função para baixar um arquivo PDF de um link e salvá-lo em um diretório específico
def baixar_pdf(link, diretorio_output):
    # Verifica se o diretório de saída existe; caso contrário, cria o diretório
    if not os.path.exists(diretorio_output):
        os.makedirs(diretorio_output)

    # Extrai o nome do arquivo PDF do link e define o caminho completo para salvá-lo
    nome_pdf = os.path.join(diretorio_output, link.split('/')[-1])

    # Realiza o download do arquivo PDF do link
    resposta_pdf = requests.get(link)

    # Salva o conteúdo do PDF no caminho especificado
    with open(nome_pdf, 'wb') as arquivo:
        arquivo.write(resposta_pdf.content)

    # Exibe uma mensagem indicando que o PDF foi baixado com sucesso
    print(f"PDF baixado: {nome_pdf}")

    # Retorna o caminho do PDF baixado
    return nome_pdf

# Função para compactar uma lista de PDFs em um único arquivo ZIP
def compactar_pdfs_em_zip(pdfs_baixados, nome_arquivo_zip):
    # Abre (ou cria) o arquivo ZIP em modo de escrita
    with zipfile.ZipFile(nome_arquivo_zip, 'w') as zipf:
        # Itera sobre os arquivos PDF baixados
        for pdf in pdfs_baixados:
            # Adiciona cada PDF ao arquivo ZIP, usando apenas o nome do arquivo no ZIP
            zipf.write(pdf, os.path.basename(pdf))

    # Exibe uma mensagem indicando que o arquivo ZIP foi criado com sucesso
    print(f"Arquivo ZIP com os PDFs criado: {nome_arquivo_zip}")

# Bloco principal do código: executa o programa quando o arquivo é executado diretamente
if __name__ == '__main__':
    # URLs dos PDFs que serão baixados
    link_pdf_1 = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN624_RN625.2024.pdf'
    link_pdf_2 = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN624_RN625.2024.pdf'

    # Nome do diretório onde os PDFs serão salvos
    diretorio_output = 'PDFs_extraidos'

    # Exibe uma mensagem indicando o início do processo de download
    print("Baixando os PDFs...")

    # Lista para armazenar os caminhos dos PDFs baixados
    pdfs_baixados = []

    # Baixa o primeiro PDF e adiciona o caminho à lista
    pdfs_baixados.append(baixar_pdf(link_pdf_1, diretorio_output))

    # Baixa o segundo PDF e adiciona o caminho à lista
    pdfs_baixados.append(baixar_pdf(link_pdf_2, diretorio_output))

    # Exibe uma mensagem indicando o início do processo de compactação
    print("Compactando os PDFs...")

    # Compacta os PDFs baixados em um arquivo ZIP
    compactar_pdfs_em_zip(pdfs_baixados, 'PDFs_baixados.zip')

    # Exibe uma mensagem indicando que o processo foi concluído com sucesso
    print("Processo concluído com sucesso!")
