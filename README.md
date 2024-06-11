# Battle Royale: Qual o melhor material?

## Otimização Band gap e Calor de Formação

_Grupo: Natália Alcantara, Samira Oliveira e Geovana Bettero_

Este repositório trat-se do trabalho final desenvolvido por três estudantes da ILUM Escola de Ciência. O projeto tem como foco a criação de um Algoritmo Genético com o objetivo de maximizar o Band Gap e minimizar o Calor de Formação em materiais 2D. O dataset utilizado foi extraído do conjunto de dados (C2DB), que contém informações estruturais, termodinâmicas, elásticas, eletrônicas, magnéticas e ópticas de aproximadamente 4.000 materiais bidimensionais, abrangendo mais de 40 estruturas cristalinas diferentes.

---
<b><br>Importância<br></b>
Na engenharia de materiais e na indústria eletrônica, compreender o comportamento dos materiais é crucial. O conhecimento do band gap de um material é especialmente importante, pois é fundamental para o projeto de novos materiais com propriedades específicas, como semicondutores para dispositivos eletrônicos. Com a aplicação de algoritmos genéticos, agora é possível otimizar objetivos específicos, maximizando ou minimizando-os com maior precisão e eficiência. Isso facilita significativamente o desenvolvimento de materiais com propriedades personalizadas para uma ampla variedade de aplicações.

<img src="https://cloud.squidex.io/api/assets/matmatch-cms/d96c504d-2d4b-40fd-9954-693d434344b0/screenshot-2020-05-05-at-16.04.35.png" alt="Imagem ilustrativa de um Band Gap" width="400"/>
    <p><i>Imagem ilustrativa de um Band Gap</i></p>
<hr>
<b><br>Objetivo do Projeto<br></b>
O objetivo deste projeto é identificar materiais bidimensionais (2D) com um maior band gap e um menor calor de formação. Utilizamos algoritmos genéticos para otimizar essas propriedades, permitindo a descoberta eficiente de materiais com as características desejáveis.

<b><br>Informações sobre o Dataset<br></b>
Neste trabalho, utilizamos um conjunto de dados que contém diversas propriedades dos materiais, essenciais para a compreensão e otimização de materiais bidimensionais (2D). As colunas relevantes para este estudo são:

_Heat of formation(eV/atom):_<br> O calor de formação representa a quantidade de energia liberada ou absorvida durante a formação de um composto a partir de seus elementos constituintes. Essa medida é crucial para avaliar a estabilidade do material e sua capacidade de formar ligações químicas. Nosso objetivo é minimizá-la.

_Eletronegativity:_<br> Este atributo indica a tendência de um átomo atrair elétrons para si mesmo quando está ligado a outro átomo, o que pode influenciar a polaridade das ligações químicas.

_Band gap:_<br>O band gap é a energia necessária para excitar um elétron de um estado ligado para um estado não ligado (estado de condução). Este é um dos principais focos de nossa otimização, buscando maximizar esse valor.

_Elementos presentes nos materiais do dataset:_<br> Esta coluna detalha os elementos químicos presentes nos materiais contidos no conjunto de dados. Essa informação pode ser útil para prever propriedades de outros materiais 2D que ainda não estão incluídos no dataset.


<hr>
<Sobre o projeto>
Antes de implementarmos o algoritmo genético, exploramos duas abordagens de machine learning utilizando o algoritmo de Floresta Aleatória. Estes modelos foram desenvolvidos para prever o band gap e o calor de formação com base nos elementos químicos presentes nos materiais do dataset. Essa etapa foi crucial para identificar os materiais mais promissores com as características desejadas, fornecendo uma base sólida para a aplicação posterior do algoritmo genético.
    
<b><br> Funcionamento Código e Utilização <br></b>

Este repositório contém a implementação de um Algoritmo Genético utilizando Python puro. Nos notebooks disponíveis, você encontrará uma explicação detalhada de todo o processo, desde a criação dos modelos iniciais até a implementação do algoritmo em si. É importante destacar que para a implementação, utilizamos os operadores de seleção por roleta máxima, cruzamento ponto duplo e uma mutação "personalizada" para o problema específico em questão. Todas as etapas do processo são descritas tanto nos notebooks quanto no script do código, fornecendo detalhes  sobre o funcionamento e sua utilização. Este repositório serve como um recurso valioso para aqueles que desejam compreender e aplicar métodos de aprendizado de máquina para otimização em materiais bidimensionais.

<b><br>Bibliotecas<br></b>
As Bibliotecas e funções usadas e necessárias para importação: Pandas, matplotlib, numpy e sklearn .  

<hr>

<b>Arquivos no Github<br></b>

dataset_C2DB.csv: Este é o dataset completo que contém todas as informações necessárias para o projeto.

ALGORITMO: Este arquivo Jupyter Notebook contém a implementação do algoritmo genético utilizado para a otimização.

funcoes.py: Este é um script Python que contém as funções essenciais para a execução do algoritmo genético. Inclui funcionalidades para a criação dos candidatos, população, genes, função objetivo, bem como as etapas de seleção, cruzamento e mutação.

modelo_band_gap.ipynb: Este arquivo Jupyter Notebook contém a implementação do modelo de Floresta Aleatória para previsão do band gap.

modelo_calor_formacao.ipynb: Este arquivo Jupyter Notebook contém a implementação do modelo de Floresta Aleatória para previsão do calor de formação.

modelo_rf_bg.pkl: Este arquivo contém o modelo de previsão de band gap treinado.

modelo_rf_cf.pkl: Este arquivo contém o modelo de previsão de calor de formação treinado.


<hr>
<b><br>Conclusão<br></b>
Ao término do processo, o algoritmo genético fornecerá como resultado um material 2D que satisfaz os critérios de maximização e minimização estabelecidos.

<hr>
<b><br>Referências<br></b>

[1] Banco de dados C2DB: https://cmr.fysik.dtu.dk/c2db/c2db.html#brief-description 

[2] CASSAR, D. R. Floresta Aleatória (2023)
