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
#VIEW(STRUCT([wall_2,wall_1,WALL,wall_3,rialzo]))

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
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi if e!=8]))

muri_fini=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muri_fini)
wall_fini=T(3)(13.5)(PROD([muri_fini,Q(3)]))
muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(13.5)(PROD([muri_spessi,Q(3)]))
muro_basso=STRUCT(MKPOLS((W,[EV[8]])))
balcone=OFFSET([0.3,0.3])(muro_basso)
wall_basso=T(3)(13.5)(PROD([balcone,Q(1.5)]))
wall_5=STRUCT([wall_spessi,wall_fini,wall_basso])

#VIEW(STRUCT([wall_5,wall_2,wall_1,WALL,wall_3,rialzo]))


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
#VIEW(STRUCT([wall_6,wall_5,wall_2,wall_1,WALL,wall_3,rialzo]))


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
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi if e!=4]))

muri_fini=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muri_fini)
wall_fini=T(3)(19.5)(PROD([muri_fini,Q(3)]))
muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(19.5)(PROD([muri_spessi,Q(3)]))
muro_basso=STRUCT(MKPOLS((W,[EV[4]])))
balcone=OFFSET([0.3,0.3])(muro_basso)
wall_basso=T(3)(19.5)(PROD([balcone,Q(1.5)]))
wall_7=STRUCT([wall_spessi,wall_fini,wall_basso])
#VIEW(STRUCT([wall_7,wall_6,wall_5,wall_2,wall_1,WALL,wall_3,rialzo]))

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
EV_fini=sorted([9,10,5,7,15,13,8,0])
EV_spessi= set(range(len(EV))).difference(EV_fini)
muri_fini=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_fini]))
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi if e!=3]))

muri_fini=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muri_fini)
wall_fini=T(3)(22.5)(PROD([muri_fini,Q(3)]))
muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(22.5)(PROD([muri_spessi,Q(3)]))

wall_8=STRUCT([wall_spessi,wall_fini])

#LEVEL9
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
EV_fini=sorted([9,10,5,7,15,13,8,0])
EV_spessi= set(range(len(EV))).difference(EV_fini)
muri_fini=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_fini]))
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi if e!=3]))

muri_fini=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muri_fini)
wall_fini=T(3)(25.5)(PROD([muri_fini,Q(6)]))
muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(25.5)(PROD([muri_spessi,Q(6)]))
muro_basso=STRUCT(MKPOLS((W,[EV[3]])))
balcone=OFFSET([0.3,0.3])(muro_basso)
wall_basso=T(3)(25.5)(PROD([balcone,Q(1.5)]))
wall_9=STRUCT([wall_basso,wall_spessi,wall_fini])

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
EV_fini=sorted([16,12,4,19,18,11,7,17])
EV_spessi= set(range(len(EV))).difference(EV_fini)
muri_fini=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_fini]))
muri_spessi=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_spessi]))

muri_fini=OFFSET([0.3/SQRT(2),0.3/SQRT(2)])(muri_fini)
wall_fini=T(3)(31.5)(PROD([muri_fini,Q(2.5)]))
muri_spessi=OFFSET([0.3,0.3])(muri_spessi)
wall_spessi=T(3)(31.5)(PROD([muri_spessi,Q(2.5)]))
wall_top=STRUCT([wall_spessi,wall_fini])




#PAVIMENTI: figure concave!!!
#LEVEL2
lines = lines2lines("nord_pav2.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((Y,FV))) #grafo pulito
VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))

#assert Y[25]==[0.0, 0.5928]
#Y[25][0]-Y[37][0] == 0.9206
scala = 31.42/0.9206
Z=((mat(Y)-Y[25])*scala).tolist()
#ZZ = AA(LIST)(range(len(Z)))
#submodel = STRUCT(MKPOLS((Z,EV)))
#VIEW(larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,0.1))
#**celle vuote**
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [1,0,4,5,3,2,6,7,8,9]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level2= DIFFERENCE([tot,buchi])
pavimento_level2=T(3)(4.25)(PROD([frame_level2,Q(0.3)]))
#VIEW(pavimento_level2)
VIEW(STRUCT([ingresso,COLOR(RED)(pavimento_level2)]))

#LEVEL3
lines = lines2lines("nord_pav3.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((Y,FV))) #grafo pulito
VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))


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
pavimento_level3=T(3)(7.25)(PROD([frame_level3,Q(0.3)]))
#VIEW(pavimento_level2)
VIEW(STRUCT([ingresso,COLOR(RED)(pavimento_level3)]))


#LEVEL5
lines = lines2lines("nord_pav5.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
grafo=STRUCT(MKPOLS((V,EV))) #grafo pulito
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))
#muri del livello5
# W[6]: [7.7104680000000005, 0.0]
# W[5]: [24.234246000000002, 0.0]
# W[5][0]-W[6][0]: 16.523778
scala = 16.523778

W=((mat(V)-V[2])*scala).tolist()

