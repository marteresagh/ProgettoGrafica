from larlib import *

*** **PROVE**

lines = lines2lines("edificio.lines")
prova=STRUCT(AA(POLYLINE)(lines)) #NON taglia i pezzi in più
VIEW(OFFSET([0.005,0.005])(prova))
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((V,EV))) #grafo pulito
VIEW(OFFSET([0.005,0.005])(prova))


**EDIFICIO DEGLI UFFICI**  3 metri ogni piano a partire da 1.5 sulle z
 **RIALZO**
lines = lines2lines("rialzo_level1.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
grafo=STRUCT(MKPOLS((V,EV))) #grafo pulito
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))

#V[6] da portare nell'origine, spigolo EV[7] da portare a grandezza mondo: 42metri
assert V[6]==[0.0051, 0.5948]
assert V[3]==[0.0051, 1.0]
assert V[9]==[1.0, 1.0]
assert V[9][0]-V[3][0] == 0.9949 #la grandezza massima non è precisa a 1

scala = 41.9/0.9949

W=((mat(V)-V[6])*scala).tolist()

***
**verifica** 
#WW = AA(LIST)(range(len(W)))
#VIEW(larModelNumbering(1,1,1)(W,[WW,EV,FV],STRUCT(MKPOLS((W,EV))),2))
#assert W[9][0]-W[3][0]==41.9
***

***
**celle vuote**
#celle vuote sono 0,1,2, mi serve solo la 3
buchi = STRUCT(MKPOLS([W,[FV[k] for k in range(3)]]))
tot = STRUCT(MKPOLS([W,FV]))
base0= DIFFERENCE([tot,buchi])
#VIEW(base0)
***

rialzo=PROD([base0,Q(1.5)])
VIEW(rialzo)



 
**LEVEL 1_parte 1** 

lines = lines2lines("rialzo_level1.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
grafo=STRUCT(MKPOLS((V,EV))) #grafo pulito
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))

#V[6] da portare nell'origine, spigolo EV[7] da portare a grandezza mondo: 42metri
assert V[6]==[0.0051, 0.5948]
assert V[3]==[0.0051, 1.0]
assert V[9]==[1.0, 1.0]
assert V[9][0]-V[3][0] == 0.9949 #la grandezza massima non è precisa a 1

scala = 41.9/0.9949

W=((mat(V)-V[6])*scala).tolist()

***
**verifica** 
#WW = AA(LIST)(range(len(W)))
#VIEW(larModelNumbering(1,1,1)(W,[WW,EV,FV],STRUCT(MKPOLS((W,EV))),2))
#assert W[9][0]-W[3][0]==41.9
***
#SPIGOLo 2 diverso
EVmuri=set(range(len(EV))).difference({2})
muro = STRUCT(MKPOLS((W,[EV[2]])))
muro=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muro)
muri = STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EVmuri]))
#muri = STRUCT(MKPOLS((W,list(EVmuri))))

#VIEW(OFFSET([0.3,0.3])(base)) #Muri spessi 30 cm circa
muri=OFFSET([0.3,0.3])(muri)
MURI=STRUCT([muro,muri])
level1=PROD([MURI,Q(4.5)])

VIEW(level1)

**COLONNE**
lines = lines2lines("colonne.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
grafo=STRUCT(MKPOLS((V,EV))) #grafo pulito
#VIEW(OFFSET([0.005,0.005])(grafo))

VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))

#V[2] da portare nell'origine, spigolo EV[9] da portare a grandezza mondo: 42metri
assert V[2]==[0.0051, 0.5948]
assert V[1]==[0.0051, 1.0]
assert V[5]==[1.0, 1.0]
assert V[5][0]-V[1][0] == 0.9949 #la grandezza massima non è precisa a 1

scala = 41.9/0.9949

W=((mat(V)-V[2])*scala).tolist()

***
**verifica** 
#WW = AA(LIST)(range(len(W)))
#VIEW(larModelNumbering(1,1,1)(W,[WW,EV,FV],STRUCT(MKPOLS((W,EV))),2))
#assert W[7][0]-W[3][0]==41.9
***

baseC=STRUCT(MKPOLS((W,EV)))
baseC=OFFSET([0.3,0.3])(baseC)

colonne=PROD([baseC,Q(29.5)]) #34-4.5
colonne=T(3)(4.5)(colonne)
VIEW(colonne)




**LEVEL 1_PARTE 2**

lines = lines2lines("uff_level1.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[18] da portare nell'origine, spigolo V[18]V[21] da portare a grandezza mondo: 42metri
assert V[18]==[0.0, 0.5928]
assert V[21]==[1.0, 0.5928]
assert  V[21][0]-V[18][0] == 1.0
scala = 41.9

W=((mat(V)-V[18])*scala).tolist()
base1=STRUCT(MKPOLS((W,EV)))
base1=OFFSET([0.1,0.1])(base1)
level_1=PROD([base1,Q(3)])
level_1=T(3)(1.5)(level_1)
VIEW(level_1)

VIEW(STRUCT([rialzo,level1,colonne,level_1]))
**LEVEL 2**


**PROVA**
***
lines = lines2lines("base_edf.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
grafo=STRUCT(MKPOLS((V,EV))) #grafo pulito
#VIEW(OFFSET([0.005,0.005])(grafo))
***
#numerazione vertici e spigoli

VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1)) 
***

#V[9] da portare nell'origine, spigolo EV[4] da portare a grandezza mondo: 42metri
assert V[9]==[0.0051, 0.5948]
assert V[3]==[0.0051, 1.0]
assert V[7]==[1.0, 1.0]
assert  V[7][0]-V[3][0] == 0.9949 #la grandezza massima non è precisa a 1
scala = 41.9/0.9949

W=((mat(V)-V[9])*scala).tolist()

***
**verifica** 
#WW = AA(LIST)(range(len(W)))
#VIEW(larModelNumbering(1,1,1)(W,[WW,EV,FV],STRUCT(MKPOLS((W,EV))),2))
#assert W[7][0]-W[3][0]==41.9
***

base = (W,FV)
#VIEW(STRUCT(MKPOLS(base)))

rialzo_uff = larModelProduct([base,larQuote1D([1.5])])
#VIEW(STRUCT(MKPOLS(rialzo_uff)))
rialzo_uff=STRUCT(MKPOLS(rialzo_uff))

base = STRUCT(MKPOLS((W,EV)))
#VIEW(OFFSET([0.5,0.5])(base)) #Muri spessi 50 cm circa
base=OFFSET([0.3,0.3])(base)

#VIEW(base)
ufficio=PROD([base,Q(34)])
VIEW(STRUCT([ufficio,rialzo_uff]))


**SALA DELLA PREGHIERA**


