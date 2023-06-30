# Health Insurance Cross Sell Project
![image](https://github.com/EDJR94/pa004_health_insurance/assets/128603807/3e1559a5-7153-457f-a092-cac66c713a11)

## 01. Problema de Negócio

Nosso cliente é uma empresa de seguros que forneceu seguros de saúde aos seus clientes e agora precisa de ajuda para construir um modelo que preveja se os seus clientes segurados do ano passado também estariam interessados em um seguro de veículos fornecido pela empresa.

Construir um modelo para prever se um cliente estaria interessado em um seguro de veículos seria extremamente útil para a empresa, pois ela pode planejar sua estratégia de comunicação de acordo buscando alcançar esses clientes que tem mais interesse, e assim otimizar seu negócio e reduzir custos.

## 02. Premissas

- As variáveis/atributos originais (e seus significados) do conjunto de dados são:

| Coluna | Descrição |
| --- | --- |
| id | ID único para cada cliente |
| gender | Gênero do Cliente |
| age | Idade do Cliente |
| region_code | Código da região em que o cliente mora |
| policy_sales_channel | Código do canal de contato escolhido pelo cliente |
| driving_license | O Cliente possui carteira de motorista? |
| vehicle_age | Idade do carro do Cliente |
| vehicle_damage | O carro já foi danificado alguma vez? |
| previously_insured | O Cliente já foi segurado alguma vez? |
| annual_premium | Valor do prêmio Anual(para seguro de saúde) |
| vintage | Quantos dias faz que o Cliente possui o seguro de saúde? |
| response | O cliente estaria interessado em um seguro de carro? |

## 03. Estratégias de Solução

A estratégia utilizada foi o método CRISP, dividido em 10 partes:

![crisp](https://github.com/EDJR94/pa004_health_insurance/assets/128603807/67b3ae4f-ea88-42e9-9cb4-43eee51cec4a)

1. Questão de Negócio apresentada.
2. Entendimento do Negócio da Empresa de Seguros.
3. Coleta de Dados.
4. Limpeza de Dados.
5. Exploração de Dados.
6. Modelagem dos Dados.
7. Utilização de Modelos de Machine Learning.
8. Avaliação do Algoritmo de Machine Learning.
9. Deploy do Modelo em Produção.
10. Enviar a predição feita e ordená-la usando Google Sheets.

## 04. Melhores Insights do Negócio

Foram levantadas as seguintes hipóteses de negócio de acordo com como funcionava o negócio da Empresa:

1. Pessoas que já possuem um seguro de saúde podem estar mais inclinadas a adquirir um seguro de veículo, pois já têm experiência com seguros.
2. Clientes que possuem um histórico de acidentes de carro podem estar mais interessados em um seguro de veículo.
3. Clientes que possuem um carro mais novo são mais prováveis de adquirirem o seguro.
4. A idade do cliente pode ser um fator importante, com os clientes mais jovens sendo menos propensos a adquirir um seguro de veículo.
5. A localização geográfica dos clientes pode ser um fator importante, com as pessoas que moram em áreas com altos índices de roubos de veículos sendo mais propensas a adquirir um seguro de veículo.
6. O gênero do cliente pode ser um fator, com homens sendo mais propensos a adquirir um seguro de veículo.
7. O preço do seguro de veículo pode ser um fator importante, com clientes mais propensos a adquirir um seguro de veículo se os preços estiverem competitivos.
8. Clientes com CNH são mais propensos a adquirirem o seguro.
9. Pessoas que já tinham seguros anteriormente tendem a querer o seguro, pois já têm experiência.
10. Pessoas que são notificadas por algum meio específico(ex: telefone) podem tender a querer o seguro

Dentre todas as hipóteses as **mais relevantes(Insights)** na minha opinião foram as seguintes:

1. **Clientes que possuem um carro mais novo são mais prováveis de adquirirem o seguro.**
    
    Podemos ver pelo gráfico que a maioria dos clientes que estariam interessados são clientes com carro usado (Entre 1 e 2 anos de uso) e não carros novos (Menos de 1 ano de uso)
    
    ![Untitled](https://github.com/EDJR94/pa004_health_insurance/assets/128603807/cf866d2a-d9cd-41be-b05b-c22459c7404e)

    
2. **Pessoas mais jovens geralmente não querem adquirir o seguro.**
    
    Essa hipótese é verdadeira, mas gostaria de destacar que as idades que têm uma procura muito maior que as outras ficam entre 40-50 anos, como podemos ver no gráfico abaixo:
    
    ![image](https://github.com/EDJR94/pa004_health_insurance/assets/128603807/ad861d37-b944-4391-8a2c-4957a73ac806)

    

## 05. Machine Learning

Foram usados os seguintes modelos de Machine Learning para analisar a previsão das vendas:

- *LogisticRegression*
- *Dummy Classifier*
- *RandomForestClassifier*
- *XGB Classifier*
- *Light GBM Classifier*

Após analisar as métricas (Precision, Recall, F1 Score, Accuracy ROC AUC Curve) optei por seguir com o *Light GBM Classifier* pois foi o que apresentou as melhores métricas no geral:

| Model Name | Precisão at K | Recall at K | F1 at K | Acurácia at K | ROC AUC at K |
| --- | --- | --- | --- | --- | --- |
| Light GBM | 0.40900 | 0.218483 | 0.284819 | 0.876824 | 0.856095 |
| XGBoost Classifier | 0.39350 | 0.210203 | 0.274025 | 0.876250 | 0.854232 |
| Random Forest | 0.34600 | 0.184829 | 0.240947 | 0.866657 | 0.831897 |
| Logistic Regression | 0.31175 | 0.166533 | 0.217096 | 0.877185 | 0.833658 |
| Dummy Classifier | 0.12425 | 0.066373 | 0.086525 | 0.877202 | 0.500000 |

O modelo Final, após ajustado os hiperparâmetros, treinado e aplicado sobre os dados de Teste(nunca vistos pelo modelo) teve a seguinte performance:

| Model Name | Precisão at K | Recall at K | F1 at K | Acurácia at K | ROC AUC at K |
| --- | --- | --- | --- | --- | --- |
| Light GBM | 0.44225 | 0.185761 | 0.261628 | 0.875312 | 0.861079 |

## 06. Tradução do Modelo para o Negócio

A partir das previsões feitas pelo modelo podemos tirar algumas conclusões. 

Considerando-se que para cada cliente que a empresa consiga vender o seguro de carro ela tenho um Lucro Bruto de R$540,00. Vamos considerar também que a empresa pretende ligar para esses potenciais clientes e cada ligação tenha um custo total de R$40,00.

Observado o gráfico abaixo, os primeiros clientes são os com a maior probalidade de aceitarem o seguro de carro. Porém chega um momento que a empresa começa a ligar para os clientes que não têm uma chance muito alta de comprar o seguro e o custo começa a se destacar e diminuir o lucro.

![Untitled (2)](https://github.com/EDJR94/pa004_health_insurance/assets/128603807/f9e0c2bd-b3e9-48eb-aa9a-c4d4602311d6)


Ou seja, a empresa precisa ligar para 46% da base de clientes(que são os que tem a maior probabilidade de aceitar o seguro) para ter o lucro máximo:

→ Lucro ligando até o cliente 35103: R$3.429.452,90

→ Lucro Ligando para a base toda de clientes: R$1.962.802,77

É um lucro 1.74 vezes maior usando o modelo.

## 06. Planilha do Google Sheets

Após enviar o modelo para produção, fiz uma planilha no Google Sheets que, dado as informações do cliente, acessa meu modelo na Nuvem, faz as predições e retorna uma lista rankeada com os melhores clientes para ligar no topo da lista, como no exemplo a seguir:

![gif google sheets](https://github.com/EDJR94/pa004_health_insurance/assets/128603807/ccd6c55c-b610-43aa-9d82-cc5bca362591)

## 07. Produto Final e Conclusão

O produto final foi uma planilha no Google Sheets que faz a previsão e ordena os clientes que tem a maior probabilidade de adquirir o seguro de carro para que a empresa de seguros entre em contato apenas com os potenciais clientes. Essa planilha pode ser acessada de qualquer dispositivo com acesso à internet que possua o aplicativo do Google Sheets.

## 08. Próximos Passos

Realizar mais Ciclos do CRISP focando em:

- Testar outros modelos de Machine Learning/Aperfeiçoar os parâmetros para refinar o modelo;
- Criar outras características(features) para o modelo a partir dos dados existentes;
- Utilizas outras estratégias para definir os Hyperparâmetros do modelo;
- Otimizar o modelo para fazer a previsão e ordenar as clientes no Excel.

## Referências

Conjunto de dados: [https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction)
