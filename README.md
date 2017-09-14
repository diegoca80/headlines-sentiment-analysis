# Análise de sentimentos de manchetes brasileiras

- Disciplina Computação Afetiva 
- Prof. Dra. Paula Dornhofer Paro Costa 
- FEEC Unicamp

# Autores

- Diego Cardoso Alves
- Murilo Marin Pechoto

# Dependências

O dataset utilizado está disponível neste repositório (retirado de https://github.com/pdpcosta/manchetesBrasildatabase), assim como todos arquivos necessários para execução do projeto.

Entretando, para executá-lo em sua máquina local, você precisará instalar o Python 3 assim como suas bibliotecas, seguindo os passos abaixo:

1. Instalação do Python 3, de prefência sua versão mais atual, disponível em: https://www.python.org/downloads/

2. Caso sua versão de Python não venha automaticamente com o módulo pip instalado, faça a instalação seguindo os passos descritos em: https://pip.pypa.io/en/stable/installing/

3. Após o pip configurado, execute o comando no diretório raiz do repositório:

- pip install -r requirements.txt

4. Como o projeto utiliza vários recursos da biblioteca NLTK, algumas destas devem ser instaladas através de um terminal python, utilizando-se o comando:

- nltk.download()

5. Escolha os recursos descritos abaixo relacionados ao passo 4 e faça a instalação:

- Corpora: MAC Morpho, stopwords

# Etapas de desenvolvimento do projeto

As etapas de desenvolvimento, assim como todo o contexto do projeto, pode ser encontradas no próprio arquivo Jupyer Notebook contido neste repositório.

# Como executar o projeto

1. Executar o Jupyter Notebook pelo terminal usando:

- jupyter notebook

2. Acessar o endereço padrão do Jupyter, caso não seja automaticamente aberto:

- http://localhost:8888/tree