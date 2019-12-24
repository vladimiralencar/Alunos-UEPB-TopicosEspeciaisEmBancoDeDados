
Cada vez mais os robôs estão presentes em nosso dia a dia. Mas para que os robôs possam entender e navegar adequadamente por um local, eles precisam de informações sobre seu ambiente.

Nesta competição, você ajudará robôs (especificamente veículos autônomos terrestres) a reconhecer a superfície do piso em que estão, usando os dados coletados por sensores IMU (Inertial Measurement Units).

Os dados usados nesta competição foram coletados pelo Departamento de Processamento de Sinais da Tampere University na Finlândia. A coleta dos dados foi feita com um pequeno robô móvel equipado com sensores IMU sobre diferentes superfícies do piso nas instalações da universidade. A tarefa é prever em qual dos nove tipos de piso (carpete, ladrilhos, concreto, etc…) o robô está usando dados do sensor, como aceleração e velocidade. Tenha sucesso nesta competição e você ajudará a melhorar a navegação dos robôs autônomos em muitas superfícies diferentes.

=====

Descrição dos Datasets

Dados de Entrada (X):
X_ treino.csv e X_teste.csv - os dados de entrada, cobrindo 10 canais de sensores e 128 medições por série temporal, mais três colunas de identificação:

-row_id: o ID para a linha.

-series_id: número de identificação da série de medições. Chave estrangeira para y_train / sample_submission.

-measurement_number: número de medição dentro da série.

Os canais de orientação codificam os ângulos atuais de como o robô é orientado como um quaternion (rotações espaciais em 3 dimensões, X, Y e Z). A velocidade angular descreve o ângulo e a velocidade do movimento e os componentes de aceleração linear descrevem como a velocidade está mudando em momentos diferentes. Os 10 canais do sensor são:

orientation_X

orientation_Y

orientation_Z

orientation_W

angular_velocity_X

angular_velocity_Y

angular_velocity_Z

linear_acceleration_X

linear_acceleration_Y

linear_acceleration_Z

Dados de Saída (y):
y_treino.csv - as superfícies para o conjunto de treinamento.

-series_id: número de identificação da série de medições.

-group_id: número de identificação para todas as medidas realizadas em uma sessão de gravação. Fornecido apenas para o conjunto de treinamento, para permitir mais estratégias de validação cruzada.

-superfície: o objetivo desta competição (variável target).

Arquivo de submissão:
sample_submission.csv - um arquivo de envio de amostra no formato correto.

----

Datasets e Solução (Rodrigo Lima): https://www.kaggle.com/rodrigolima82/dsa-competicao-set-2019
