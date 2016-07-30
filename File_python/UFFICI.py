"UFFICI"
from larlib import *

"LEVEL 1_muri esterni" 

lines = lines2lines("rialzo_level1.lines")
V,FV,EV,polygons = larFromLines(lines) 

grafo=STRUCT(MKPOLS((V,EV))) 
EV[9]=[4,0]

VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))

#V[6] da portare nell'origine, spigolo EV[7] da portare a grandezza mondo: 42metri
#assert V[6]==[0.0051, 0.5948]
#assert V[3]==[0.0051, 1.0]
#assert V[9]==[1.0, 1.0]
#assert V[9][0]-V[3][0] == 0.9949 #la grandezza massima non è precisa a 1
scala = 41.9/0.9949

W=((mat(V)-V[6])*scala).tolist()
#mura esterne piu basse
EV_bassi=sorted([13,14,2,4,6,5,3,10,12,0])
EV_alti= set(range(len(EV))).difference(EV_bassi)
muri = STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_alti]))


#VIEW(OFFSET([0.3,0.3])(base)) #Muri spessi 30 cm circa
muri=OFFSET([0.3,0.3])(muri)
wall_1=PROD([muri,Q(34)])
#VIEW(level1)
EV_5= STRUCT(MKPOLS((W,[EV[5]])))
muro5=OFFSET([0.3,0.3])(EV_5)
wall_5=PROD([muro5,Q(34)])
EV_3= STRUCT(MKPOLS((W,[EV[3]])))
muro3=OFFSET([0.3,0.3])(EV_3)
wall_3=PROD([muro3,Q(34)])
EV_10= STRUCT(MKPOLS((W,[EV[10]])))
muro10=OFFSET([0.3,0.3])(EV_10)
wall_10=PROD([muro10,Q(34)])
EV_12= STRUCT(MKPOLS((W,[EV[12]])))
muro12=OFFSET([0.3,0.3])(EV_12)
wall_12=PROD([muro12,Q(34)])
EV_0= STRUCT(MKPOLS((W,[EV[0]])))
muro0=OFFSET([0.3,0.3])(EV_0)
wall_0=PROD([muro0,Q(34)])

#ESTERNO=STRUCT([wall_1,wall_5,wall_3,wall_10,wall_12,wall_0])
#VIEW(STRUCT([wall_1,wall_5,wall_3,wall_10,wall_12,wall_0]))


"COLONNE"
lines = lines2lines("colonne.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
grafo=STRUCT(MKPOLS((V,EV))) #grafo pulito
#VIEW(OFFSET([0.005,0.005])(grafo))

VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))

#V[2] da portare nell'origine, spigolo EV[9] da portare a grandezza mondo: 42metri
#assert V[2]==[0.0051, 0.5948]
#assert V[5][0]-V[1][0] == 0.9949 

scala = 41.9/0.9949

W=((mat(V)-V[2])*scala).tolist()

EV_si= [12,13,14,15,18,16,17,19]

#**verifica** 
#WW = AA(LIST)(range(len(W)))
#VIEW(larModelNumbering(1,1,1)(W,[WW,EV,FV],STRUCT(MKPOLS((W,EV))),2))
#assert W[7][0]-W[3][0]==41.9


baseC=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_si]))
baseC=OFFSET([0.3,0.3])(baseC)

colonne=PROD([baseC,Q(29.5)]) #34-4.5
colonne=T(3)(4.5)(colonne)
#VIEW(colonne)


#VIEW(level_4)
#VIEW(level_4up)

EDF_UFF=STRUCT([wall_1,colonne])
#VIEW(EDF_UFF)

"PAVIMENTI"


lines = lines2lines("pavimento_level3.lines")
V,FV,EV,polygons = larFromLines(lines)

#VV = AA(LIST)(range(len(V)))
#submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))
#V[21] da portare nell'origine a grandezza mondo: 42metri
#assert V[21]==[0.0, 0.5928]
scala = 41.9
W=((mat(V)-V[21])*scala).tolist()
#celle vuote sono 2,5,6,9,8
buchi = STRUCT(MKPOLS([W,[FV[k] for k in [2,5,6,9,8]]]))
tot = STRUCT(MKPOLS([W,FV]))
top= DIFFERENCE([tot,buchi])
top2=T(3)(31.25)(PROD([top,Q(0.3)]))
Pav_UFF=T([1,2])([0.1,0.2])(S(2)(0.99)(top2))

"MURO CIRCOLARE"

lines = lines2lines("murocircolare.lines") 
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
"""
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))
"""
#lo spigolo EV[60] deve misurare (misura presa dal pavimento livello 2) W[12][0]-W[4][0]==7.366019999999999

