#INGRESSO NORD
lines = lines2lines("nord_level0.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
grafo=STRUCT(MKPOLS((V,EV))) #grafo pulito
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))

#V[22] da portare nell'origine, spigolo EV[7] da portare a grandezza mondo: 42metri
#assert V[22]==[0.0029, 0.0999]
#assert V[11]==[0.9959, 0.9972]
#assert V[18]==[0.0029, 0.9972]
#assert V[11][0]-V[18][0] == 0.993 #la grandezza massima non è precisa a 1

scala = 31.42/0.993

W=((mat(V)-V[22])*scala).tolist()

base0 = STRUCT(MKPOLS([W,FV]))
rialzo=PROD([base0,Q(1.5)])
#VIEW(rialzo)

EV_alti=sorted([7,5,0,4,22,3,21,26])
EV_bassi= set(range(len(EV))).difference(EV_alti)
muri_alti=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_alti]))
muri_bassi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_bassi]))

muri_bassi=OFFSET([0.3,0.3])(muri_bassi)
wall_bassi=PROD([muri_bassi,Q(7.5)])
muri_alti=OFFSET([0.3,0.3])(muri_alti)
wall_alti=PROD([muri_alti,Q(34)])
WALL=STRUCT([wall_bassi,wall_alti])

#MARMO
EV_cut=sorted([7,3,2,12,28,1,9,14,4,0,26,21])
EV_righe= set(range(len(EV))).difference(EV_cut)
frame=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_righe]))

righe = T([1,2])([-0.15,-0.15])( OFFSET([0.6,0.6])(frame))
RIGHE=PROD([righe,INTERVALS(0.20)(1)])
MARMO=T(3)(1.4)(RIGHE)
rip_MARMObottom=STRUCT(NN(3)([MARMO,T(3)(3)]))

#VIEW(STRUCT([WALL,rialzo]))

#MURI 
#LEVEL1

lines = lines2lines("nord_level1.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[6] da portare nell'origine, spigolo V[38]V[22] da portare a grandezza mondo: 42metri
scala = 31.42

W=((mat(V)-V[6])*scala).tolist()

#muri si e no
EV_NO=sorted([0,7,9,4,6])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_1=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))

muri_1=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muri_1)
wall_1=T(3)(1.5)(PROD([muri_1,Q(3)]))
#VIEW(STRUCT([wall_1,wall,rialzo]))

#LEVEL2
lines = lines2lines("nord_level2.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[6] da portare nell'origine, spigolo V[38]V[22] da portare a grandezza mondo: 42metri
scala = 31.42

W=((mat(V)-V[5])*scala).tolist()

#muri fini e muri spessi
EV_NO=sorted([0,7,5,8])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_2=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))

muri_2=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muri_2)
wall_2=T(3)(4.5)(PROD([muri_2,Q(3)]))
#VIEW(STRUCT([wall_2,wall_1,WALL,rialzo]))

#LEVEL3/4
lines = lines2lines("nord_level3.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

#V[6] da portare nell'origine, spigolo V[38]V[22] da portare a grandezza mondo: 42metri
scala = 31.42

W=((mat(V)-V[5])*scala).tolist()

#muri fini e muri spessi
EV_spessi=sorted([2,5,12,4,16])
EV_fini= set(range(len(EV))).difference(EV_spessi)
muri_fini=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_fini]))
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))

muri_fini=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muri_fini)
wall_fini=T(3)(7.5)(PROD([muri_fini,Q(6)]))
muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(7.5)(PROD([muri_spessi,Q(6)]))
wall_3=STRUCT([wall_spessi,wall_fini])
VIEW(STRUCT([wall_2,wall_1,WALL,wall_3,rialzo]))

#MARMO
EV_cut=sorted([1,11,3,15,8,10,7,0,13,9,6,14])
EV_righe= set(range(len(EV))).difference(EV_cut)
frame=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_righe]))

righe = T([1,2])([-0.15,-0.15])( OFFSET([0.6,0.6])(frame))
RIGHE=PROD([righe,INTERVALS(0.20)(1)])
MARMO=T(3)(10.4)(RIGHE)
rip_MARMOup=STRUCT(NN(8)([MARMO,T(3)(3)]))


#LEVEL5
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
EV_spessi=sorted([4,0,11,21,7,1,14,8])
EV_fini= set(range(len(EV))).difference(EV_spessi)
muri_fini=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_fini]))
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))

muri_fini=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muri_fini)
wall_fini=T(3)(13.5)(PROD([muri_fini,Q(3)]))
muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(13.5)(PROD([muri_spessi,Q(3)]))
wall_5=STRUCT([wall_spessi,wall_fini])
VIEW(STRUCT([wall_5,wall_2,wall_1,WALL,wall_3,rialzo]))


#LEVEL6
lines = lines2lines("nord_level6.lines")
grafo = STRUCT(AA(POLYLINE)(lines))
#VIEW(grafo)

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.2))

scala = 31.42

W=((mat(V)-V[16])*scala).tolist()

#muri fini e muri spessi
EV_fini=sorted([24,32,14,20,4,34,29,7,3,27,1,11])
EV_spessi= set(range(len(EV))).difference(EV_fini)
muri_fini=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_fini]))
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))

muri_fini=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muri_fini)
wall_fini=T(3)(16.5)(PROD([muri_fini,Q(3)]))
muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(16.5)(PROD([muri_spessi,Q(3)]))
wall_6=STRUCT([wall_spessi,wall_fini])
VIEW(STRUCT([wall_6,wall_5,wall_2,wall_1,WALL,wall_3,rialzo]))


#LEVEL7
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
EV_fini=sorted([13,7,8,6,15,2,16,0])
EV_spessi= set(range(len(EV))).difference(EV_fini)
muri_fini=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_fini]))
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))

muri_fini=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muri_fini)
wall_fini=T(3)(19.5)(PROD([muri_fini,Q(3)]))
muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(19.5)(PROD([muri_spessi,Q(3)]))
wall_7=STRUCT([wall_spessi,wall_fini])
VIEW(STRUCT([wall_7,wall_6,wall_5,wall_2,wall_1,WALL,wall_3,rialzo]))

#LEVEL8up
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

#muri fini e muri spessi
EV_fini=sorted([9,10,5,7,15,13,8,0])
EV_spessi= set(range(len(EV))).difference(EV_fini)
muri_fini=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_fini]))
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))

muri_fini=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muri_fini)
wall_fini=T(3)(22.5)(PROD([muri_fini,Q(11.5)]))
muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(22.5)(PROD([muri_spessi,Q(11.5)]))
wall_8up=STRUCT([wall_spessi,wall_fini])
VIEW(STRUCT([rip_MARMOup,rip_MARMObottom,wall_8up,wall_7,wall_6,wall_5,wall_2,wall_1,WALL,wall_3,rialzo]))



