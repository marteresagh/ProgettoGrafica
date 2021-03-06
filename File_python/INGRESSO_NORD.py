"INGRESSO NORD"
from larlib import *
lines = lines2lines("nord_level0.lines")
V,FV,EV,polygons = larFromLines(lines) 
grafo=STRUCT(MKPOLS((V,EV))) 
"""
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))
"""
#V[18][0]-V[11][0]=0.993

scala = 31.42/0.993

W=((mat(V)-V[22])*scala).tolist()

EV_alti=sorted([7,5,0,4,22,3,21,26])
EV_bassi= set(range(len(EV))).difference(EV_alti)
muri_alti=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_alti]))
muri_bassi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_bassi]))

muri_bassi=OFFSET([0.3,0.3])(muri_bassi)
wall_bassi=PROD([muri_bassi,Q(7.5)])
muri_alti=OFFSET([0.3,0.3])(muri_alti)
wall_alti=PROD([muri_alti,Q(34)])
WALL=STRUCT([wall_bassi,wall_alti])

wall_int1=T(3)(7.5+2.80)(CUBOID([31.72,0.3,26.5-2.80]))
wall_int2=T(3)(7.5)(CUBOID([13,0.3,2.80]))
wall_int3=T([1,3])([19,7.5])(CUBOID([31.72-13-6,0.3,2.80]))


WALL1=STRUCT([wall_int1,wall_int2,wall_int3,WALL])



"FINESTRE"

frame=CUBOID([2,1,27])
fessura1=T([1,2,3])([-.7,1.6,4.5])(frame)
fessura2=T([1,2,3])([30.7,1.6,4.5])(frame)
fessura3=T([1,2,3])([-.7,26.36,4.5])(frame)
fessura4=T([1,2,3])([30.7,26.36,4.5])(frame)
finestre=T([1,2,3])([12.6, 23.3,27])(CUBOID([7,5,3]))
#W[21][1]-W[13][1]: 5.573907999999999
fessura5=T([1,2,3])([12.6, 23.3,32.5])(CUBOID([7,5,1.2]))
buco_circ=CYLINDER([3,1.5])(32)
buco=R([1,3])(PI/2)(buco_circ)
bucotr=T([1,2,3])([0.7,14.5,7.5])(buco)
bucotr2=T([1,2,3])([32,14.5,7.5])(buco)
BUCHI=COLOR(RED)(STRUCT([fessura1,fessura2,fessura3,fessura4,fessura5,bucotr,bucotr2,finestre]))
#VIEW(STRUCT([INGRESSO,PAVIMENTI]))


"LEVEL3"
lines = lines2lines("nord_level3.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
"""
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))
"""
scala = 31.42

W=((mat(V)-V[5])*scala).tolist()

#muri fini e muri spessi
EV_spessi=sorted([12,16])
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))

muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(7.5)(PROD([muri_spessi,Q(26.5)]))
wall_3=wall_spessi
#VIEW(STRUCT([wall_2,wall_1,WALL,wall_3,rialzo]))
frame_muro1=STRUCT(MKPOLS((W,[EV[2]])))
muri_lat1=OFFSET([0.3,0.3])(frame_muro1)
wall_lat01=T(3)(7.5)(PROD([muri_lat1,Q(26.5)]))
frame_muro2=STRUCT(MKPOLS((W,[EV[4]])))
muri_lat2=OFFSET([0.3,0.3])(frame_muro2)
wall_lat02=T(3)(7.5)(PROD([muri_lat2,Q(26.5)]))

wall_lat1=DIFFERENCE([wall_lat01,BUCHI])
wall_lat2=DIFFERENCE([wall_lat02,BUCHI])

WALL2=STRUCT([wall_3,wall_lat1,wall_lat2])
#VIEW(WALL2)

"LEVEL5"
lines = lines2lines("nord_level5.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

scala = 31.42

W=((mat(V)-V[7])*scala).tolist()

#muri fini e muri spessi
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in [3,2]]))

muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(13.5)(PROD([muri_spessi,Q(3)]))
muro_basso=STRUCT(MKPOLS((W,[EV[8]])))
balcone=OFFSET([0.3,0.3])(muro_basso)
wall_basso=T(3)(13.5)(PROD([balcone,Q(1.5)]))
wall_5=STRUCT([wall_spessi,wall_basso])

#VIEW(STRUCT([wall_5,wall_2,wall_1,WALL,wall_3]))

"LEVEL7"
lines = lines2lines("nord_level7.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

scala = 31.42

W=((mat(V)-V[3])*scala).tolist()

#muri fini e muri spessi

EV_spessi= [5,11]
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))

muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(19.5)(PROD([muri_spessi,Q(3)]))
muro_basso=STRUCT(MKPOLS((W,[EV[4]])))
balcone=OFFSET([0.3,0.3])(muro_basso)
wall_basso=T(3)(19.5)(PROD([balcone,Q(1.5)]))
wall_7=STRUCT([wall_spessi,wall_basso])
#VIEW(STRUCT([wall_7,wall_6,wall_5,wall_2,WALL,wall_3,WALL_1]))

#LEVEL8
lines = lines2lines("nord_level8.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

scala = 31.42

W=((mat(V)-V[6])*scala).tolist()
#W[9]== [19.125354, 22.820346, 30]
#W[3]==[12.822502000000002, 22.839198000000003,30]
#W[9][0]-W[3][0]==6.302852

#muri fini e muri spessi
EV_spessi= [14,11]
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))

muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(22.5)(PROD([muri_spessi,Q(9)]))
muro_basso=STRUCT(MKPOLS((W,[EV[3]])))
balcone=OFFSET([0.3,0.3])(muro_basso)
wall_basso=T(3)(25.5)(PROD([balcone,Q(1.5)]))
wall_9=STRUCT([wall_basso,wall_spessi])

#LEVEL_top
lines = lines2lines("nord_top.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

scala = 31.42

W=((mat(V)-V[10])*scala).tolist()

#muri fini e muri spessi

EV_spessi= [21,22,8,14,1,6,15]
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))

muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(31.5)(PROD([muri_spessi,Q(2.5)]))
wall_top=wall_spessi


#muro in alto al centro 
muro=CUBOID([6.302852,0.3,3])
muro_centro=T([1,2,3])([12.822502000000002, 22.839198000000003,30])(muro)

MURI0=STRUCT([WALL1,WALL2,wall_5,wall_7,wall_9,wall_top,muro_centro])

"PAVIMENTI"
#LEVEL3
lines = lines2lines("nord_pav3.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((Y,FV))) #grafo pulito
#VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
#VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))


#Y[9][0]-Y[0][0] == 0.9345
scala = 31.42/0.9345
Z=((mat(Y)-Y[0])*scala).tolist()
#ZZ = AA(LIST)(range(len(Z)))
#submodel = STRUCT(MKPOLS((Z,EV)))
#VIEW(larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,0.1))
#**celle vuote**
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [0,1,2,3]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level3= DIFFERENCE([tot,buchi])
pavimento_level3=T(3)(7.2)(PROD([frame_level3,Q(0.3)]))
#VIEW(pavimento_level2)
#VIEW(STRUCT([ingresso,COLOR(RED)(pavimento_level3)]))


#LEVEL5
lines = lines2lines("nord_pav5.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
grafo=STRUCT(MKPOLS((V,EV))) #grafo pulito
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))
#muri del livello5
# W[6]: [7.7104680000000005, 0.0]
# W[5]: [24.234246000000002, 0.0]
# W[5][0]-W[6][0]: 16.523778
scala = 16.523778

W=((mat(V)-V[2])*scala).tolist()

