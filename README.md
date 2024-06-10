# Battle Royale: Qual o melhor material?

## Otimização Band gap e Calor de Formação

_Grupo: Natália Alcantara, Samira Oliveira e Geovana Bettero_

Este repositório trata-se de um trabalho final feito por três estudantes da ILUM Escola de Ciência. O trabalho se concentra na criação de um Algoritmo Genético com o objetivo de maximizar o Band Gap e minimizar o Calor de Formação. O dataset utilizado foi retirado de um dados chamado (C2DB) de materiais 2D e contém propriedades estruturais, termodinâmicas, elásticas, eletrônicas, magnéticas e ópticas de cerca de 4.000 materiais bidimensionais distribuídos em mais de 40 estruturas cristalinas diferentes. Para montagem do dataset foram escolhidas algumas colunas do banco para sua formulação, como visto a seguir.

<l>
<b><br>Importância<br></b>
 Na engenharia de materiais e na indústria eletrônica determinar o comportamento de um material é de extrema importancia. Assim, conhecer o band gap  de um material é crucial para projetar novos materiais com propriedades específicas, como semicondutores para dispositivos eletrônicos. Desta forma, com algoritmos genéticos tornou-se possível maximizar ou minimizar dado objetivo com maior precisão e eficiência, facilitando o desenvolvimento de materiais com propriedades sob medida para diversas aplicações.
 

<img src="https://cloud.squidex.io/api/assets/matmatch-cms/d96c504d-2d4b-40fd-9954-693d434344b0/screenshot-2020-05-05-at-16.04.35.png" alt="Imagem ilustrativa de um Band Gap" width="400"/>
    <p><i>Imagem ilustrativa de um Band Gap</i></p>
<hr>
<b><br>Informações sobre o Dataset<br></b>
O Dataset em questão possui os seguintes atributos:

_Heat of formation(eV/atom):_<br> O calor de formação é a quantidade de energia liberada ou absorvida quando um composto é formado a partir de seus elementos constituintes. Ele pode indicar a estabilidade do material e sua capacidade de formar ligações químicas. É o nosso alvo para minimização. 

_Eletronegativity:_<br> A eletronegatividade é a tendência de um átomo de atrair elétrons para si mesmo quando está ligado a outro átomo, o que pode influenciar a polaridade das ligações químicas.

_Band gap:_<br> O band gap é a energia necessária para excitar um elétron de um estado ligado para um estado não ligado (condução) e é o alvo de maximização.

_Elementos presentes nos materiais do dataset:_<br> Esses elementos parcionados podem ser utilizados para previsões de outros materiais 2D que não estão no dataset.

<hr>
<Sobre o projeto>
Antes de implementar o algoritmo genético, dois modelos de machine learning utilizando Floresta Aleatória foi utilizado para prever o band gap e o calor formação com base nos elementos parcionado dos materiais pertencentes do dataset, para que dessa forma, fosse possível o material mais propricio com as caracteristicas desejadas. 

<b><br> Funcionamento Código e Utilização <br></b>

O código deste repositório emprega uma Algoritmo Genético utilizando Python puro. Nos notebooks fornecidos, há uma explicação detalhada do processo, abrangendo desde a criação dos modelos até a implementação do algoritmo genético. Vale ressaltar que para implementação do algorimto utilizamos os operadores de seleção por roleta máxima, cruzamento ponto duplo e com uma mutação "personalizada" para o problema. As etapas do processo são descritas no notebook e no script do código, fornecendo os detalhes. Este repositório serve como um recurso valioso para aqueles que desejam entender e aplicar métodos de aprendizado de máquina para otimização em materiais 2D.

<b><br>Bibliotecas<br></b>
As Bibliotecas e funções usadas e necessárias para importação: Pandas, matplotlib, numpy e sklearn .  

<hr>

<b>Documentos no Github<br></b>

_C2DB_full.csv_: Dataset completo


<hr>
<b><br>Conclusão<br></b>
Ao final, o algoritmo genético retornará um material 2D que atende os requisitos estabelicidos de maximização e minimização. 

<hr>
<b><br>Referências<br></b>

[1] Banco de dados C2DB: https://cmr.fysik.dtu.dk/c2db/c2db.html#brief-description 

[2] CASSAR, D. R. Floresta Aleatória (2023)
