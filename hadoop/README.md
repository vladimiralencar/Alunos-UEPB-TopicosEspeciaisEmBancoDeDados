# Usando o hadoop

start-dfs.sh
start-yarn.sh

# Para acessar o Ambari:
Ativar o Browser
http://dataserver:8080

# Para Moitorar o Hadoop:
Ativar o Browser
http://localhost:8088

# Aplicacao Filmes:

hdfs dfs -put u.data /mapred # colocando um arquivo no hdfs

Executar um dataset no hadoop
python AvaliaFilme.py  hdfs:///mapred/u.data -r hadoop

# redireciona a saida para um arquivo
python AvaliaFilme.py  hdfs:///mapred/u.data -r hadoop > /home/aluno/analytics/filmes.txt

Aplicacao amigosFacebook:

hdfs dfs -put amigos_facebook.csv /mapred # coloca o arquivo no hdfs
python AmigosIdade.py hdfs:///mapred/amigos_facebook.csv -r hadoop > /home/aluno/output/amigos_idade.txt

# Aplicacao Livros:

hdfs dfs -put OrgulhoePreconceito.txt /mapred/  # coloca o arquivo no hdfs
python MR-DataMining-1.py hdfs:///mapred/OrgulhoePreconceito.txt -r hadoop > /home/aluno/output/livro1.txt

# Aplicacao Cloudera - logs de servidores
hdfs dfs -mkdir /mapred
hdfs dfs -put web_server.log /mapred

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input /mapred/web_server.log -output /saida

hdfs dfs -cat /saida/part-00000

hdfs dfs -get /saida/part-00000 # pegar o arquivo do hdfs para o sistema linux

# VM HortonWorks (Máquina Virtual)
Ambari: Login: maria_dev, Password: maria_dev
No terminal ( fn + option + f5): Login: root, Password: hadoop

Criar tabela Hive:
Menu -> Hive View
create table estudantes
(ID INT,
nome VARCHAR(50),
sobrenome VARCHAR(50),
sexo Char(1),
email VARCHAR(100));

INSERT INTO estudantes
VALUES
(1000,'Barack','Obama','M','barack@gmail.com');

select * from estudantes;

- Query -> Visualization
- Query -> Data Explorer

# Cloudera Hadoop (Máquina Virtual)

http://quickstart.cloudera:7180
Username: cloudera
Password: cloudera

Abrir o Terminal
hbase shell
version
status

# HBASE
 create 'dsacademy', {NAME=>'ALUNO'},{NAME=>'INSTRUTOR'}
 alter 'dsacademy', {NAME=>'CURSOS'}
list
describe 'dsacademy'
exists 'dsacademy'
disable 'dsacademy'
drop 'dsacademy'
