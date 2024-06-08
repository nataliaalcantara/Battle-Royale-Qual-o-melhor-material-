# Trabalho-Algoritmo-Genetico-

# Band Gap and Heat of Formation Optimization
_Grupo: Natália Alcantara, Samira Oliveira e Geovana Bettero_

Este repositório trata-se de um trabalho final feito por três estudantes da ILUM Escola de Ciência. O trabalho se concentra na criação de um Algoritmo Genético com o objetivo de maximizar o Band Gap e minimizar o Calor de Formação. O dataset utilizado foi retirado de um dados chamado (C2DB) de materiais 2D e contém propriedades estruturais, termodinâmicas, elásticas, eletrônicas, magnéticas e ópticas de cerca de 4.000 materiais bidimensionais distribuídos em mais de 40 estruturas cristalinas diferentes. Para montagem do dataset foram escolhidas algumas colunas do banco para sua formulação, como visto a seguir.

<hr>
<b><br>Importância<br></b>
 Na engenharia de materiais e na indústria eletrônica determinar o comportamento de um material é de extrema importancia. Assim, conhecer o band gap  de um material é crucial para projetar novos materiais com propriedades específicas, como semicondutores para dispositivos eletrônicos. Desta forma, com algoritmos genéticos tornou-se possível maximizar ou minimizar dado objetivo com maior precisão e eficiência, facilitando o desenvolvimento de materiais com propriedades sob medida para diversas aplicações.


<img src="https://nirajchawake.wordpress.com/wp-content/uploads/2014/10/picture1.png" width="400">
    <p><i>Imagem ilustrativa de um Band Gap</i></p>

  
<hr>
<b><br>Informações sobre o Dataset<br></b>
O Dataset em questão possui os seguintes atributos:


_Fórmula:_<br>A fórmula química que indica sua composição atômica.

_Thermodynamic stability level:_<br>  A estabilidade termodinâmica de um material afeta diretamente suas propriedades físicas e eletrônicas. Materiais mais estáveis tendem a ter uma estrutura cristalina mais ordenada.

_Energy(ev/atom):_<br>  A energia total do sistema que pode fornecer informações sobre a força das ligações químicas presentes no material

_Work function(eV):_<br> A função de trabalho é a energia mínima necessária para remover um elétron de um material para o vácuo. Ela está  relacionada à energia de Fermi do material e pode afetar o comportamento dos elétrons na superfície do material.

_Heat of formation(eV/atom):_<br> O calor de formação é a quantidade de energia liberada ou absorvida quando um composto é formado a partir de seus elementos constituintes. Ele pode indicar a estabilidade do material e sua capacidade de formar ligações químicas. É o nosso alvo para minimização. 

_Space group number:_<br>  O grupo espacial descreve a simetria da estrutura cristalina do material, podendo afetar a dispersão de elétrons e lacunas na estrutura de bandas. Seu número vai de 1 a 230 e cada grupo representa uma simetria diferente de um cristal periódico.

_Volume of unity cell(Å³):_<br> O volume da célula unitária está diretamente relacionado à densidade do material e à distância média entre os átomos.

_Eletronegativity:_<br> A eletronegatividade é a tendência de um átomo de atrair elétrons para si mesmo quando está ligado a outro átomo, o que pode influenciar a polaridade das ligações químicas.

_Band gap:_<br> O band gap é a energia necessária para excitar um elétron de um estado ligado para um estado não ligado (condução) e é o alvo de maximização.

_Elementos presentes nos materiais do dataset:_<br> Esses elementos parcionados podem ser utilizados para previsões de outros materiais que não estão no dataset.

<hr>
<Sobre o projeto>
Antes de implementar o algoritmo genético, dois modelos de machine learning utilizando Floresta Aleatória foi utilizado para prever o band gap e o calor formação apartir esses elementos parcionado dos materiais pertencentes do dataset, para que dessa forma, fosse possível o material mais propricio com oas caracteristicas desejadas. 

<b><br> Funcionamento Código e Utilização <br></b>

O código deste repositório emprega uma Algoritmo Genético utilizando o módulo DEAP. Nos notebooks fornecidos, há uma explicação detalhada do processo, abrangendo desde a criação dos modelos até a implemntação do algoritmo genético. As etapas do processo são descritas no notebook, fornecendo detalhes. Este repositório serve como um recurso valioso para aqueles que desejam entender e aplicar métodos de aprendizado de máquina para otimização em materiais 2D.

<b><br>Bibliotecas<br></b>
As Bibliotecas e funções usadas e necessárias para importação: Pandas, re, deap, matplotlib, numpy e sklearn .  

<hr>

<b>Documentos no Github<br></b>

_C2DB_full.csv_: Dataset completo


<hr>
<b><br>Conclusão<br></b>


<hr>
<b><br>Referências<br></b>

[1] Banco de dados C2DB: https://cmr.fysik.dtu.dk/c2db/c2db.html#brief-description 

[2] CASSAR, D. R. PyTorch Lightning. (2024)
