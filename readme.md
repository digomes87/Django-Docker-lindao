Projeto Criado com a intenção de trabalhar com Docker.

Ao contrario da configuração padrão utilizada em projetos Django.
A 'venv' que se demostra muito útil, porém alguns erros de configuração
persistem, com o tempo esses erros passaram a ser frequentes em diversos projetos.

Ao menos sempre que trabalhava com bancos diferentes.
Utilizar docker passou a ser mais interessante, e os erros diminuiram
drasticamente.

Inclusive nesse projeto fiquei maravilhado com a possibilidade de usar o 
pgAdmin sem configurar nada! EU disse nada !!!

Tá claro que tem umas linhas no docker-compose que configuram isso.
mas sem nada de instalação, nada de fazer dawnload de servidor para banco.

Simplismente avisa o docker que deve subir o banco na porta x e tudo certo.



*** Extremamente importante,
Se for optar por usar o postgres, tens que lembrar que o postgres é um pouco chato com a questão de compartilhamento de volumes,
por isso antes de dar o comando docker-compose-up tu deves criar o volume compartilhado do docker.

Se for seguir esse exemplo de projeto o comando é:
Docker volume create iniciando-django-pgadmin
