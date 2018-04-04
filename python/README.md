
# Python para Análise de Dados

![Screenshot](https://github.com/vladimiralencar/Alunos-UEPB-TopicosEspeciaisEmBancoDeDados/blob/master/python/Pipeline-Dados-Python.png)

# Coprocessor

De uma forma macro e resumida, podemos definir o coprocessor como um framework que provém um caminho fácil para executar seu código customizado dentro do HBase. As analogias mais comumentes utilizadas para representar o coprocessor são "Trigger / Store Procedure" e AOP. 

O coprocessor pode ser desenvolvido como:
- Observer Coprocessor: é como uma "trigger" de banco de dados, ou seja, é acionado antes ou após um determinado evento. 
- Endpoint Coprocessor: é como uma "store procedure" de um banco de dados, sendo que esse tipo de coprocessor deve ser acionado explicitamente através do método 'CoprocessorService ()' da 'HTableInterface' (ou HTable).

