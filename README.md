
-------------GUIA PARA USAR O DJANGO-------------
-------------------------------------------------

- Criar ambiente virtual python

 >python -m venv venv

- Ativando o ambiente 

>. .\venv\Scripts\activate

*Lembrando que todas as linhas a baixo devem ser executadas no ambiente virtual, acessado com o comando a cima.*

- Instalando o django

>pip install django

- Conferindo as dependencias 

>pip freeze

- Criando projeto django

>django-admin startproject project .

- Rodar o servidor

>python .\manage.py runserver

*Por padrão o servidor inicia na porta 8000 e pode ser acessado pelo caminho http://localhost:8000/*

- Comando para criar App

>python .\manage.py startapp home

criar ou atualizar o requirements

>pip freeze > requirements.txt

## caso o vscode não completar o html do Django-html colocar no settings.json o techo a baixo ##
 "emmet.includeLanguages": {
        "django-html": "html",
    }