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
EV_NO=sorted([126,101,93,133,37])
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
EV_NO=sorted([53,126,168])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_5=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_5=OFFSET([0.3,0.3])(muri_5)
wall_5=T(3)(13.5)(PROD([muri_5,Q(3)]))
wall_7=T(3)(19.5)(PROD([muri_5,Q(3)]))

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
EV_NO=sorted([2,0])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_4=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_4=OFFSET([0.3,0.3])(muri_4)
parete0=STRUCT(AA(POLYLINE)([[W[EV[89][0]],W[EV[89][1]]]]))
parete=OFFSET([0.3,0.3])(parete0)
parete5=T(3)(13.5)(PROD([parete,Q(3)]))
parete7=T(3)(19.5)(PROD([parete,Q(3)]))
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

#disegna level dopo il 9
muri=STRUCT([WALL_1,wall_2,wall_5,wall_6,wall_4,wall_7,wall_8,wall_9,parete5,parete7])

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


VIEW()


#sistema piani 2 e 3, e il marmo taglia un pezzo 
