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

#muri si e no
EV_NO=sorted([7,109,108,48])
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
EV_NO=sorted([52,6,119,62,95,125])
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
EV_NO=sorted([88,2,14,119])
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
EV_NO=sorted([9,152,141,157])
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
EV_NO=sorted([63,15,104])
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
EV_NO=sorted([143,110,141,15])
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
EV_NO=sorted([68,105,129,81,74,6,95,23,42])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_9=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_9=OFFSET([0.3,0.3])(muri_9)
wall_9=T(3)(25.5)(PROD([muri_9,Q(6)]))

pil=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in [6,95,23,42]]))
pil=OFFSET([0.3,0.3])(pil)
pilastri=T(3)(25.5)(PROD([pil,Q(0.3)]))
WALL_9=STRUCT([wall_9,pilastri])
EV_NOfinale=sorted([1,108,74,149,34,53,49,63,15,16,154,0,81,80,161,51,123,10,25,105,129,68,42,23,95,6,51,66])
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
EV_SI= sorted([6,100,21,94,30,78])
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

