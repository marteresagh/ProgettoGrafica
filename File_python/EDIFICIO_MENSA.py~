#EDIFICIO MENSA
#MURI
#LEVEL1
lines = lines2lines("mensa_level1.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[55][1]-V[79][1]: 0.8166
scala = 31.42/0.8166

W=((mat(V)-V[70])*scala).tolist()
WW = AA(LIST)(range(len(W)))
submodel = STRUCT(MKPOLS((W,EV)))
#VIEW(larModelNumbering(1,1,1)(W,[WW,EV],submodel,0.2))

#muri si e no
EV_NO=sorted([7,109,108,48,21,45])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_1=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))

muri_1=OFFSET([0.3,0.3])(muri_1)
wall_1=PROD([muri_1,Q(4.5)])
wall_3=T(3)(7.5)(PROD([muri_1,Q(3)]))
#VIEW(wall_1)

#LEVEL2
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
EV_NO=sorted([52,6,119,62,95,125,167,133])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_2=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
balconi0=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in [95,125]]))
balconi=OFFSET([0.3,0.3])(balconi0)
balconi_1=T(3)(4.5)(PROD([balconi,Q(1.5)]))
muri_2=OFFSET([0.3,0.3])(muri_2)
wall_2=T(3)(4.5)(PROD([muri_2,Q(3)]))
WALL_2=STRUCT([wall_2,balconi_1])
wall_4=T(3)(6)(WALL_2)
#VIEW(wall_2)
VIEW(STRUCT([wall_1,WALL_2,wall_3,wall_4]))

#LEVEL5
lines = lines2lines("mensa_level5.lines")
#grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[72][1]-V[73][1]: 0.8166
scala = 31.42/0.8166

W=((mat(V)-V[161])*scala).tolist()

#muri si e no
EV_NO=sorted([88,2,14,119,125,19])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_5=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
balconi0=STRUCT(AA(POLYLINE)([[W[EV[2][0]],W[EV[2][1]]]]))
balconi=OFFSET([0.3,0.3])(balconi0)
balconi_5=T(3)(13.5)(PROD([balconi,Q(1.5)]))
muri_5=OFFSET([0.3,0.3])(muri_5)
wall_5=T(3)(13.5)(PROD([muri_5,Q(3)]))
WALL_5=STRUCT([wall_5,balconi_5])

#LEVEL6
lines = lines2lines("mensa_level6.lines")
#grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[120][1]-V[121][1]: 0.8166
scala = 31.42/0.8166

W=((mat(V)-V[130])*scala).tolist()

#muri si e no
EV_NO=sorted([9,152,141,157,126,51])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_6=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_6=OFFSET([0.3,0.3])(muri_6)
wall_6=T(3)(16.5)(PROD([muri_6,Q(3)]))

#LEVEL7
lines = lines2lines("mensa_level7.lines")
#grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[120][1]-V[121][1]: 0.8166
scala = 31.42/0.8166

W=((mat(V)-V[168])*scala).tolist()

#muri si e no
EV_NO=sorted([63,15,104,148,165])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_7=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_7=OFFSET([0.3,0.3])(muri_7)
wall_7=T(3)(19.5)(PROD([muri_7,Q(3)]))

#LEVEL8
lines = lines2lines("mensa_level8.lines")
#grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[84][1]-V[85][1]: 0.8166
scala = 31.42/0.8166

W=((mat(V)-V[118])*scala).tolist()

#muri si e no
EV_NO=sorted([143,110,141,15,164,130])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_8=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_8=OFFSET([0.3,0.3])(muri_8)
wall_8=T(3)(22.5)(PROD([muri_8,Q(3)]))

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

#muri si e no
EV_NO=sorted([68,105,129,81,74,6,95,23,42,46,158])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_9=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_9=OFFSET([0.3,0.3])(muri_9)
wall_9=T(3)(25.5)(PROD([muri_9,Q(6)]))

