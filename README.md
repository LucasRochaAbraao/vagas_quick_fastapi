# Vagas Quick
> Esse repositório contém o projeto que gerencia a API que o site da Quick consulta para divulgar vagas na página /trabalhe-conosco.
> São 2 projetos arquivados juntos, pois para criar a API eu uso o FASTAPI, que expõe as vagas. E também há um discord bot para nosso RH gerenciar as vagas do banco de dados.

[![python-image]][python-url]
[![discord-image]][discord-url]
[![fastapi-image]][fastapi-url]
[![heroku-image]][heroku-url]
[![mongodb-image]][mongodb-url]

Nesse repositório vocẽ encontra informações de instalação, além de ter acesso ao código fonte, que inclui uma licença open source pra copiar (desde que use a mesma licença no seu projeto)


## Índice

* [Comandos](#comandos)
* [Setup & Instalação](#setup--instalação)

## Comandos  

|    Comando   |    Sintaxe    |   Descrição   |
|     :---     |     :---:     |     :---:     |
| criar_vaga | !criar_vaga | Inicia o processo de criação de vaga. |
| excluir_vaga | !excluir_vaga | Inicia o processo de exclusão de vaga. |
| vagas | !vagas | Mostrar todas as vagas no banco de dados. |
| desativar_vaga | !desativar_vaga <id da vaga> | Desativa uma vaga, mas deixa guardada no banco de dados. |
| ativar_vaga | !sativar_vaga <id da vaga> | ativa uma vaga, para ser exposta pela API e ser divulgada no site. |

## Setup & Instalação
Primeiro é necessário instalar, configurar e ativar um ambiente virtual, para um melhor gerenciamento do projeto.

```
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```
Depois mais alguns passos para ligar o bot e fazer um deployment automático...

>Clone o repo
```
pip install -r requirements.txt
```


>Crie uma conta no discord e siga a documentação oficial para:
```
Criar um bot
Criar um servidor
Vincular seu bot ao servidor
https://discord.com/developers/docs/intro
```


>crie um arquivo ".env" no diretório do projeto, contendo 2 variáveis:
```
DISCORD_TOKEN=219038129031290asdasduiashuidahsuidsad
DB_URL=mongodb+srv://clustername:<password>-cluster-cl.server.mongodb.net/test
```


>Crie uma conta grátis no https://cloud.mongodb.com
```
Siga a documentação oficial para:
Criar um cluster
Criar uma database
Criar uma collection
No dashboard do mongodb é possível obter o url para conectar, que vai no arquivo ".env" na variável "DB_URL"
https://docs.mongodb.com/
```


>Crie uma conta grátis no heroku
```
Crie uma nova aplicação no heroku
Vincule sua conta no heroku com a do github, no menu "deploy"
Acompanhe nos logs do heroku seu próximo commit
Para sua aplicação executar automaticamente, habilite o "worker" no menu "Resources"
```

[python-image]: https://img.shields.io/static/v1?label=python&message=3.7&color=blue
[python-url]: https://www.python.org/downloads/release/python-370/

[discord-image]: https://img.shields.io/static/v1?label=discord.py&message=rewrite+&color=lightgrey
[discord-url]: https://discord.com/developers/docs/intro

[fastapi-image]: https://img.shields.io/static/v1?label=fastapi&message=0.63+&color=blue
[fastapi-url]: https://fastapi.tiangolo.com/

[heroku-image]: https://img.shields.io/static/v1?label=heroku&message=app&color=red
[heroku-url]: https://www.heroku.com/

[mongodb-image]: https://img.shields.io/static/v1?label=mongodb&message=atlas&color=success
[mongodb-url]: https://docs.mongodb.com/

Distribuído sob a licença `GNU GENERAL PUBLIC LICENSE`. Veja `LICENSE` para mais informações.