scaling=7.366019999999999
W=((mat(V)-V[64])*scaling).tolist()
W=(mat(W)+[17.26699, 0.0]).tolist()
#WW = AA(LIST)(range(len(W)))
#submodel = STRUCT(MKPOLS((W,EV)))
#VIEW(larModelNumbering(1,1,1)(W,[WW,EV],submodel,0.2))


EV_no=[60]
EV_si= set(range(len(EV))).difference(EV_no)
muro_circ=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_si]))

muro_circ=OFFSET([0.3,0.3])(muro_circ)
muro_circ=T([2,3])([0.1,1])(PROD([muro_circ,Q(33)]))
#VIEW(STRUCT([EDF_UFF,PAVIMENTI_UFF,muro_circ]))


#BUCHI e DETTAGLI
taglio = CUBOID([2,1,33])
taglio=T([1,2,3])([-1,-.5,1.5])(taglio)
taglio=T(1)(21.2)(taglio)
MURO_front=DIFFERENCE([wall_0,taglio])

rett = CUBOID([8,1,12.5])
rett=T([1,2,3])([33.4,-0.3,2.25])(rett)

rett1 = CUBOID([8,1,12.5])
rett1=T([1,2,3])([0.8,-0.3,2.25])(rett1)

#triangoli
V=[[-1,0],[1,0],[0,1]]
FV=[[0,1,2]]
triangle=STRUCT(MKPOLS((V,FV)))
triangle=S([1,2])([4,13.5])(triangle)
triangle=PROD([triangle,INTERVALS(1)(1)])
#VIEW(triangle)
#cambio di coordinate con lo scambio e poi buco  
X,FX,EX=UKPOL(triangle)
X = AA(CONS([S1,S3,S2]))(X)
tr_buco=STRUCT([MKPOL((X,FX,EX))])
tr_buco=T([1,2,3])([37.4,-0.3,18])(tr_buco)

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
tr_buco1=COLOR(RED)(T([1,2,3])([4.8,-0.3,18])(tr_buco1))
TRBUCO=STRUCT([rett,rett1,tr_buco,tr_buco1])

MURI_FRONT=DIFFERENCE([STRUCT([wall_5,wall_10]),TRBUCO])


#cerchi
buco_circ= CYLINDER([4,3])(16)
#VIEW(buco_circ)
buco=R([1,3])(PI/2)(buco_circ)
circ=T([1,2,3])([1,4.8,16.5])(buco)
#VIEW(STRUCT([circ,EDF_UFF5]))
circ2=T(1)(42)(circ)
BUCO=STRUCT([circ,circ2])
MURI_LAT=DIFFERENCE([STRUCT([wall_3,wall_12]),BUCO])

#GRIGLIE
frame=S([1,2])([0.30,0.30])(SKEL_1(STRUCT(MKPOLS(larCuboids([32,32])))))
grid=OFFSET([0.03,0.03])(frame)
GRID=PROD([grid,INTERVALS(0.1)(1)])
frame2=S([1,2])([1.2,1.2])(SKEL_1(STRUCT(MKPOLS(larCuboids([8,8])))))
grid2=OFFSET([0.1,0.1])(frame2)
GRID2=PROD([grid2,INTERVALS(0.1)(1)])
GR=STRUCT([GRID2])
GRID_sx=T(3)(33.8)(GR)
GRID_dx=T(1)(32.4)(GRID_sx)

frame3=S([1,2])([0.41,0.41])(SKEL_1(STRUCT(MKPOLS(larCuboids([7,7])))))
grid3=OFFSET([0.1,0.1])(frame3)
GRID3=PROD([grid3,INTERVALS(0.1)(1)])
grcol_dx=T([1,2,3])([27.997909337621874, 10.928786812744997,33.8])(GRID3)
grcol_sx=T([1,2,3])([10.928786812744999, 10.928786812744997,33.8])(GRID3)
GRID_tot=T(2)(0.1)(STRUCT([GRID_dx,GRID_sx,grcol_dx,grcol_sx]))


MURI=STRUCT([wall_1,MURO_front,MURI_FRONT,MURI_LAT,colonne,muro_circ])
UFFICI=STRUCT([COLOR([0.6,0.6,0.6])(MURI),Pav_UFF,GRID_tot])
#VIEW(UFFICI)

EDIFICIO=T(2)(-17.064911046336317)(UFFICI)
VIEW(EDIFICIO)
UFF1=T([1,2])([4.8, -3])(R([1,2])(-PI/4)(EDIFICIO))
UFF2=T([1,2])([34.7, 62.8])(R([1,2])(5*PI/4)(EDIFICIO))
UFF3=T([1,2])([99.1, 33.4])(R([1,2])(3*PI/4)(EDIFICIO))
UFF4=T([1,2])([69.9, -32.96318075509524])(R([1,2])(PI/4)(EDIFICIO))

EDF_UFFICI=STRUCT([UFF1,UFF2,UFF3,UFF4])

