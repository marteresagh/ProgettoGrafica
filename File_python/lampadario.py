from larlib import *
lines = lines2lines("lampadario.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[79][1]-V[182][1]: 0.6268
scala = 13/0.34

W=((mat(V)-V[15])*scala).tolist()

base=STRUCT(MKPOLS((W,EV)))
frame=OFFSET([0.05,0.05])(base)
lampadario=T([1,2,3])([33, 8.2,20])(PROD([frame,Q(0.05)]))
#VIEW(STRUCT([lampadario,STRUTTURA]))

