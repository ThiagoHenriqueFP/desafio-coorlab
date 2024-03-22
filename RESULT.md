# Resultado - Desáfio CoorLab

## Backend

A solução desenvolvida no backend foi utilizando [fastapi](https://fastapi.tiangolo.com/), um projeto que como o nome já remete, é focado em desenvolver API's de forma rápida, desta forma sendo uma boa escolha devido a simpicidade dos user stories descritos no README.md. O banco de dados é lido pela lib "pandas" que permite manipular o arquivo json e retornar via http. As funções descritas dentro do parser servem para manipular o json.

Um dos detalhes importantes que seguem a implementação do backend é que o cors está habilitdo para qualquer origem, visto que é um projeto que nãol irá para produção.

## Frontend

Desenvolvido em vue.js, como dito nas instruções, não foi utilizado nenhuma lib externa, com exceção da lib "axios" para realizar requisições http para a api. O objetivo foi deixar a aplicação o mais modularizada e consistente possível, respeitando o design fornecido e boas práticas.
