"EDIFICIO MENSA"
from larlib import *
#MURI
lines = lines2lines("mensa_level2.lines")
#grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[128][1]-V[127][1]: 0.8166
scala = 31.42/0.8166

W=((mat(V)-V[11])*scala).tolist()

#muri si e no
EV_NO=sorted([167,133,71,94,116,14,62,126,99,55,103,46,144,75,121,15,4,162,104,148,114,109,95,41,9,66,125,64,113,7,52,6,119])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_2=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_2=OFFSET([0.3,0.3])(muri_2)
wall_2=PROD([muri_2,Q(31.5)])
#VIEW(wall_2)

#LEVEL9
lines = lines2lines("mensa_level9.lines")
#grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[84][1]-V[85][1]: 0.8166
scala = 31.42/0.8166

W=((mat(V)-V[134])*scala).tolist()

pil=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in [6,95,23,42]]))
pil=OFFSET([0.3,0.3])(pil)
pilastri=T(3)(25.5)(PROD([pil,Q(0.3)]))

EV_NOfinale=sorted([1,108,74,149,34,53,49,63,15,16,154,0,81,80,161,51,123,10,25,105,129,68,42,23,95,6,51,66,46,158])
EV_SIfinale= set(range(len(EV))).difference(EV_NOfinale)
muri_finale=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SIfinale]))
muri_finale=OFFSET([0.3,0.3])(muri_finale)
wall_finale0=T(3)(31.5)(PROD([muri_finale,Q(2.5)]))
wall_finale=STRUCT([wall_finale0,pilastri])

#FINALE
lines = lines2lines("mensa_finale.lines")
#grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[101][1]-V[33][1]: 0.8166
scala = 31.42/0.8166

W=((mat(V)-V[36])*scala).tolist()

#muri si e no
EV_SI= sorted([6,100,21,94,30,78])
muri_11=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_11=OFFSET([0.3,0.3])(muri_11)
wall_11=T(3)(31.5)(PROD([muri_11,Q(2.5)]))
muri=STRUCT([wall_2,wall_11,wall_finale])
#VIEW(muri)


"""BUCHI"""
lines = lines2lines("facciata_mensa.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
grafo=STRUCT(MKPOLS((V,EV))) #grafo pulito
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))
scala = 31.72/0.9159

W=(mat(V)*scala).tolist()
FV_SI=[10,11,8,9,6,5]
buchi = STRUCT(MKPOLS([W,[FV[k] for k in FV_SI]]))
buchiPROD=R([2,3])(PI/2)(PROD([buchi,Q(2)]))
parete=T([1,3])([16.3,0.5])(R([1,2])(PI/2)(buchiPROD))
muro=T(1)(16.964337496938526)(CUBOID([0.3,31.42,31.5]))
facciata=DIFFERENCE([muro,parete])
chiusura=T([1,2])([-8.93426891991183, 4.971178055351459])(CUBOID([0.3,21.24,31.5]))

#PAVIMENTI 

lines = lines2lines("mensa_pavimento.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((Y,FV))) #grafo pulito
#VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
#VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))
#Y[35][1]-Y[64][1]==-0.948

scala = 38.4766103355376/0.948
Z=((mat(Y)-Y[86])*scala).tolist()
#Z[22]=[0.0, 2.6818197403869712]

"top"
buchi = STRUCT(MKPOLS([Z,[FV[16]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_top= DIFFERENCE([tot,buchi])
top=T(3)(31.25)(PROD([frame_top,Q(0.3)]))


"FINESTRE"

#EV[167]=(91, 138)
#W[91][1]-W[138][1]=3.6706686260102863
#EV[133]= (10, 11)
#W[10][1]-W[11][1]= -3.3859417095273088
trave_base=CUBOID([0.3,3.6,1.55])
trave_top=T(3)(30.5)(CUBOID([0.3,3.6,3.55]))
trave=T(3)(3.5)(CUBOID([0.3,3.6,1.05]))
travi=STRUCT(NN(9)([trave,T(3)(3.05)]))
bordo=SKEL_1(CUBOID([2,3.6]))
seg=T(2)(1.2)(INTERVALS(2)(1))
seg1=STRUCT(NN(2)([seg,T(2)(1.2)]))
seg2=T(1)(0.7)(R([1,2])(PI/2)(INTERVALS(3.6)(1)))
grid_fin=OFFSET([0.05,0.05])(STRUCT([bordo,seg1,seg2]))
fin_lat=T([1,3])([0.15,1.55])(R([1,3])(PI/2)(PROD([grid_fin,Q(0.05)])))
fin_laterali=STRUCT(NN(10)([fin_lat,T(3)(3.05)]))
LAT_sx=T(2)(-3.3)(STRUCT([trave_top,travi,trave_base]))
LAT_dx=T(2)(35.02)(LAT_sx)

fin_sx=T(2)(-3.3)(fin_laterali)
fin_dx=T(2)(35.02)(fin_sx)
GRATE=STRUCT([fin_sx,fin_dx])

"FESSURE"
frame0=SKEL_1(PROD([Hpc(Grid([2*[3.8/2]])),Hpc(Grid([35*[31./35]]))]))
frame1=T(2)(-1.5)(CUBOID([3.8,1.5]))
frame2=T(2)(31)(CUBOID([3.8,1.5]))
mur=STRUCT([frame1,frame2])
gridOFF=OFFSET([0.05,0.05])(frame0)
grid_fess=T(3)(0.15)(PROD([gridOFF,Q(0.05)]))
muretti=COLOR([0.6,0.6,0.6])(PROD([mur,Q(0.3)]))
FESSURE0=R([2,3])(PI/2)(T(2)(1.5)(STRUCT([muretti,grid_fess])))
FESS1=T([1])([-6.7])(R([1,2])(-3*PI/4)(FESSURE0))
FESS2=T([1,2])([-7.1,31.2])(R([1,2])(3*PI/4)(FESSURE0))
FESSURE=STRUCT([FESS1,FESS2])

#VIEW(LAT)
#VIEW(STRUCT([LAT_dx,LAT_sx,muri,facciata,top,chiusura]))

MURI=STRUCT([LAT_dx,LAT_sx,muri,facciata,chiusura])

MENSA=STRUCT([COLOR([0.6,0.6,0.6])(MURI),top,GRATE,FESSURE])
VIEW(MENSA)

EST=T([1,2])([109, -0.5629329794293257])(MENSA)


