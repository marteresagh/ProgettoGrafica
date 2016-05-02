#SALA DELLA PREGHIERA
#dimensioni 20.95 per lato e 34 di altezza, 7.61 il raggio delle colonne, offset delle pareti a 0.3
from larlib import *

base= CUBOID([20.5,20.5])
rialzo=PROD([base,Q(1.5)])
muri=OFFSET([0.3,0.3])(SKEL_1(base))
pareti=PROD([muri,Q(34)])
pav_sala=T([1,2,3])([0.3,0.3,13.5])(CUBOID([20.5,20.5,0.5]))
pav_sala1=T([1,2,3])([0.3,0.3,7.5])(CUBOID([20.5,20.5,0.5]))
soffitto=T([1,2,3])([0.3,0.3,33.5])(CUBOID([20.2,20.2,0.5]))
SALA=STRUCT([rialzo,pareti,soffitto,pav_sala,pav_sala1])

#COLONNE PIANO TERRA
lines = lines2lines("sala_terra.lines") 
grafo = STRUCT(AA(POLYLINE)(lines))
V,EV = lines2lar(lines)
scaling=14.95
W=(mat(V)*scaling).tolist()
grafo1=STRUCT(MKPOLS((W,EV)))
arco=OFFSET([0.3,0.3])(grafo1)
ARCHI=T([1,2])([2.87,2.87])(PROD([arco,Q(13.5)]))
#VIEW(STRUCT([ARCHI]))

#VIEW(SALA)
#a 6*1.5 metri c'è l'ingresso principale, ovvero al terzo piano, al primo c' è il passaggio inferiore al livello 5 ovvero a 1.5+3*4

#BUCHI TONDI
buco_ell= S(1)(0.53)(CYLINDER([7,1.5])(100))
buco=R([1,3])(PI/2)(buco_ell)
circ=COLOR(RED)(T([1,3])([0.8,28])(buco))
buco1=R([1,2])(PI/2)(R([1,3])(PI/2)(buco_ell))
circ1=COLOR(RED)(T([2,3])([0.8,28])(buco1))

#VIEW(STRUCT([circ1,circ]))

frame=R([1,2])(-PI/2)(STRUCT(MKPOLS(larDisk(7,PI)([100,1]))))
buco_circ= S(1)(0.85)(PROD([frame,Q(1.5)])) 
buco2=R([1,3])(PI/2)(buco_circ)
circ2=COLOR(RED)(T([1,3])([.8,14.5])(buco2))
buco3=R([1,2])(PI/2)(R([1,3])(PI/2)(buco_circ))
circ3=COLOR(RED)(T([2,3])([.8,14.5])(buco3))
#VIEW(STRUCT([circ3,circ2]))

#DA CAMBIARE CIRC SUD!!!!!!!!!!!!!!!!!!!!!!
circ_sud=COLOR(RED)(T([1,2,3])([.8,.8,13.3])(S([3])(-0.75)(T([1,2,3])([-.8,-.8,-14.5])(STRUCT([circ2,circ3])))))

#CILINDRI
base1=STRUCT(MKPOLS(larDisk(7.61,3./2*PI)([100,1])))
base2=STRUCT(MKPOLS(larDisk(7.31,3./2*PI)([100,1])))
cil1=PROD([base1,Q(34)])
cil2=T(3)(-1)(PROD([base2,Q(37)]))
cil_vuoto=DIFFERENCE([cil1,cil2])
#VIEW(cil_vuoto)

#dettagli MARMO
base01=STRUCT(MKPOLS(larDisk(7.76,3./2*PI)([100,1])))
base02=STRUCT(MKPOLS(larDisk(7.16,3./2*PI)([100,1])))
cil01=PROD([base01,Q(0.2)])
cil02=T(3)(-.5)(PROD([base02,Q(1)]))
r_circ=DIFFERENCE([cil01,cil02])
MARMOcirc=T(3)(1.4)(r_circ)
rip_MARMOcirc=STRUCT(NN(11)([MARMOcirc,T(3)(3)]))

#FINESTRE

