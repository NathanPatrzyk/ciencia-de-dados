# Tarefas de Mineração

## Classificação e estimativa de probabilidade de classe

É uma forma de mineração que busca encontrar pequenos grupos em um grupo maior, tentando prever, para cada um dos indivíduos, a que classes eles fazer parte.

As classes são mutuamente exclusivas, ou seja, descobrindo "quais fazem parte?", sabemos automaticamente "quais NÃO fazem parte?".

Conforme novos indivíduos são "adicionados" o sistema vai classificando-os, e gerando uma probabilidade desse fazer parte de uma determinada classe.

Isso faz com que a classificação de relacione com a pontuação, enquanto no primeiro produz uma previsão de classe, o segundo representa uma probabilidade que o indíviduo pertença a essa classe.

Um exemplo seria: Quais clientes compram produtos de informática?

## Regressão

Também conhecido como Estimativa de valor, essa forma de minerar dados vai buscar prever para um determinado indivíduo o valor de uma variável.

Da mesma forma, a partir da análise de outros indivíduos será calculado o QUANTO para um novo indivíduo.

Ao contrário da classificação, que buscar prever se algo vai acontecer, a regressão busca preve o quanto daquilo irá ocorrer.

Um exemplo seria: Quanto um cliente comprará em produtos de informática?

## Combinação por similaridade

Esse tarefa irá identificar quais indivíduos são semelhantes, é uma forma de encontrar entidades que possuam algum grau de semelhança.

Vão funcionar como uma base para outras tarefas como Classificação, Regressão ou Agrupamento.

Um exemplo seria: Quais usuários que compraram produtos semelhantes , logo podemos recomendar outros produtos a esses usuários.

## Agrupamento

É uma forma de minerar dados que reune indivíduos de acordo com sua similaridade, agrupando elementos em diferentes grupos ou segmentos.

Após esses grupos serem formados podem ser aplicados outras abordagens de mineração. Também podendo ser utilizado em processo de tomada de decisão.

Um exemplo seria: Nossos produtos formam categorias ou segmentos?

## Agrupamento de coocorrência

Também conhecido como Mineração de conjunto de itens frequentes, Descoberta da regra de associação ou Análise de portfólio de ações.

Irá tentar encontrar associações se baseando nas transações envolvidas. Se diferencia do agrupamento, pois o agrupamento analisa semelhanças entre os objetos, e o agrupamento de coocorrência vai analisar as semelhanças entre as transações desses objetos.

Os resultados serão as descrições de itens ocorridos em conjunto, incluindo, normalmente estatísticas de frequência e estimativas.

Um exemplo seria: Quais produtos são comprados em conjunto?.

## Perfilamento

Também chamado de Descrição de comportamento, vai caracterizar o comportamentos de um indíviduo, grupo ou população.

Pode trazer descrições mais complexas, reunindo diferentes tipos de dados, e retornando um perfil completo sobre a questão buscada.

Um exemplo seria: O reCAPTCHA que traça um perfil de um usuário real e um perfil de um usuário falso, a fim de evitar fraudes digitais, que analisa a forma que um usuário normalmente utiliza os navegadores e interagem com teclado e mouse.
 
## Previsão de vínculo

Preve ligações entre itens de dados, podendo sugerir desde onde um vínculo pode ocorrer, até a força desse vínculo, normalmente utilizado em redes sociais e serviços de streamming, como Instagram e Netflix.

Um exemplo seria: Quais filmes podemos recomendar para determinado usuário?

## Redução de dados

É uma forma de pegar um grande conjunto de dados, e trocá-lo por um conjunto menor, desde que não sejam perdidos informações importantes do conjunto original, isso irá possibilitar mais facilidade ao processar um conjunto pequeno.

Busca manter os dados mais evidentes, mas a redução acaba gerando perda de informação, portanto é importante manter esse equilíbrio.

Um exemplo seria: Tenho uma base de dados com 10000 pedidos, vou reduzir para 100 pedidos com a maior quantidade de itens.

## Modelagem causal

É utilizado para compreender acontecimentos ou ações que influenciam outras pessoas, essas técnicas compreendem aquelas com um grande investimento em dados, como experimentos randomizados controlados, concluindo de forma causal a partir de dados coletados de forma observacional.

Diferencia situação onde um determinado evento aconteceria ou não, para isso são construídos pressupostos que mantenham a conclusão causal.

Um exemplo seria: Anúncio de um produto - As vendas aumentaram pois os anúncios influenciaram o usuário OU a previsão teve sucesso ao identificar os usuários que teriam comprado de qualquer forma?