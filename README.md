# Web Scraping
Este projeto tem como objetivo realizar o download de arquivos PDF a partir de links fornecidos, salvá-los em um diretório específico e compactá-los em um único arquivo ZIP para facilitar o armazenamento e compartilhamento.

#Bibliotecas Utilizadas
O projeto utiliza as seguintes bibliotecas:

requests: Utilizada para realizar requisições HTTP e fazer o download dos arquivos PDF diretamente dos links fornecidos.
os: Utilizada para manipulação de diretórios e arquivos no sistema operacional, como criação de pastas e organização.
zipfile: Utilizada para criar e manipular arquivos ZIP, permitindo compactar os PDFs baixados.
Como todas essas bibliotecas são nativas do Python, não é necessário instalar pacotes adicionais.

Funções Implementadas
O projeto conta com as seguintes funções:

baixar_pdf(link, diretorio_output):

Realiza o download de um arquivo PDF a partir de um link fornecido.
Verifica se o diretório especificado para salvar os arquivos existe e o cria caso não exista.
Salva o arquivo PDF no diretório de destino.
compactar_pdfs_em_zip(pdfs_baixados, nome_arquivo_zip):

Compacta uma lista de arquivos PDF em um único arquivo ZIP.
Adiciona os PDFs ao arquivo ZIP utilizando apenas o nome do arquivo no interior do ZIP.
Como Utilizar
Links dos PDFs:

Insira os links dos arquivos PDF que deseja baixar diretamente no código, na seção principal do script.
No exemplo, os links estão definidos nas variáveis link_pdf_1 e link_pdf_2.
Execução do Código:

Certifique-se de estar no diretório do script Python e execute o seguinte comando no terminal:
bash
Copy
Edit
python script.py  
Resultado:

Os arquivos PDF serão baixados e salvos no diretório PDFs_extraidos.
Após o download, os arquivos serão compactados em um arquivo ZIP chamado PDFs_baixados.zip, no mesmo diretório.
Estrutura do Projeto
O bloco principal do script (if __name__ == '__main__':) define os links dos PDFs, chama as funções de download e compactação, e exibe mensagens indicando o progresso e conclusão do processo.
A lista pdfs_baixados armazena os caminhos dos arquivos PDF baixados, permitindo que sejam compactados em seguida.
Exemplos de Links
Os links utilizados neste exemplo correspondem a arquivos disponibilizados pela ANS:

Anexo I
Anexo II
Personalização
Você pode personalizar o projeto de várias formas:

Alterar os links dos PDFs para outros documentos de sua escolha.
Modificar o diretório de saída (diretorio_output) ou o nome do arquivo ZIP gerado.
