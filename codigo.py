import requests
import os
import zipfile

def baixar_pdf(link, diretorio_output):
    if not os.path.exists(diretorio_output):
        os.makedirs(diretorio_output)
    nome_pdf = os.path.join(diretorio_output, link.split('/')[-1])
    resposta_pdf = requests.get(link)
    with open(nome_pdf, 'wb') as arquivo:
        arquivo.write(resposta_pdf.content)
    print(f"PDF baixado: {nome_pdf}")
    return nome_pdf

def compactar_pdfs_em_zip(pdfs_baixados, nome_arquivo_zip):
    with zipfile.ZipFile(nome_arquivo_zip, 'w') as zipf:
        for pdf in pdfs_baixados:
            zipf.write(pdf, os.path.basename(pdf))
    print(f"Arquivo ZIP com os PDFs criado: {nome_arquivo_zip}")

if __name__ == '__main__':
    link_pdf_1 = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN624_RN625.2024.pdf'
    link_pdf_2 = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN624_RN625.2024.pdf'
    diretorio_output = 'PDFs_extraidos'
    print("Baixando os PDFs...")
    pdfs_baixados = []
    pdfs_baixados.append(baixar_pdf(link_pdf_1, diretorio_output))
    pdfs_baixados.append(baixar_pdf(link_pdf_2, diretorio_output))
    print("Compactando os PDFs...")
    compactar_pdfs_em_zip(pdfs_baixados, 'PDFs_baixados.zip')
    print("Processo concluído com sucesso!")
