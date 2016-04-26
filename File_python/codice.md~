from larlib import *

#**PROVE**

#lines = lines2lines("edificio.lines")
#prova=STRUCT(AA(POLYLINE)(lines)) #NON taglia i pezzi in più
#VIEW(OFFSET([0.005,0.005])(prova))
#V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
#prova=STRUCT(MKPOLS((V,EV))) #grafo pulito
#VIEW(OFFSET([0.005,0.005])(prova))


#**EDIFICIO DEGLI UFFICI**  3 metri ogni piano a partire da 1.5 sulle z
# **RIALZO**
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

#***
#**verifica** 
#WW = AA(LIST)(range(len(W)))
#VIEW(larModelNumbering(1,1,1)(W,[WW,EV,FV],STRUCT(MKPOLS((W,EV))),2))
#assert W[9][0]-W[3][0]==41.9
#***

#***
#**celle vuote**
#celle vuote sono 0,1,2, mi serve solo la 3
buchi = STRUCT(MKPOLS((W,[FV[0]])))
tot = STRUCT(MKPOLS([W,FV]))
base0= DIFFERENCE([tot,buchi])
VIEW(base0)
***

rialzo=PROD([base0,Q(1.5)])
#VIEW(rialzo)



 
#**LEVEL 1_muri esterni** 

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

#mura esterne piu basse
EV_bassi=sorted([1,3,5,0,10,12,16,7])
EV_alti= set(range(len(EV))).difference(EV_bassi)
muri_bassi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_bassi]))
muri_alti=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_alti]))
#***
#**verifica** 
#WW = AA(LIST)(range(len(W)))
#VIEW(larModelNumbering(1,1,1)(W,[WW,EV,FV],STRUCT(MKPOLS((W,EV))),2))
#assert W[9][0]-W[3][0]==41.9
***
#SPIGOLo 2 diverso
EVmuri=set(range(len(EV))).difference({2})
muro = STRUCT(MKPOLS((W,[EV[2]])))
muro=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muro)
muri = STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_alti]))

muri_bassi=OFFSET([0.3,0.3])(muri_bassi)

#VIEW(OFFSET([0.3,0.3])(base)) #Muri spessi 30 cm circa
muri=OFFSET([0.3,0.3])(muri)
MURI_alti=STRUCT([muro,muri])
wall_1=PROD([MURI_alti,Q(4.5)])
wall_2=PROD([muri_bassi,Q(1.5)])
level1=STRUCT([wall_1,wall_2])
#VIEW(level1)

#**COLONNE**
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

#non voglio le mura di contorno perchè ddevono avere dei buchi per il passaggio
EV_no=sorted([0,1,7,5,10,2,3,9])
EV_si= set(range(len(EV))).difference(EV_no)

#***
#**verifica** 
#WW = AA(LIST)(range(len(W)))
#VIEW(larModelNumbering(1,1,1)(W,[WW,EV,FV],STRUCT(MKPOLS((W,EV))),2))
#assert W[7][0]-W[3][0]==41.9
***

baseC=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_si]))
baseC=OFFSET([0.3,0.3])(baseC)

colonne=PROD([baseC,Q(29.5)]) #34-4.5
colonne=T(3)(4.5)(colonne)
#VIEW(colonne)


#**LEVEL 1_muri interni**

lines = lines2lines("uff_level1.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[3] da portare nell'origine, spigolo V[18]V[21] da portare a grandezza mondo: 42metri
assert V[3]==[0.0, 0.5928]
assert V[21]==[1.0, 0.5928]
assert  V[21][0]-V[18][0] == 1.0
scala = 41.9

W=((mat(V)-V[3])*scala).tolist()

#muri fini e muri spessi
EV_spessi=sorted([12,1,0,15,11,10,14])
EV_fini= set(range(len(EV))).difference(EV_spessi)
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))
muri_fini=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_fini]))

muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_1=PROD([muri_spessi,Q(3)])
muri_fini=OFFSET([0.15,0.15])(muri_fini)
wall_1=PROD([muri_spessi,Q(3)])
wall_2=PROD([muri_fini,Q(3)])
level_1=STRUCT([wall_1,wall_2])

level_1=T(3)(1.5)(level_1)
#VIEW(level_1)

VIEW(STRUCT([rialzo,level1,colonne,level_1]))