grid=SKEL_1(STRUCT(MKPOLS(larCuboids([5,1]))))
grid2=T([1,2])([.5,1])(SKEL_1(STRUCT(MKPOLS(larCuboids([4,1])))))
grid_rip=STRUCT(NN(2)([(STRUCT([grid,grid2])),T(2)(2)]+[grid]))
#VIEW(grid_rip)
bordo=SKEL_1(CUBOID([5,5]))
#VIEW(STRUCT([bordo,grid_rip]))
seg=T([1])(.5)(R([1,2])(-PI/2)(INTERVALS(2)(1)))
grata1=STRUCT(NN(4)([seg,T(1)(1)]))
grata2=T(2)(7)(grata1)
seg2=T([1,2])([5,1.5])(INTERVALS(2)(1))
grata3=STRUCT(NN(3)([seg2,T(2)(1)]))
grata=STRUCT([bordo,grid_rip,grata1,grata2,grata3])
griglia1=OFFSET([0.05,0.05])(grata)
griglia=PROD([griglia1,Q(0.05)])
finestra1=T([1,2,3])([0.1,0.2,25.5])(R([2,3])(PI/2)(griglia))
finestra2=T([1,2])([.3,0.1])(R([1,2])(PI/2)(finestra1))
#VIEW(griglia)
#VIEW(STRUCT([COLOR(RED)(finestra2),COLOR(RED)(finestra1)]))


#FINESTRE SUD
grid_sud=SKEL_1(STRUCT(MKPOLS(larCuboids([5,1]))))
grid2_sud=T([1,2])([.5,1])(SKEL_1(STRUCT(MKPOLS(larCuboids([4,1])))))
grid3_sud=T(2)(2)(grid_sud)
gridsud=STRUCT([grid_sud,grid2_sud,grid3_sud])
bordo1=SKEL_1(CUBOID([5,3]))
wind1=T(2)(-1.5)(SKEL_1(STRUCT(NN(9)([CUBOID([1,1.5]),T(1)(0.5)]))))
quad=SKEL_1(T([2])(3)(CUBOID([0.5,1])))
quad1=SKEL_1(T([1,2])([.5,3])(STRUCT(NN(2)([CUBOID([1.5,1]),T(1)(1.5)]))))
seg3=T([1,2])([.5,4])(R([1,2])(PI/2)(INTERVALS(2)(1)))
rip_seg3=STRUCT(NN(3)([seg3,T(1)(1.5)]))
seg4=T([1])([5])(INTERVALS(2)(1))
rip_seg4=STRUCT(NN(2)([seg4,T(2)(1.5)]))
grata2=STRUCT([wind1,gridsud,bordo1,rip_seg3,rip_seg4,quad,quad1])
griglia2=OFFSET([0.05,0.05])(grata2)
griglia_sud=PROD([griglia2,Q(0.05)])
finestra1_sud=T([1,2,3])([0.1,0.2,15.5])(R([2,3])(PI/2)(griglia_sud))
finestra2_sud=T([1,2])([.3,0.1])(R([1,2])(PI/2)(finestra1_sud))
fin_SUD=T(3)(14.5)(S(3)(0.88)(T(3)(-14)(STRUCT([finestra1_sud,finestra2_sud]))))

#DA CAMBIARE LE FINESTRE SOTTO
FIN_SOTTO=T(3)(13.3)(S(3)(-.75)(S(3)(0.88)(T(3)(-14)(STRUCT([finestra1_sud,finestra2_sud])))))
#VIEW(STRUCT([fin_SUD,SALA_PREG]))
#trasformazioni finestre
GRATE=STRUCT([FIN_SOTTO,fin_SUD,finestra1,finestra2])
fin2=T(1)(20.8)(R([1,2])(PI/2)(GRATE))
fin3=T([1,2])([20.8,20.8])(R([1,2])(PI)(GRATE))
fin4=T(2)(20.8)(R([1,2])(-PI/2)(GRATE))
FINESTRE=STRUCT([GRATE,fin2,fin3,fin4])
#FINE FINESTRE

#PILASTRI E MARMO

