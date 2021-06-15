Wie kommt man anhand der Frage auf die Typen 1-4?
Regex?

Question Types:

1. [IR single] About content of a given paper. 
2. [IR global] Content-wise for one or several papers in corpus (with unknown title)

Bei den IR Fragen unterscheidung zwischen Plain und with annotations.
Plain: 

3. [KG single] Retrieve metadata for one paper (Title known or unknown, see above)
4. [KG global] Retrieve metadata for several papers in the corpus (Maybe presenting as table or diagram if numerical values)




Idee: Erstmal Regex matches, dann mit paper ids aus dem makg auffüllen und ein BERT classification Modell trainieren.


Aktiv/passiv Vergangenheit/Zukunft 
Annotation -> Which Method/dataset

IMRAD
Diese Abkürzung steht für Introduction (Einführung), Methods (Methoden), Results (Ergebnisse) And Discussion (und Diskussion)
Muss man für die Informationen in einer section schauen -> IMRAD = True, ansonsten im ganzen Dokument -> False

Bsp:
“Which ML methods have been used by author Y?” -> section methods
“Which data sets have been introduced in papers at conference Z?” -> section data


Idee wie eine application am Ende aussehen könnte: Es gibt schaltflächen mit Infos die man wissen will, bspw etwas über ein dataset -> dann kommen templates und man muss nur noch ein paar Informationen ausfüllen wie das Paper über das mans wissen will.



Annotation mode nur wenn Frage über dataset/methods ist
bsp: "Which dataset is used in the Paper 'On Emerging Entity Detection'"