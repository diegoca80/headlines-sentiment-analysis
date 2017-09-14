# An�lise de sentimentos de manchetes brasileiras

- Disciplina Computa��o Afetiva 
- Prof. Dra. Paula Dornhofer Paro Costa 
- FEEC Unicamp

# Autores

- Diego Cardoso Alves
- Murilo Marin Pechoto

# Depend�ncias

O dataset utilizado est� dispon�vel neste reposit�rio (retirado de https://github.com/pdpcosta/manchetesBrasildatabase), assim como todos arquivos necess�rios para execu��o do projeto.

Entretando, para execut�-lo em sua m�quina local, voc� precisar� instalar o Python 3 assim como suas bibliotecas, seguindo os passos abaixo:

1. Instala��o do Python 3, de pref�ncia sua vers�o mais atual, dispon�vel em: https://www.python.org/downloads/

2. Caso sua vers�o de Python n�o venha automaticamente com o m�dulo pip instalado, fa�a a instala��o seguindo os passos descritos em: https://pip.pypa.io/en/stable/installing/

3. Ap�s o pip configurado, execute o comando no diret�rio raiz do reposit�rio:

- pip install -r requirements.txt

4. Como o projeto utiliza v�rios recursos da biblioteca NLTK, algumas destas devem ser instaladas atrav�s de um terminal python, utilizando-se o comando:

- nltk.download()

5. Escolha os recursos descritos abaixo relacionados ao passo 4 e fa�a a instala��o:

- Corpora: MAC Morpho, stopwords

# Etapas de desenvolvimento do projeto

As etapas de desenvolvimento, assim como todo o contexto do projeto, pode ser encontradas no pr�prio arquivo Jupyer Notebook contido neste reposit�rio.

# Como executar o projeto

1. Executar o Jupyter Notebook pelo terminal usando:

- jupyter notebook

2. Acessar o endere�o padr�o do Jupyter, caso n�o seja automaticamente aberto:

- http://localhost:8888/tree