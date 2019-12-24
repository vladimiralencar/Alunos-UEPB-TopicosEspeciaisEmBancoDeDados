
Antes de definir o problema a ser resolvido nesta Competição, vamos compreender um pouco do mercado de seguros! Ao final você encontra a descrição do que deve ser feito.

O Mercado de Seguros

Estar preparado para imprevistos é uma das vantagens de quem tem planejamento financeiro. Para aumentar ainda mais a sua segurança contra situações inesperadas, uma boa solução são os seguros.

Existem diferentes tipos que você pode contratar. Alguns protegem seus bens como carro, moto ou casa. Outros protegem você e sua família - são os seguros de saúde, vida e acidentes pessoais.

Prêmio

O valor que você paga pelo seguro é baseado na avaliação do risco. Riscos baixos têm prêmios baixos e riscos altos, prêmios altos.

As seguradoras coletam informações sobre os interessados em contratar o seguro e analisam estatisticamente o risco envolvido em cada caso, para chegar ao valor do prêmio.

A lei exige que tanto o segurado quanto a seguradora usem o princípio da boa-fé. Isso significa que o segurado deve fornecer declarações verdadeiras à seguradora, para que esta trace um perfil de risco correto antes de definir o valor da indenização e do prêmio.

Franquia

A franquia é uma participação conjunta do segurado e da seguradora no risco e no valor da indenização. Quanto maior o valor da franquia, menor o valor do prêmio e vice-versa. Nem todos os seguros possuem franquia. Quando ela existe, pode ser:

Dedutível: a seguradora indeniza somente o valor do prejuízo que ultrapassar a franquia. Por exemplo, em um seguro com indenização de R$ 10 mil e franquia de R$ 2 mil, em caso de sinistro o segurado pagará R$ 2 mil, referentes à franquia, e a seguradora, R$ 8 mil.

Simples: a seguradora não é obrigada a pagar os valores abaixo da franquia, mas, se o dano ultrapassar esse total, a seguradora paga o valor integral do prejuízo. Por exemplo, em um seguro com indenização de R$ 10 mil e franquia de R$ 2 mil, em caso de sinistro, se o valor do prejuízo for até R$ 2 mil, quem paga é o segurado. Se o valor for acima de R$ 2 mil, a seguradora paga o valor total do prejuízo, e o segurado não desembolsa nada.

Problema a ser Resolvido

Indenização

Conforme você leu acima, os pedidos de indenização devem ser bem cuidadosamente avaliados pela seguradora, o que pode levar tempo. Por isso, você foi contratado para construir um modelo preditivo capaz de prever a probabilidade de um determinado pedido ser atendido imediatamente ou não.

Com base em dados históricos e anônimos, seu objetivo é fazer a previsão de probabilidade se cada novo pedido de indenização poder ser atendido de forma imediata ou não.

Os dados históricos estão classificados com duas classes, 0 e 1.

A classe 0 indica que o pedido de indenização não foi atendido imediatamente (provavelmente porque requeria uma análise mais detalhada). A classe 1 indica que o pedido de indenização foi atendido imediatamente.

Seu trabalho não é prever se um novo pedido deve ou não ser atendido imediatamente, mas sim prever a probabilidade de cada pedido. Isso permite que a seguradora priorize pedidos acima de 80% de probabilidade de serem atendidos imediatamente, por exemplo.

Este é um problema de classificação binária, mas ao invés de prever as classes, você deverá prever as probabilidades.

Há um complicador adicional. As variáveis não estão identificadas, pois são dados anônimos. Mas isso não é relevante para a solução do problema.

Dataset e Solução: https://www.kaggle.com/valencar/kernel-vladimiralencar-lana-v05
