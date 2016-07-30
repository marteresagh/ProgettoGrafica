"EDIFICIO ALLOGGI"
from larlib import *
from scale import *

#LEVEL1
"""
lines = lines2lines("alloggi_level1.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV],submodel,0.2))

#V[99][0]-V[96][0]=0.5853
scala = 22.85/0.5853

W=(mat(V)*scala).tolist()
#muri si e no
EV_SI= [65,195,38]
muri_1=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_1=OFFSET([0.3,0.3])(muri_1)
wall_1=PROD([muri_1,Q(4.5)])
"""

a=T([1,2])([3.6814539552366305, 16.396719630958483])(CUBOID([0.3,5.89110712455151,4.5]))
b=T([1,2])([0.0019519904322569624, 16.396719630958483])(CUBOID([0.3,5.89110712455151,4.5]))
wall_1=STRUCT([a,b])

#LEVEL2

lines = lines2lines("alloggi_level2.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
"""
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))
"""
#V[9][0]-V[91][0]= 0.58525

scala = 22.85/0.58525

W=(mat(V)*scala).tolist()
"""
WW = AA(LIST)(range(len(W)))
submodel = STRUCT(MKPOLS((W,EV)))
mappa=larModelNumbering(1,1,1)(W,[WW,EV],submodel,1)
"""
#modifica degli spigoli
EV[127]=[32,18]
EV[91]=[79,133]
EV[27]=[115,129]

#muri da alzare
EV_SI= [119,16,65,37,62,91,44,148,114,128,124,78,147,27,137,86,34,96,127,53,14,74,88,97,45,145,130,40]
muri_2=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_2=OFFSET([0.3,0.3])(muri_2)
wall_2=PROD([muri_2,Q(34)])

EV_SI= [149,87]
lat=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
lat=OFFSET([0.3,0.3])(lat)
lat=PROD([lat,Q(34)])

EV_NO=sorted([114,78,145,34,27,147,119,16,137,86,37,62,65,130,40,14,96,74,45,14,97,53,88,127,118,149,87,124,35,128,148,27,124,90,44,91,69,56,35,2,136,13,118])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_tondi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_tondi=OFFSET([0.3,0.3])(muri_tondi)
wall_tondi=PROD([muri_tondi,Q(34)])

#VIEW(STRUCT([wall_tondi,lat,wall_2,wall_1]))

#LEVEL5/7
lines = lines2lines("alloggi_level5_7.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
"""
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.1))
"""
#scala: V[19][0]-V[24][0]=0.5852833333333334

scala = 22.85/0.5852833333333334

W=(mat(V)*scala).tolist()

#muri da alzare

EV_SI= [147,69,36,46,21,6,85,152]
muri_5=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_5=OFFSET([0.3,0.3])(muri_5)
wall_5=T(3)(13.5)(PROD([muri_5,Q(11)]))
#VIEW(STRUCT([wall_tondi,lat,wall_2,wall_1,wall_5]))


#LEVEL FINALE
lines = lines2lines("alloggi_finale.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
"""
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))
"""
#V[141][0]-V[77][0]=0.58525

scala = 22.85/0.58525

W=(mat(V)*scala).tolist()

#muri si e no
EV_SI= [139,94]
muri_finale=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_finale=OFFSET([0.3,0.3])(muri_finale)
wall_finale=T(3)(25.5)(PROD([muri_finale,Q(8.5)]))
#VIEW(STRUCT([wall_tondi,lat,wall_2,wall_1,wall_5,wall_finale]))

"""buchi"""
#TRIANGOLI LATERALI
V=[[-1,0],[1,0],[0,1]]
FV=[[0,1,2]]
triangle=STRUCT(MKPOLS((V,FV)))
triangle1=S([1,2])([7.5,10.5])(triangle)
triangle1=PROD([triangle1,Q(3.5)])
#VIEW(triangle)
#cambio di coordinate con lo scambio e poi buco  
X,FX,EX=UKPOL(triangle1)
X = AA(CONS([S1,S3,S2]))(X)
tr_buco=STRUCT([MKPOL((X,FX,EX))])
tr_buco1=T([1,2,3])([11.6,-0.4,14])(tr_buco)
tr_buco2=T([1,2,3])([11.6,35.9,14])(tr_buco)

tondi=DIFFERENCE([wall_tondi,STRUCT([tr_buco1,tr_buco2])])

#FINESTRE TRIANGOLARI
triangle2=S([1,2])([6,3])(triangle)
triangle2=PROD([triangle2,Q(1.5)])
X,FX,EX=UKPOL(triangle2)
X = AA(CONS([S1,S3,S2]))(X)
tr_fin=STRUCT([MKPOL((X,FX,EX))])
tr_fin1=T([1,2,3])([10.9,14.3,14.6])(tr_fin)
tr_fin2=T([1,2,3])([10.9,23.5,14.6])(tr_fin)
tr_fin3=T([1,2,3])([10.9,14.3,20.6])(tr_fin)
tr_fin4=T([1,2,3])([10.9,23.5,20.6])(tr_fin)
TR_FIN=STRUCT([tr_fin1,tr_fin2,tr_fin3,tr_fin4])
#FINESTRE RETTANGOLARI
fin1=T([1,2,3])([6,14.3,4.6])(CUBOID([10,1.5,2.6]))
fin2=T([1,2,3])([6,14.3,9.3])(CUBOID([10,1.5,3]))
fin3=T([1,2,3])([6,23.5,4.6])(CUBOID([10,1.5,2.6]))
fin4=T([1,2,3])([6,23.5,9.3])(CUBOID([10,1.5,3]))
FIN=STRUCT([fin1,fin2,fin3,fin4])

BUCHI=STRUCT([TR_FIN,FIN])
#VIEW(STRUCT([BUCHI,lat]))
muri_fin=DIFFERENCE([lat,BUCHI])
muri=STRUCT([wall_1,muri_fin,tondi,wall_2,wall_finale])

#VIEW(muri)

"""PAVIMENTI"""
#pavimento level1
lines = lines2lines("alloggi_pavimento.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((Y,FV))) #grafo pulito
#VIEW(prova)
"""
YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
VIEW(larModelNumbering(1,1,1)(Y,[YY,FV],submodel,0.1))
"""
#Y[99][0]-Y[83][0]=0.5817

scala = 22.85/0.5817
Z=(mat(Y)*scala).tolist()

#pavimento level2
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [14,7,3,2,6,4,5,8,18,13]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level2= DIFFERENCE([tot,buchi])
pavimento_level2=T([1,3])([-0.6,4.2])(PROD([frame_level2,Q(0.3)]))

#pavimento level3
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [7,3,19,2,6,4,5,8,18,13,20,14,17]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level2= DIFFERENCE([tot,buchi])
pavimento_level3=T([1,3])([-0.6,7.2])(PROD([frame_level2,Q(0.3)]))
pavimenti3_5=STRUCT(NN(2)([pavimento_level3,T(3)(6)]))
#top
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [7,3,19,2,6,4,5,8,18,13,20,17,14]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level11= DIFFERENCE([tot,buchi])
top=T([1,3])([-0.6,31.5])(PROD([frame_level11,Q(0.3)]))

PAVIMENTI=STRUCT([pavimento_level2,pavimenti3_5,top])
#VIEW(STRUCT([muri,PAVIMENTI]))

""" finestre """

#W[128]: [19.705074754378472, 24.171610422896197]

#W[85]: [19.705074754378472, 14.836394703118327]

#W[85][1]-W[128][1]: -9.335215719777871


#MURO CENTRALE con finestre
trave=CUBOID([0.3,5.3,1])
FRAME1=STRUCT([trave])
FRAME2=T(3)(6)(STRUCT([trave]))
TRAVE=T(3)(12)(trave)
wall=CUBOID([0.3,5.3,8.2])
buco_fin=T([1,2,3])([-0.4,1.2,1])(CUBOID([1,3,3]))
wall_fin0=DIFFERENCE([wall,buco_fin])
#grid_small=SKEL_1(PROD([Hpc(Grid([2*[1.5]])),Hpc(Grid([2*[1.5]]))]))
#gridOFF_small=OFFSET([0.05,0.05])(grid_small)
#fin_small=T([1,2,3])([0.15,1,1])(R([1,3])(PI/2)(PROD([gridOFF_small,Q(0.05)])))
wall_fin=T(3)(13)(STRUCT([wall_fin0]))
laterale_dx=T([2,3])([-1.8,-8.3])(CUBOID([0.3,1.8,29.5]))
laterale_sx=T([2,3])([5.3,-8.3])(CUBOID([0.3,2,29.5]))
FRAME0=T([1,2,3])([19.705074754378472, 14.836394703118327+2,12.8])(STRUCT([wall_fin,FRAME1,FRAME2,TRAVE,laterale_dx,laterale_sx]))
#VIEW(STRUCT([PAVIMENTI,MURI_ALLOGGI,FRAME0]))

#griglia finestre
grid=SKEL_1(PROD([Hpc(Grid([3*[5.3/3]])),Hpc(Grid([3*[5.3/3]]))]))
gridOFF=OFFSET([0.05,0.05])(grid)
fin=T([1,2,3])([0.15,-0.02,1])(R([1,3])(PI/2)(PROD([gridOFF,Q(0.05)])))
FRAME1=STRUCT([fin])
FRAME2=T(3)(6)(STRUCT([fin]))
grid_small=SKEL_1(STRUCT(MKPOLS(larCuboids([3,3]))))
gridOFF_small=OFFSET([0.05,0.05])(grid_small)
fin_small=T([1,2,3])([0.15,1.2,1])(R([1,3])(PI/2)(PROD([gridOFF_small,Q(0.05)])))
wall_fin=T(3)(13)(STRUCT([fin_small]))
FRAME_FIN=T([1,2,3])([19.705074754378472, 14.836394703118327+2,12.8])(STRUCT([wall_fin,FRAME1,FRAME2]))
#VIEW(STRUCT([FRAME0,FRAME_FIN]))

#griglie finestre pareti laterali
grid_rett=SKEL_1(PROD([ Hpc(Grid([5*[10./5]])), Hpc(Grid([2*[3./2]]))]))
gridOFF_rett=OFFSET([0.05,0.05])(grid_rett)
fin_rett1=T([1,2,3])([6,15,4.6])(R([2,3])(PI/2)(PROD([gridOFF_rett,Q(0.05)])))
fin_rett2=T([3])([4.7])(fin_rett1)
fin_rett3=T([2])([9.3])(fin_rett1)
fin_rett4=T([2,3])([9.3,4.7])(fin_rett1)
FIN_RETT=STRUCT([fin_rett1,fin_rett2,fin_rett3,fin_rett4])

grid_tr=SKEL_1(PROD([ Hpc(Grid([6*[12./6]])), Hpc(Grid([3*[1]]))]))
gridOFF_tr=OFFSET([0.05,0.05])(grid_tr)
fin_tr1=T([1,2,3])([6,15,14.6])(R([2,3])(PI/2)(PROD([gridOFF_tr,Q(0.05)])))
fin_tr2=T([3])([6])(fin_tr1)
fin_tr3=T([2])([9.3])(fin_tr1)
fin_tr4=T([2,3])([9.3,6])(fin_tr1)
FIN_TR=STRUCT([fin_tr1,fin_tr2,fin_tr3,fin_tr4])
#VIEW(STRUCT([MURI,FIN_TR,FIN_RETT]))

"""SCALA"""
scala=T([1,2,3])([20, 16.836394703118327,7.35])(S(1)(-1)(createFilledSteps(20,[0.28,5.3,0.15],rail=True,spessore=0.3,altezza=1.5)))

MURI=STRUCT([muri,FRAME0,wall_5])
GRATE=STRUCT([FRAME_FIN,FIN_RETT,FIN_TR])
VIEW(STRUCT([T(1)(-0.1)(PAVIMENTI),COLOR([0.6,0.6,0.6])(MURI),GRATE,scala]))

EDF_ALLOGGI=STRUCT([T(1)(-0.1)(PAVIMENTI),COLOR([0.6,0.6,0.6])(MURI),GRATE,scala])
OVEST=T([1,2])([-24.5,-5])(EDF_ALLOGGI)

