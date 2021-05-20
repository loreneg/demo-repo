# Regressione linare, non so esattamente cosa sia, spiegazione in fondo della regressione lineare semplice
from scipy import stats
import matplotlib.pyplot as plt
from random import *


bias = 3.0
scale = 0.7
err = 5.0
x = []
y = []
for i in range(100):
    x.append(-20.0 + 40.0*random())
    y.append(scale*x[i] + bias + gauss(0, 3))
    # errori sistematici di bias e scale + errore casuale gaussiano (curva di Gauss spiegata nei miei appunti di sistemi
    # a pag. 54 degli appunti scritti in blu)


# calcolo regressione lineare
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)


# PLOT:
# campioni
plt.scatter(x, y)
# retta ideale
plt.plot(x, x, c='r')
# retta approssimante
yy = []
for v in x:
    yy.append(intercept + slope*v)
plt.plot(x, yy, 'b', label='fitted line')
plt.grid()
plt.show()

"""
REGRESSIONE LINEARE:
La regressione formalizza e risolve il problema di una relazione funzionale tra variabili misurate sulla base di dati 
campionari estratti da un'ipotetica popolazione infinita. Originariamente Galton utilizzava il termine come sinonimo di
correlazione, tuttavia oggi in statistica l'analisi della regressione è associata alla risoluzione del modello lineare. 
Per la loro versatilità, le tecniche della regressione lineare trovano impiego nel campo delle scienze applicate: 
chimica, geologia, biologia, fisica, ingegneria, medicina, nonché nelle scienze sociali: economia, linguistica, 
psicologia e sociologia.
Più formalmente, in statistica la regressione lineare rappresenta un metodo di stima del valore atteso condizionato di 
una variabile dipendente, o endogena, Y, dati i valori di altre variabili indipendenti, o esogene, 
X1, ..., Xk:  E=[Y | X1, ..., Xk], dove E è l'insieme delle Y tali che X sia compresa tra X1 e Xk.
L'uso dei termini endogeno/esogeno è talvolta criticato, In quanto implicherebbe una nozione di causalità che 
l'esistenza di una regressione non prevede; in determinati contesti, provocherebbe inoltre confusione, essendo ad 
esempio il concetto di esogeneità in econometria formalmente definito tramite l'ipotesi di ortogonalità alla base delle 
proprietà statistiche della regressione lineare col metodo dei minimi quadrati.


Introduzione alla REGRESSIONE LINEARE SEMPLICE:
Il modello di regressione lineare è:
Yi = Beta{0} + (Beta{1} * Xi) + ui
dove:
- i varia tra le osservazioni, i = 1, ..., n
- Yi è la variabile dipendente
- Xi è la variabile indipendente o regressore
- Beta{0} + (Beta{1} * X) è la retta di regressione o funzione di regressione della popolazione
- Beta{0} è l'intercetta della retta di regressione della popolazione
- Beta{1} è il coefficiente angolare della retta di regressione della popolazione
- ui è l'errore statistico

"""