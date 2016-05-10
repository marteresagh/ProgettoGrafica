#EDIFICIO ALLOGGI
#LEVEL1
lines = lines2lines("alloggi_level1.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[79][1]-V[182][1]: 0.6268
scala = 22.85/0.6268

W=(mat(V)*scala).tolist()

#muri si e no
EV_NO=sorted([114,85,153])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_1=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_1=OFFSET([0.3,0.3])(muri_1)
wall_1=PROD([muri_1,Q(4.5)])
balconi0=STRUCT(AA(POLYLINE)([[W[EV[85][0]],W[EV[85][1]]]]))
balconi=OFFSET([0.3,0.3])(balconi0)
balconi_1=T(3)(1.5)(PROD([balconi,Q(1.5)]))
WALL_1=STRUCT([wall_1,balconi_1])
#VIEW(WALL_1)

#LEVEL2
lines = lines2lines("alloggi_level2.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[79][1]-V[182][1]: 0.6268
scala = 22.85/0.6268

W=(mat(V)*scala).tolist()

#muri si e no
EV_NO=sorted([90,69,56,35,2])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_2=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_2=OFFSET([0.3,0.3])(muri_2)
wall_2=T(3)(4.5)(PROD([muri_2,Q(6)]))
#VIEW(wall_2)


#LEVEL5/7
lines = lines2lines("alloggi_level5_7.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[79][1]-V[182][1]: 0.6268
scala = 22.85/0.6268

W=(mat(V)*scala).tolist()

#muri si e no
EV_NO=sorted([53,126])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_5=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_5=OFFSET([0.3,0.3])(muri_5)
wall_5=T(3)(13.5)(PROD([muri_5,Q(3)]))
wall_7=T(3)(19.5)(PROD([muri_5,Q(3)]))
parete0=STRUCT(AA(POLYLINE)([[W[EV[168][0]],W[EV[168][1]]]]))
parete=OFFSET([0.3,0.3])(parete0)
parete4=T(3)(10.5)(PROD([parete,Q(3)]))
parete6=T(3)(16.5)(PROD([parete,Q(3)]))
parete8=T(3)(22.5)(PROD([parete,Q(3)]))

#LEVEL4/6/8
lines = lines2lines("alloggi_level6_8.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[79][1]-V[182][1]: 0.6268
scala = 22.85/0.6268

W=(mat(V)*scala).tolist()

#muri si e no
EV_NO=sorted([2,0,89])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_4=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_4=OFFSET([0.3,0.3])(muri_4)
wall_4=T(3)(10.5)(PROD([muri_4,Q(3)]))
wall_6=T(3)(16.5)(PROD([muri_4,Q(3)]))
wall_8=T(3)(22.5)(PROD([muri_4,Q(3)]))

#LEVEL9
lines = lines2lines("alloggi_level9.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[79][1]-V[182][1]: 0.6268
scala = 22.85/0.6268

W=(mat(V)*scala).tolist()

#muri si e no
EV_NO=sorted([73,112])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_9=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_9=OFFSET([0.3,0.3])(muri_9)
wall_9=T(3)(25.5)(PROD([muri_9,Q(3)]))


#LEVEL FINALE
lines = lines2lines("alloggi_finale.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[79][1]-V[182][1]: 0.6268
scala = 22.85/0.6268

W=(mat(V)*scala).tolist()

#muri si e no
EV_NO=sorted([106,42])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_finale=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_finale=OFFSET([0.3,0.3])(muri_finale)
wall_finale=T(3)(28.5)(PROD([muri_finale,Q(5.5)]))

#disegna level dopo il 9
muri=STRUCT([WALL_1,wall_2,wall_5,wall_6,wall_4,wall_7,wall_8,wall_9,parete4,parete6,parete8,wall_finale])

"""MARMO"""
lines = lines2lines("alloggi_marmo.lines")

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

scala = 22.85/0.6268

W=(mat(V)*scala).tolist()

frame=STRUCT(MKPOLS((W,EV)))
righe = T([1,2])([-0.15,-0.15])( OFFSET([0.6,0.6])(frame))
RIGHE=PROD([righe,INTERVALS(0.20)(1)])
MARMO=T(3)(1.4)(RIGHE)
rip_MARMO=STRUCT(NN(11)([MARMO,T(3)(3)]))
VIEW(STRUCT([rip_MARMO,muri]))
MURI=STRUCT([rip_MARMO,muri])
#VIEW(MURI)


 

"""PAVIMENTI"""
#PAVIMENTo LEVel1
lines = lines2lines("alloggi_pavimento.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((Y,FV))) #grafo pulito
#VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
#VIEW(larModelNumbering(1,1,1)(Y,[FV],submodel,0.1))

#assert Y[25]==[0.0, 0.5928]
#Y[25][0]-Y[37][0] == 0.9206
scala = 22.85/0.6268
Z=(mat(Y)*scala).tolist()
#**celle vuote**
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [7,3,19,2,6,4,5,8,18,13]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level1= DIFFERENCE([tot,buchi])
pavimento_level1=T([1,3])([-0.6,1.5])(PROD([frame_level1,Q(0.3)]))
#PAVIMENTO2
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [14,7,3,19,2,6,4,5,8,18,13,15,16]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level2= DIFFERENCE([tot,buchi])
pavimento_level2=T([1,3])([-0.6,4.5])(PROD([frame_level2,Q(0.3)]))
#pavimento3
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [7,3,19,2,6,4,5,8,18,13,15,16,20,14,17]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level2= DIFFERENCE([tot,buchi])
pavimento_level3=T([1,3])([-0.6,7.5])(PROD([frame_level2,Q(0.3)]))
pavimenti3=STRUCT(NN(3)([pavimento_level3,T(3)(3)]))
pavimento_level9=T([1,3])([-0.6,25.5])(PROD([frame_level2,Q(0.3)]))

pavimenti9=STRUCT(NN(2)([pavimento_level9,T(3)(3)]))

buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [7,3,19,2,6,4,5,8,18,13,20,17,14]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level11= DIFFERENCE([tot,buchi])
top=T([1,3])([-0.6,31.5])(PROD([frame_level11,Q(0.3)]))

#PAVIMENTo LEVel5
lines = lines2lines("alloggi5.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((Y,FV))) #grafo pulito
#VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
#VIEW(larModelNumbering(1,1,1)(Y,[FV],submodel,0.1))
scala = 22.85/0.6268
Z=(mat(Y)*scala).tolist()
#level5
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [25,6,0,19,18,5,20,1,21,2,16,17,7,11,8,10]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level5= DIFFERENCE([tot,buchi])
pavimento_level5=T([1,3])([-0.6,13.5])(PROD([frame_level5,Q(0.3)]))
pavimenti5=STRUCT(NN(4)([pavimento_level5,T(3)(3)]))
PAVIMENTI=STRUCT([pavimento_level1,pavimento_level2,pavimenti3,pavimenti5,pavimenti9,top])
#VIEW(STRUCT([MURI,PAVIMENTI]))

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
tr_buco1=T([1,2,3])([10.9,-0.4,14])(tr_buco)
tr_buco2=T([1,2,3])([10.9,33.9,14])(tr_buco)

#FINESTRE E FESSURE
triangle2=S([1,2])([6,3])(triangle)
triangle2=PROD([triangle2,Q(1.5)])
X,FX,EX=UKPOL(triangle2)
X = AA(CONS([S1,S3,S2]))(X)
tr_fin=STRUCT([MKPOL((X,FX,EX))])
tr_fin1=T([1,2,3])([10.9,13.3,14.6])(tr_fin)
tr_fin2=T([1,2,3])([10.9,22,14.6])(tr_fin)
tr_fin3=T([1,2,3])([10.9,13.3,20.6])(tr_fin)
tr_fin4=T([1,2,3])([10.9,22,20.6])(tr_fin)
TR_FIN=STRUCT([tr_fin1,tr_fin2,tr_fin3,tr_fin4])
fin1=T([1,2,3])([6,13.3,4.6])(CUBOID([10,1.5,3]))
fin2=T([1,2,3])([6,13.3,9.3])(CUBOID([10,1.5,3]))
fin3=T([1,2,3])([6,22,4.6])(CUBOID([10,1.5,3]))
fin4=T([1,2,3])([6,22,9.3])(CUBOID([10,1.5,3]))
FIN=STRUCT([fin1,fin2,fin3,fin4])

#VIEW(STRUCT([MURI,COLOR(RED)(tr_fin1),COLOR(RED)(tr_fin2),COLOR(RED)(tr_fin3),COLOR(RED)(tr_fin4),COLOR(RED)(fin1),COLOR(RED)(fin2),COLOR(RED)(fin3),COLOR(RED)(fin4)]))

BUCHI=STRUCT([tr_buco1,tr_buco2,TR_FIN,FIN])
MURI_ALLOGGI=DIFFERENCE([MURI,BUCHI])

VIEW(STRUCT([PAVIMENTI,MURI_ALLOGGI]))