pil=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in [6,95,23,42]]))
pil=OFFSET([0.3,0.3])(pil)
pilastri=T(3)(25.5)(PROD([pil,Q(0.3)]))
WALL_9=STRUCT([wall_9,pilastri])
EV_NOfinale=sorted([1,108,74,149,34,53,49,63,15,16,154,0,81,80,161,51,123,10,25,105,129,68,42,23,95,6,51,66,46,158])
EV_SIfinale= set(range(len(EV))).difference(EV_NOfinale)
muri_finale=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SIfinale]))
muri_finale=OFFSET([0.3,0.3])(muri_finale)
wall_finale=T(3)(25.5)(PROD([muri_finale,Q(8.5)]))

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
EV_SI= sorted([6,100,21,94,30,78,])
muri_11=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_11=OFFSET([0.3,0.3])(muri_11)
wall_11=T(3)(31.5)(PROD([muri_11,Q(2.5)]))
muri=STRUCT([wall_1,WALL_2,wall_3,wall_4,WALL_5,wall_6,wall_7,wall_8,WALL_9,wall_11,wall_finale])
VIEW(muri)

"""MARMO e BUCHI"""
#MARMO
lines = lines2lines("mensa_marmo.lines")

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

scala = 31.42/0.8166

W=((mat(V)-V[10])*scala).tolist()

frame=STRUCT(MKPOLS((W,EV)))
righe = T([1,2])([-0.15,-0.15])( OFFSET([0.6,0.6])(frame))
RIGHE=PROD([righe,INTERVALS(0.20)(1)])
MARMO=T(3)(1.4)(RIGHE)
rip_MARMO=STRUCT(NN(11)([MARMO,T(3)(3)]))
VIEW(STRUCT([rip_MARMO,muri]))
MURI=STRUCT([rip_MARMO,muri])
#BUCHI
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
MENSA=DIFFERENCE([MURI,parete])
VIEW(MENSA)

""" PAVIMENTI """

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


ZZ = AA(LIST)(range(len(Z)))
submodel = STRUCT(MKPOLS((Z,EV)))
#VIEW(larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,1))

FV[18]=[42,43,128,110,111,82]
FV[19]=[25,132,101,106,62,18]
FV[5]=[109,50,49,43,42]
#**celle vuote**
"""level1"""
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [13,12,18,19]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level1= DIFFERENCE([tot,buchi])
pavimento_level1=T(3)(1.25)(PROD([frame_level1,Q(0.3)]))
#VIEW(pavimento_level1)

"""level3"""
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [13,12,18,19,1,2,3,4]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level3= DIFFERENCE([tot,buchi])
pavimento_level3=T(3)(7.25)(PROD([frame_level3,Q(0.3)]))
pavimento_level5=T(3)(13.25)(PROD([frame_level3,Q(0.3)]))
#VIEW(pavimento_level3)

"""level 7"""
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [13,12,18,19,1,2,3,4,16]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level7= DIFFERENCE([tot,buchi])
pavimento_level7=T(3)(19.25)(PROD([frame_level7,Q(0.3)]))
pavimento_level9=T(3)(25.25)(PROD([frame_level7,Q(0.3)]))

"""top"""
buchi = STRUCT(MKPOLS([Z,[FV[16]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_top= DIFFERENCE([tot,buchi])
top=T(3)(31.25)(PROD([frame_top,Q(0.3)]))



"""level2"""
lines = lines2lines("mensa_pav2.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((Y,FV))) #grafo pulito
#VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
#VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))


scala = 38.4766103355376/0.948
Z=((mat(Y)-Y[99])*scala).tolist()

ZZ = AA(LIST)(range(len(Z)))
submodel = STRUCT(MKPOLS((Z,EV)))
#VIEW(larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,1))

buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [14,9,0,10,1,2,3,4]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level2= DIFFERENCE([tot,buchi])
pavimento_level2=T([2,3])([2.6818197403869712,4.25])(PROD([frame_level2,Q(0.3)]))
level_2up=STRUCT(NN(4)([pavimento_level2,T(3)(6)]))
#VIEW(pavimento_level2)

PAVIMENTI=STRUCT([top,level_2up,pavimento_level1,pavimento_level3,pavimento_level5,pavimento_level7,pavimento_level9])

"""FINESTRE"""

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
LAT_sx=T(2)(-3.3)(STRUCT([fin_laterali,trave_top,travi,trave_base]))
LAT_dx=T(2)(35.02)(LAT_sx)
#VIEW(LAT)
VIEW(STRUCT([LAT_dx,LAT_sx,MENSA,PAVIMENTI]))