#**LEVEL 2**
lines = lines2lines("uff_level2.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[40] da portare nell'origine, spigolo V[40]V[23] da portare a grandezza mondo: 42metri
assert V[40]==[0.0, 0.5928]
assert V[23]==[1.0, 0.5928]
assert V[40][0]-V[23][0] == 1.0
scala = 41.9

W=((mat(V)-V[40])*scala).tolist()

#muri fini e muri spessi
EV_spessi=sorted([28,1,7,38,0,27,32,45,42,8,9,34,13,44,16])
EV_fini= set(range(len(EV))).difference(EV_spessi)
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))
muri_fini=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_fini]))

muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_1=PROD([muri_spessi,Q(3)])
muri_fini=OFFSET([0.15,0.15])(muri_fini)
wall_1=PROD([muri_spessi,Q(3)])
wall_2=PROD([muri_fini,Q(3)])
level_2=STRUCT([wall_1,wall_2])

level_2=T(3)(4.5)(level_2)
#VIEW(level_2)

VIEW(STRUCT([rialzo,level1,colonne,level_1,level_2]))

#**LEVEL 3**

lines = lines2lines("uff_level3.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[38] da portare nell'origine, spigolo V[38]V[22] da portare a grandezza mondo: 42metri
assert V[38]==[0.0, 0.5928]
assert V[22]==[1.0, 0.5928]
assert V[38][0]-V[22][0] == 1.0
scala = 41.9

W=((mat(V)-V[38])*scala).tolist()

#muri fini e muri spessi
EV_spessi=sorted([30,1,41,8,37,12,19,38,39,21,15,42,45,4,6,40,13,14])
EV_fini= set(range(len(EV))).difference(EV_spessi)
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))
muri_fini=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_fini]))

muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_1=PROD([muri_spessi,Q(3)])
muri_fini=OFFSET([0.15,0.15])(muri_fini)
wall_1=PROD([muri_spessi,Q(3)])
wall_2=PROD([muri_fini,Q(3)])
level_3=STRUCT([wall_1,wall_2])

level_3=T(3)(7.5)(level_3)
level_3up=STRUCT(NN(4)([level_3,T(3)(6)]))


#VIEW(level_3)
#VIEW(level_3up)

VIEW(STRUCT([rialzo,level1,colonne,level_1,level_2,level_3,level_3up]))

#**LEVEL 4**

lines = lines2lines("uff_level4.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[42] da portare nell'origine, spigolo V[42]V[27] da portare a grandezza mondo: 42metri
assert V[42]==[0.0, 0.5928]
assert V[27]==[1.0, 0.5928]
assert V[42][0]-V[27][0] == 1.0
scala = 41.9

W=((mat(V)-V[42])*scala).tolist()

#muri fini e muri spessi
EV_spessi=sorted([37,22,5,46,9,27,40,8,12,50,49,14,38,1,33,7,32])
EV_fini= set(range(len(EV))).difference(EV_spessi)
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))
muri_fini=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_fini]))

muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_1=PROD([muri_spessi,Q(3)])
muri_fini=OFFSET([0.15,0.15])(muri_fini)
wall_1=PROD([muri_spessi,Q(3)])
wall_2=PROD([muri_fini,Q(3)])
level_4=STRUCT([wall_1,wall_2])

level_4=T(3)(10.5)(level_4)
level_4up=STRUCT(NN(3)([level_4,T(3)(6)]))

#**ultimo livello da concludere**
lines = lines2lines("finale.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))
W=((mat(V)-V[5])*scala).tolist()
base=STRUCT(MKPOLS((W,EV)))
finale=OFFSET([0.3,0.3])(base)
finale=T(3)(28.5)(PROD([finale,Q(5.5)]))

#dettagli
***
lines = lines2lines("rialzo_level1.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
grafo=STRUCT(MKPOLS((V,EV))) #grafo pulito
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))

scala = 41.9/0.9949

W=((mat(V)-V[6])*scala).tolist()

#***
#**verifica** 
#WW = AA(LIST)(range(len(W)))
#VIEW(larModelNumbering(1,1,1)(W,[WW,EV,FV],STRUCT(MKPOLS((W,EV))),2))
#assert W[9][0]-W[3][0]==41.9
EV_cut=sorted([2,4,14,13])
EV_righe= set(range(len(EV))).difference(EV_cut)
frame=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_righe]))

righe = T([1,2])([-0.15,-0.15])( OFFSET([0.60,0.60])(frame))
RIGHE=PROD([righe,INTERVALS(0.20)(1)])
MARMO=T(3)(1.4)(RIGHE)
rip_MARMO=STRUCT(NN(11)([MARMO,T(3)(3)]))