base=STRUCT(MKPOLS((W,FV)))
pav5=T([1,2,3])([7.7104680000000005, 0.0, 13.25])(PROD([base,Q(0.3)]))
VIEW(pav5)

#LEVEL6
lines = lines2lines("nord_pav6.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((Y,FV))) #grafo pulito
#VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))


#Y[30][0]-Y[34][0] == 0.9603999999999999
scala = 31.42/0.9603999999999999
Z=((mat(Y)-Y[34])*scala).tolist()
#ZZ = AA(LIST)(range(len(Z)))
#submodel = STRUCT(MKPOLS((Z,EV)))
#VIEW(larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,0.1))
#**celle vuote**
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [3,6,8,0,2,11,10,13,12,5,1,9,7,4,16]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level6= DIFFERENCE([tot,buchi])
pavimento_level6=T(3)(16.25)(PROD([frame_level6,Q(0.3)]))

VIEW(STRUCT([ingresso,COLOR(RED)(pavimento_level6)]))

#LEVEL7
lines = lines2lines("nord_pav7.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((Y,FV))) #grafo pulito
#VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.2))


#Y[1][0]-Y[9][0] == 0.9549
scala = 31.42/0.9549
Z=((mat(Y)-Y[9])*scala).tolist()
#ZZ = AA(LIST)(range(len(Z)))
#submodel = STRUCT(MKPOLS((Z,EV)))
#VIEW(larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,0.1))
#**celle vuote**
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [0,1,2,3,4,5]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level7= DIFFERENCE([tot,buchi])
pavimento_level7=T(3)(19.25)(PROD([frame_level7,Q(0.3)]))

VIEW(STRUCT([ingresso,COLOR(RED)(pavimento_level7)]))

#LEVEL9
lines = lines2lines("nord_pav9.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((Y,FV))) #grafo pulito
#VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.2))


#Y[23][0]-Y[29][0] == 0.9195
scala = 31.42/0.9195
Z=((mat(Y)-Y[29])*scala).tolist()
ZZ = AA(LIST)(range(len(Z)))
submodel = STRUCT(MKPOLS((Z,EV)))
VIEW(larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,0.1))
#**celle vuote**
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [0,1,2,3,4,5,6,7]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level9= DIFFERENCE([tot,buchi])
pavimento_level9=T([1,3])([0.1,25.25])(PROD([frame_level9,Q(0.3)]))

VIEW(STRUCT([ingresso,COLOR(RED)(pavimento_level9)]))


buchi_top = STRUCT(MKPOLS([Z,[FV[k] for k in [0,1,2,3,6]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_top= DIFFERENCE([tot,buchi_top])
top=T([1,3])([0.1,31.25])(PROD([frame_top,Q(0.3)]))

VIEW(STRUCT([ingresso,COLOR(RED)(top)]))
PAVIMENTI=STRUCT([pavimento_level2,pavimento_level3,pav5,pavimento_level6,pavimento_level7,pavimento_level9,top])
VIEW(STRUCT([ingresso,PAVIMENTI]))

#fessure e buchi 
#Z[10]: [31.42, 1.0695443175638941]
#Z[13]: [31.42, 28.392471995649814]

#muro in alto al centro 
muro=CUBOID([6.302852,0.3,3])
muro_centro=T([1,2,3])([12.822502000000002, 22.839198000000003,30])(muro)

ingresso=STRUCT([rip_MARMOup,rip_MARMObottom,wall_top,wall_8,wall_9,wall_7,wall_6,wall_5,wall_2,wall_1,WALL,wall_3,rialzo,muro_centro])
VIEW(ingresso)

#fessure

frame=COLOR(RED)(CUBOID([2,1,27]))
fessura1=T([1,2,3])([-.7,1.6,4.5])(frame)
fessura2=T([1,2,3])([30.7,1.6,4.5])(frame)
fessura3=T([1,2,3])([-.7,26.36,4.5])(frame)
fessura4=T([1,2,3])([30.7,26.36,4.5])(frame)
finestre=T([1,2,3])([12.6, 23.3,27])(CUBOID([7,5,3]))
#W[21][1]-W[13][1]: 5.573907999999999
fessura5=T([1,2,3])([12.6, 23.3,32.5])(CUBOID([7,5,1.2]))
buco_circ=CYLINDER([3,1.5])(100)
buco=R([1,3])(PI/2)(buco_circ)
bucotr=T([1,2,3])([0.7,14.5,7.5])(buco)
bucotr2=T([1,2,3])([32,14.5,7.5])(buco)
BUCHI=COLOR(RED)(STRUCT([fessura1,fessura2,fessura3,fessura4,fessura5,bucotr,bucotr2,finestre]))
INGRESSO=DIFFERENCE([ingresso,BUCHI])
VIEW(STRUCT([INGRESSO,PAVIMENTI]))

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
#VIEW(STRUCT([INGRESSO,fin_1,fin_2]))

GRATE=STRUCT([fin_1,fin_2,grid_fessure1,grid_fessure2,grid_fessure3,grid_fessure4])
VIEW(STRUCT([GRATE,INGRESSO,PAVIMENTI]))




