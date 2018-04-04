# Usando o hadoop
Iniciando o hadoop e o gerenciador de recursos YARN: <br />
start-dfs.sh <br />
start-yarn.sh <br />

# Para acessar o Ambari:
Ativar o Browser <br />
http://dataserver:8080

# Para Moitorar o Hadoop:
Ativar o Browser <br />
http://localhost:8088 <br />

# Aplicacao Filmes: <br />

hdfs dfs -put u.data /mapred # colocando um arquivo no hdfs <br />

Executar um dataset no hadoop <br />
python AvaliaFilme.py  hdfs:///mapred/u.data -r hadoop

# redireciona a saida para um arquivo <br />
python AvaliaFilme.py  hdfs:///mapred/u.data -r hadoop > /home/aluno/analytics/filmes.txt

Aplicacao amigosFacebook: <br />

hdfs dfs -put amigos_facebook.csv /mapred # coloca o arquivo no hdfs <br />
python AmigosIdade.py hdfs:///mapred/amigos_facebook.csv -r hadoop > /home/aluno/output/amigos_idade.txt <br />

# Aplicacao Livros:

hdfs dfs -put OrgulhoePreconceito.txt /mapred/  # coloca o arquivo no hdfs <br />
python MR-DataMining-1.py hdfs:///mapred/OrgulhoePreconceito.txt -r hadoop > /home/aluno/output/livro1.txt <br />

# Aplicacao Cloudera - logs de servidores
hdfs dfs -mkdir /mapred <br />
hdfs dfs -put web_server.log /mapred <br />

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input /mapred/web_server.log -output /saida <br />

hdfs dfs -cat /saida/part-00000 <br />

hdfs dfs -get /saida/part-00000 => pegar o arquivo do hdfs para o sistema linux <br />

# VM HortonWorks (Máquina Virtual)
Ambari: Login: maria_dev, Password: maria_dev <br />
No terminal ( fn + option + f5): Login: root, Password: hadoop <br />

Criar tabela Hive: <br />
Menu -> Hive View <br />
create table estudantes <br />
(ID INT, <br />
nome VARCHAR(50), <br />
sobrenome VARCHAR(50), <br />
sexo Char(1), <br />
email VARCHAR(100)); <br />

INSERT INTO estudantes <br />
VALUES <br />
(1000,'Barack','Obama','M','barack@gmail.com'); <br />

select * from estudantes; <br />

- Query -> Visualization <br />
- Query -> Data Explorer <br />

# Cloudera Hadoop (Máquina Virtual)

http://quickstart.cloudera:7180 <br />
Username: cloudera <br />
Password: cloudera <br />

Abrir o Terminal <br />
hbase shell <br />
version <br />
status <br />

# HBASE
 create 'dsacademy', {NAME=>'ALUNO'},{NAME=>'INSTRUTOR'} <br />
 alter 'dsacademy', {NAME=>'CURSOS'} <br />
list <br />
describe 'dsacademy' <br />
exists 'dsacademy' <br />
disable 'dsacademy' <br />
drop 'dsacademy' <br />