base=STRUCT(MKPOLS((W,FV)))
pav5=T([1,2,3])([7.7104680000000005, 0.0, 13.2])(PROD([base,Q(0.3)]))
#VIEW(pav5)
#LEVEL9
lines = lines2lines("nord_pav9.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((Y,FV))) #grafo pulito
#VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
#VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.2))


#Y[23][0]-Y[29][0] == 0.9195
scala = 31.42/0.9195
Z=((mat(Y)-Y[29])*scala).tolist()
"""
ZZ = AA(LIST)(range(len(Z)))
submodel = STRUCT(MKPOLS((Z,EV)))
VIEW(larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,0.1))
"""
buchi_top = STRUCT(MKPOLS([Z,[FV[k] for k in [0,1,2,3,6]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_top= DIFFERENCE([tot,buchi_top])
top=T([1,3])([0.1,31.5])(PROD([frame_top,Q(0.3)]))

PAVIMENTI=STRUCT([pavimento_level3,pav5,top])


"""porta di ingresso"""
porta=T([1,2,3])([13,-.7,7.5])(CUBOID([6,1.5,2.80]))

"""PORTONE"""
a=STRUCT(NN(2)([CUBOID([6,0.1,0.3]),T(3)(1)]))
b=STRUCT(NN(5)([T(1)(0.85)(CUBOID([0.3,0.1,2.8])),T(1)(1)]))
c=OFFSET([0.1,0.1,0.1])(SKEL_1(CUBOID([5.9,0,2.7])))
PORTONE=T([1,2,3])([13,0.1,7.5])(STRUCT([a,b,c]))


#GRIGLIE
seg=CUBOID([1.2,0.05,0.05])
grid=R([1,2])(PI/2)(STRUCT(NN(35)([seg,T(3)(0.75)])))
grid_fessure1=T([1,2,3])([.15,1.5,5.25])(grid)
grid_fessure2=T([1,2,3])([31.57,1.5,5.25])(grid)
grid_fessure3=T([1,2,3])([.15,26.26,5.25])(grid)
grid_fessure4=T([1,2,3])([31.57,26.26,5.25])(grid)
grid1=S(2)(5./3)(SKEL_1(STRUCT(MKPOLS(larCuboids([3,3])))))
grid_fin=OFFSET([0.05,0.05])(grid1)
grid_fin=R([1,3])(PI/2)(PROD([grid_fin,Q(0.05)]))
fin_1=T([1,2,3])([13,23.3,27])(grid_fin)
fin_2=T([1,2,3])([19.3,23.3,27])(grid_fin)
GRATE0=STRUCT([grid_fessure1,grid_fessure2,grid_fessure3,grid_fessure4])
#VIEW(STRUCT([INGRESSO,fin_1,fin_2]))

"""pareti oblique"""

#W[12]:[8.181768000000002, 14.198698000000002]
#W[13]: [12.822502000000002, 6.246295999999999]
#SQRT((W[12][0]-W[13][0])**2+(W[12][1]-W[13][1])**2): 9.207448594934432
#W[16]: [6.362550000000001, 13.265524]
#W[17]: [11.386608, 4.653302000000001]
#SQRT((W[16][0]-W[17][0])**2+(W[16][1]-W[17][1])**2): 9.970532912770912

#W[18]: [2.6707000000000005, 11.402318000000001]
#W[19]: [7.7104680000000005, 2.7618180000000003]
#SQRT((W[18][0]-W[19][0])**2+(W[18][1]-W[19][1])**2): 10.00287467400367
#W[0][1]-W[6][1]: 28.394254
#W[27]: [24.253098, 25.946636000000005]

parete1=T([1,2,3])([8.181768000000002, 14.198698000000002,7.5])(R([1,2])(-PI/3)(CUBOID([9.207448594934432,0.3,26.5])))
parete2=T([1,2,3])([6.362550000000001, 13.265524,7.5])(R([1,2])(-PI/3)(CUBOID([9.970532912770912,0.3,26.5])))
parete3=T([1,2,3])([2.6707000000000005, 11.402318000000001,7.5])(R([1,2])(-PI/3)(CUBOID([10.00287467400367,0.3,12])))
PARETE=STRUCT([parete1,parete2,parete3])


"""BUCHI"""
buco= T(3)(-1)(CYLINDER([4,8])(32))
cerchi=R([1,3])(PI/2)(buco)
foro3=T([1,2,3])([10.5,10.21,13.5])(R([1,2])(PI/6)(cerchi))
foro4=T([1,2,3])([10.5,10.21,26.5])(R([1,2])(PI/6)(cerchi))
FORO=STRUCT([foro3,foro4])
OBLIQUI=DIFFERENCE([PARETE,FORO])
OBLIQUI2=T(2)(14.889938000000003)(S(2)(-1)(T(2)(-28.394254/2)(OBLIQUI)))
OBL_dx=STRUCT([OBLIQUI,OBLIQUI2])
OBL_sx=T(1)([18.66])(S(1)(-1)(T(1)(-13.5)(OBL_dx)))

muri=STRUCT([MURI0,OBL_dx,OBL_sx])

"""grate"""
#grata finestre
grid=SKEL_1(STRUCT(MKPOLS(larCuboids([4,1]))))
grid2=T([1,2])([.5,1])(SKEL_1(STRUCT(MKPOLS(larCuboids([3,1])))))
grid_rip=STRUCT(NN(2)([(STRUCT([grid,grid2])),T(2)(2)]))
bordofin=SKEL_1(CUBOID([4,4]))
seg=T([1])(.5)(R([1,2])(-PI/2)(INTERVALS(2)(1)))
grata=STRUCT(NN(4)([seg,T(1)(1)]))
grata_2=T(2)(6)(grata)
grata_3=T(1)(-2)(R([1,2])(PI/2)(grata))
grata_4=T(1)(6)(grata_3)
GRID=STRUCT([grata,grata_2,grata_3,grata_4,bordofin,grid_rip])
gridOFF=OFFSET([0.05,0.05])(GRID)
GRATA_fin=T([1,2])([-2,-2])(PROD([gridOFF,Q(0.05)]))
GRATA=R([2,3])(PI/2)(R([1,3])(PI/2)(GRATA_fin))
fin1=T([1,2,3])([0.15,14.5,7.5])(GRATA)
fin2=T([1,2,3])([31.57,14.5,7.5])(GRATA)

 #grata fessure
frame0=SKEL_1(PROD([Hpc(Grid([2*[2.5/2]])),Hpc(Grid([35*[31./35]]))]))
frame1=T(2)(-1.5)(CUBOID([2.5,1.5]))
frame2=T(2)(31)(CUBOID([2.5,1.5]))
mur=STRUCT([frame1,frame2])
gridOFF=OFFSET([0.05,0.05])(frame0)
grid_fess=T(3)(0.15)(PROD([gridOFF,Q(0.05)]))
muretti=COLOR([0.6,0.6,0.6])(PROD([mur,Q(0.3)]))
FESSURE0=R([2,3])(PI/2)(T(2)(1.5)(STRUCT([muretti,grid_fess])))
FESS1=T(1)(0.3)(R([1,2])(5*PI/4)(FESSURE0))
FESS2=T([1,2])([31.72,0.3])(R([1,2])(-PI/4)(FESSURE0))
FESSURE=STRUCT([FESS1,FESS2])

GRATE=STRUCT([fin1,fin2,FESSURE,GRATE0])

VIEW(STRUCT([T(2)(0.1)(PAVIMENTI),COLOR([0.6,0.6,0.6])(muri),GRATE,COLOR([0.5,0.4,0.4])(PORTONE)]))

INGR_NORD=STRUCT([T(2)(0.1)(PAVIMENTI),COLOR([0.6,0.6,0.6])(muri),GRATE,COLOR([0.5,0.4,0.4])(PORTONE)])
NORD=T([1,2])([36.1, 64.33069161376547])(INGR_NORD)