#VIEW(level_4)
#VIEW(level_4up)
EDF_UFF=STRUCT([rialzo,level1,colonne,level_1,level_2,level_3up,level_4up,finale,rip_MARMO])
VIEW(EDF_UFF)

#**PAVIMENTI**
#**pavimento level 2**
lines = lines2lines("pavimento_level2.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
#prova=STRUCT(MKPOLS((V,FV))) #grafo pulito
#VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
#VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))
#V[26] da portare nell'origine, spigolo EV[18] da portare a grandezza mondo: 42metri
assert Y[26]==[0.0, 0.5928]
assert Y[26][0]-Y[7][0] == 1.0
scala = 41.9
Z=((mat(Y)-Y[26])*scala).tolist()
ZZ = AA(LIST)(range(len(Z)))
submodel = STRUCT(MKPOLS((Z,EV)))
#VIEW(larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,0.1))
#**celle vuote**
#celle vuote sono 0,1,2,7,65,4, mi serve solo la 3
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [0,1,2,4,5,7,6]]]))
tot = STRUCT(MKPOLS([Z,FV]))
pavimento_level2= DIFFERENCE([tot,buchi])
pavimento_level2=T(3)(4.25)(PROD([pavimento_level2,Q(0.3)]))
#VIEW(pavimento_level2)
VIEW(STRUCT([EDF_UFF,pavimento_level2]))


#**pavimento level3**
lines = lines2lines("pavimento_level3.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
#prova=STRUCT(MKPOLS((V,FV))) #grafo pulito
#VIEW(prova)

VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))
#V[21] da portare nell'origine a grandezza mondo: 42metri
assert V[21]==[0.0, 0.5928]
scala = 41.9
W=((mat(V)-V[21])*scala).tolist()
#**celle vuote**
#celle vuote sono 0,4,3,8,9,5,6,2 mi serve  la 7,1
buchi = STRUCT(MKPOLS([W,[FV[k] for k in [0,4,3,8,9,5,6,2]]]))
tot = STRUCT(MKPOLS([W,FV]))
pavimento_level3= DIFFERENCE([tot,buchi])
pavimento_level3=T(3)(7.25)(PROD([pavimento_level3,Q(0.3)]))
#VIEW(pavimento_level3)
VIEW(STRUCT([EDF_UFF,pavimento_level3,pavimento_level2]))

#**pavimento level4**
lines = lines2lines("pavimento_level3.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
#prova=STRUCT(MKPOLS((V,FV))) #grafo pulito
#VIEW(prova)

VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))
#V[21] da portare nell'origine a grandezza mondo: 42metri
assert V[21]==[0.0, 0.5928]
scala = 41.9
W=((mat(V)-V[21])*scala).tolist()
#**celle vuote**
#celle vuote sono 0,4,3,8,9,5,6,2 mi serve  la 7,1
buchi = STRUCT(MKPOLS([W,[FV[k] for k in [3,8,9,5,6,2]]]))
tot = STRUCT(MKPOLS([W,FV]))
pavimento_level4= DIFFERENCE([tot,buchi])
pavimento_level4=T(3)(10.25)(PROD([pavimento_level4,Q(0.3)]))

#**pavimenti superiori e finale**
pavimento_3up=STRUCT(NN(4)([pavimento_level3,T(3)(6)]))
pavimento_4up=STRUCT(NN(3)([pavimento_level4,T(3)(6)]))

lines = lines2lines("pavimento_level3.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
#prova=STRUCT(MKPOLS((V,FV))) #grafo pulito
#VIEW(prova)

VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))
#V[21] da portare nell'origine a grandezza mondo: 42metri
assert V[21]==[0.0, 0.5928]
scala = 41.9
W=((mat(V)-V[21])*scala).tolist()
#**celle vuote**
#celle vuote sono 2,5,6,9,8
buchi = STRUCT(MKPOLS([W,[FV[k] for k in [2,5,6,9,8]]]))
tot = STRUCT(MKPOLS([W,FV]))
top= DIFFERENCE([tot,buchi])
top1=T(3)(28.25)(PROD([top,Q(0.3)]))
top2=T(3)(31.25)(PROD([top,Q(0.3)]))
PAVIMENTI_UFF=COLOR(RED)(STRUCT([pavimento_3up,pavimento_level2,pavimento_4up,top1,top2]))

#VIEW(pavimento_level4up)
VIEW(STRUCT([EDF_UFF,PAVIMENTI_UFF]))

#**MURO CIRCOLARE**

lines = lines2lines("murocircolare.lines") 
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#lo spigolo EV[60] deve misurare (misura presa dal pavimento livello 2) W[12][0]-W[4][0]==7.366019999999999, traslazione Z[4]