pil_x=T(2)(-0.3)(CUBOID([-7.61,0.3,34]))
pil_y=CUBOID([0.3,7.61,34])

righe_x=T(2)(-0.15)(T(2)(-0.3)(CUBOID([-7.61,0.60,0.2])))
righe_y=T(1)(-.15)(CUBOID([0.60,7.61,0.2]))
rig=STRUCT([righe_x,righe_y])
MARMOrig=T(3)(1.4)(rig)
rip_MARMOrig=STRUCT(NN(11)([MARMOrig,T(3)(3)]))

pilastro=STRUCT([cil_vuoto,pil_x,pil_y,rip_MARMOcirc,rip_MARMOrig])
BUCHI=STRUCT([circ,circ1,circ2,circ3,circ_sud])
tagli=R([1,2])(PI/2)(BUCHI)
tagli2=T(1)(20.8)(R([1,2])(PI/2)(tagli))
tagli3=T([1,2])([20.8,20.8])(R([1,2])(PI)(tagli))
tagli4=T(2)(20.8)(R([1,2])(-PI/2)(tagli))
FORI=STRUCT([tagli,tagli2,tagli3,tagli4])
croce1=R([1,2])(PI/2)(pilastro)
croce2=T(1)(20.8)(R([1,2])(PI/2)(croce1))
croce3=T([1,2])([20.8,20.8])(R([1,2])(PI)(croce1))
croce4=T(2)(20.8)(R([1,2])(-PI/2)(croce1))

#dettagli MARMO
base0= CUBOID([20.8,20.8])
frame_righe=T([1,2])([-0.15,-0.15])(OFFSET([0.4,0.4])(SKEL_1(base0)))
righe=PROD([frame_righe,Q(0.2)])
MARMOrett=T(3)(1.4)(righe)
rip_MARMOrett=STRUCT(NN(11)([MARMOrett,T(3)(3)]))
#VIEW(rip_MARMOrett)
PREG=STRUCT([SALA,croce1,croce2,croce3,croce4,rip_MARMOrett])
#SALA_PREG=DIFFERENCE([PREG,FORI])


#ARCHI ANGOLATI
para=CUBOID([20,0.3,6.3])
semi_circ=STRUCT(MKPOLS(larDisk(9.6/2,PI)([100,1])))
shape=T([1,2,3])([10,0.5,-0.15])(R([2,3])(PI/2)(PROD([semi_circ,Q(1)])))
shapeTETTO=DIFFERENCE([para,shape])
shape1=T(1)(-5.2)(shapeTETTO)

#5.2
shapeR=R([1,2])(-PI/4)(R([2,3])(-PI/9)(shape1))
tetto=COLOR(RED)(T([1,2,3])([0.2,7,28])(shapeR))
cubo1=T([2,3])([-10,15])(CUBOID([20,10,20]))
cubo2=T([1,3])([-10,15])(CUBOID([10,20,20]))
eccesso=STRUCT([cubo1,cubo2])
tetto_finale1=DIFFERENCE([tetto,eccesso])
tetto_finale=T([1,2])([-4.8,-4.8])(tetto_finale1)
tetto_finale2=T([1,2])([16,16])(S([1,2])([-1,-1])(tetto_finale))
tetto_finale3=T([1,2])([16,4.8])(R([1,2])(PI/2)(tetto_finale))
tetto_finale4=T([1,2])([4.8,16])(S([1,2])([-1,-1])(R([1,2])(PI/2)(tetto_finale)))
TETTO=STRUCT([tetto_finale1,tetto_finale2,tetto_finale3,tetto_finale4])
SALA_PREGHIERA=STRUCT([ARCHI,TETTO,SALA_PREG,FINESTRE])
VIEW(SALA_PREGHIERA)

#MANCA SECONDO PIANO E COMPLETA CON LA CORTE 

