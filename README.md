# Web Scraping
Este projeto tem como objetivo realizar o download de arquivos PDF a partir de links fornecidos, salvá-los em um diretório específico e compactá-los em um único arquivo ZIP para facilitar o armazenamento e compartilhamento.

# Bibliotecas Utilizadas
O projeto utiliza as seguintes bibliotecas:

- `requests`: Utilizada para realizar requisições HTTP e fazer o download dos arquivos PDF diretamente dos links fornecidos.
- `os`: Utilizada para manipulação de diretórios e arquivos no sistema operacional, como criação de pastas e organização.
- `zipfile`: Utilizada para criar e manipular arquivos ZIP, permitindo compactar os PDFs baixados.
Como todas essas bibliotecas são nativas do Python, não é necessário instalar pacotes adicionais.

Certifique-se de ter as bibliotecas instaladas antes de executar o projeto. Caso precise instalá-las, você pode utilizar o gerenciador de pacotes `pip` para instalar as dependências. Veja os exemplo abaixo:

```bash
pip install requests
```
Certifique-se de ter uma conexão com a internet durante a instalação para que o pip possa baixar e instalar as bibliotecas necessárias.

Certifique-se de estar no diretório do script Python e execute o seguinte comando no terminal:
bash
Copy
Edit
python script.py  
Resultado:

## Como Utilizar

1. Clone o repositório para sua máquina local utilizando o seguinte comando:
```bash
git clone https://github.com/NicolasBastos027/WebScraping.git
```

2. Navegue para o diretório do projeto:
3. Defina a URL da página web que deseja acessar na variável `url`.
4. Execute o script Python e aguarde a conclusão.
```bash
python codigo.py
```
5. Os arquivos que correspondem ao padrão desejado serão baixados e salvos na pasta atual.
6. Após o download, os arquivos serão compactados em um arquivo zip com o destino especificados.
7. Verifique o arquivo zip gerado para acessar os arquivos baixados.

Tenha em mente que você pode personalizar o padrão utilizado para filtrar os links desejados ajustando a expressão regular na variável `padrao` no arquivo.

---

Este projeto é um exemplo básico de web scraping e manipulação de arquivos usando Python. Sinta-se à vontade para adaptar e expandir o código de acordo com suas necessidades.