scaling=7.366019999999999
W=((mat(V)-V[64])*scaling).tolist()
W=(mat(W)+Z[4]).tolist()
WW = AA(LIST)(range(len(W)))
submodel = STRUCT(MKPOLS((W,EV)))
#VIEW(larModelNumbering(1,1,1)(W,[WW,EV],submodel,0.2))


EV_no=[60]
EV_si= set(range(len(EV))).difference(EV_no)
muro_circ=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_si]))

muro_circ=OFFSET([0.3,0.3])(muro_circ)
muro_circ=T(3)(1)(PROD([muro_circ,Q(33)]))
VIEW(STRUCT([EDF_UFF,PAVIMENTI_UFF,muro_circ]))
Pav_UFF=T([1,2])([0.1,0.2])(S(2)(0.99)(PAVIMENTI_UFF))

#BUCHI e DETTAGLI
taglio = CUBOID([2,1,33])
taglio=T([1,2,3])([-1,-.5,1.5])(taglio)
taglio=T(1)(21.2)(taglio)
#EDF_UFF1=DIFFERENCE([EDF_UFF,taglio])
#VIEW(STRUCT([EDF_UFF1,PAVIMENTI_UFF,muro_circ]))

#larghezza colonna W[10][0]-W[1][0] Out[376]: 9.674709999999997
#distanza dei rettangoli da inizio è di 0.8
rett = CUBOID([8,1,12.5])
rett=T([1,2,3])([33.4,-0.5,2.25])(rett)
#EDF_UFF2=DIFFERENCE([EDF_UFF1,rett])
#VIEW(STRUCT([EDF_UFF2,PAVIMENTI_UFF,muro_circ]))

rett1 = CUBOID([8,1,12.5])
rett1=T([1,2,3])([0.8,-0.5,2.25])(rett1)
#EDF_UFF3=DIFFERENCE([EDF_UFF2,rett1])
#VIEW(STRUCT([EDF_UFF3,PAVIMENTI_UFF,muro_circ]))

#triangoli
V=[[-1,0],[1,0],[0,1]]
FV=[[0,1,2]]
triangle=STRUCT(MKPOLS((V,FV)))
triangle=S([1,2])([4,13.5])(triangle)
triangle=PROD([triangle,INTERVALS(1)(1)])
#VIEW(triangle)
#cambio di coordinate con lo scambio e poi buco  
Q,FQ,EQ=UKPOL(triangle)
Q = AA(CONS([S1,S3,S2]))(Q)
tr_buco=STRUCT([MKPOL((Q,FQ,EQ))])
#altezza 16.5
tr_buco=T([1,2,3])([37.4,-0.5,18])(tr_buco)
#EDF_UFF4=DIFFERENCE([EDF_UFF3,tr_buco])
#VIEW(STRUCT([EDF_UFF4,PAVIMENTI_UFF,muro_circ]))
#secondo
V=[[-1,0],[1,0],[0,1]]
FV=[[0,1,2]]
triangle=STRUCT(MKPOLS((V,FV)))
triangle=S([1,2])([4,13.5])(triangle)
triangle=PROD([triangle,INTERVALS(1)(1)])
#VIEW(triangle)
#cambio di coordinate con lo scambio e poi buco  
V,FV,EV=UKPOL(triangle)
V = AA(CONS([S1,S3,S2]))(V)
tr_buco1=STRUCT([MKPOL((V,FV,EV))])
#altezza 16.5
tr_buco1=COLOR(RED)(T([1,2,3])([4.8,-0.5,18])(tr_buco1))
#EDF_UFF5=DIFFERENCE([EDF_UFF4,tr_buco1])
#VIEW(STRUCT([EDF_UFF5,PAVIMENTI_UFF,muro_circ]))

#cerchi
buco_circ= CYLINDER([4,3])(100)
#VIEW(buco_circ)
#12 altezza, 5.3 
buco=R([1,3])(PI/2)(buco_circ)
circ=T([1,2,3])([0.5,4.8,16.5])(buco)
#VIEW(STRUCT([circ,EDF_UFF5]))
#12 altezza, 5.3 
circ2=T(1)(42)(circ)

BUCHI=COLOR(RED)(STRUCT([taglio,rett,rett1,tr_buco,tr_buco1,circ,circ2]))
EDF_UFFfinal=DIFFERENCE([EDF_UFF,BUCHI])
VIEW(STRUCT([EDF_UFFfinal,Pav_UFF,muro_circ]))