#CORTE :CAMBIA I DISEGNI:PIU PRECISI 
#LEVEL1
lines = lines2lines("corte_level1.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[203] da portare nell'origine, spigolo V[29]V[97] da portare a grandezza mondo: 30.46metri
#assert V[203]==[0.0, 1.0]
#assert V[189]==[0.0414,1.0]
#assert V[71]==[0.9528,1.0]
#assert V[71][0]-V[189][0] == 0.9114
scala = 30.46/0.9114

W=((mat(V)-V[203])*scala).tolist()

#W[79][0]-W[168][0]
# 34.25165860789385


base=STRUCT(MKPOLS((W,EV)))
baseOFF=OFFSET([0.3,0.3])(base)
muri_level1=PROD([baseOFF,Q(4.5)])
VIEW(muri_level1)

#LEVEL2
lines = lines2lines("corte_level2.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[210] da portare nell'origine, spigolo da portare a grandezza mondo: 30.46metri
#assert V[210]==[0.0, 1.0]
#assert V[211]==[0.0406,0.9989]
#assert V[165]==[0.952,0.9989]
#assert V[165][0]-V[211][0] == 0.9114
scala = 30.46/0.9114

W=((mat(V)-V[210])*scala).tolist()

base2=STRUCT(MKPOLS((W,EV)))
baseOFF2=OFFSET([0.3,0.3])(base2)
muri_level2=T(3)(4.5)(PROD([baseOFF2,Q(3)]))
#VIEW(muri_level2)
VIEW(STRUCT([muri_level1,muri_level2]))

#LEVEL3
lines = lines2lines("corte_level3.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[168] da portare nell'origine, spigolo V[29]V[97] da portare a grandezza mondo: 30.46metri
#assert V[168]==[0.0, 0.9989]
#assert V[169]==[0.0414,0.9989]
#assert V[52]==[0.9528,0.9989]
#assert V[52][0]-V[169][0] == 0.9114
scala = 30.46/0.9114

W=((mat(V)-V[168])*scala).tolist()

base3=STRUCT(MKPOLS((W,EV)))
baseOFF3=OFFSET([0.3,0.3])(base3)
muri_level3=T(3)(7.5)(PROD([baseOFF3,Q(3)]))
#VIEW(muri_level3)
VIEW(STRUCT([muri_level1,muri_level2,muri_level3]))


#LEVEL4/5
lines = lines2lines("corte_level45.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[107] da portare nell'origine, spigolo V[29]V[97] da portare a grandezza mondo: 30.46metri
#assert V[107]==[0.0, 0.9989]
#assert V[108]==[0.0406,0.9989]
#assert V[103]==[0.952,0.9989]
#assert V[103][0]-V[108][0] == 0.9114
scala = 30.46/0.9114

W=((mat(V)-V[107])*scala).tolist()

base4=STRUCT(MKPOLS((W,EV)))
baseOFF4=OFFSET([0.3,0.3])(base4)
muri_level4=T(3)(10.5)(PROD([baseOFF4,Q(3)]))
muri_level5=T(3)(13.5)(PROD([baseOFF4,Q(3)]))
#VIEW(muri_level4)
VIEW(STRUCT([muri_level1,muri_level2,muri_level3,muri_level4,muri_level5]))


#LEVEL6
lines = lines2lines("corte_level6up.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[107] da portare nell'origine, spigolo V[29]V[97] da portare a grandezza mondo: 30.46metri
#assert V[192]==[0.0, 0.9989]
#assert V[131]==[0.0406,0.9989]
#assert V[160]==[0.952,0.9989]
#assert V[160][0]-V[131][0] == 0.9114
scala = 30.46/0.9114

W=((mat(V)-V[192])*scala).tolist()

base6=STRUCT(MKPOLS((W,EV)))
baseOFF6=OFFSET([0.3,0.3])(base6)
muri_level6=T(3)(16.5)(PROD([baseOFF6,Q(17.5)]))
#VIEW(muri_level6)
MURI=STRUCT([muri_level1,muri_level2,muri_level3,muri_level4,muri_level5,muri_level6])

VIEW(STRUCT([MURI,PREG]))

rot_SALA=R([1,2])(-PI-0.0872665)(T([1,2])([-10.475,-10.475])(PREG))
tras_SALA=T([1,2])([13.328,-31.416])(rot_SALA)


