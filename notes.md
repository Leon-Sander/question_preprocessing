Wie kommt man anhand der Frage auf die Typen 1-4?
Regex?

Question Types:

1. [IR single] About content of a given paper. 
2. [IR global] Content-wise for one or several papers in corpus (with unknown title)

Bei den IR Fragen unterscheidung zwischen Plain und with annotations.
Plain: 

3. [KG single] Retrieve metadata for one paper (Title known or unknown, see above)
4. [KG global] Retrieve metadata for several papers in the corpus (Maybe presenting as table or diagram if numerical values)

Diese Aufgabe ist in meinem code das Template Matching. Erstmal simple Aufteilung in kg oder ir.



Idee: Erstmal Regex matches, dann mit paper ids aus dem makg auffüllen und ein BERT classification Modell trainieren.