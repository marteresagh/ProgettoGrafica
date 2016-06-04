#CENTRALE
"""inizio"""
lines = lines2lines("centrale.lines")
grafo = STRUCT(AA(POLYLINE)(lines))


#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[0] da portare nell'origine 
#V[51][0]-V[78][0]= 0.3094

scala = 31.42/0.3094

W=((mat(V)-V[0])*scala).tolist()
WW = AA(LIST)(range(len(W)))
submodel = STRUCT(MKPOLS((W,EV)))
mappa=larModelNumbering(1,1,1)(W,[WW,EV,FV],submodel,5)
#WW = AA(LIST)(range(len(W)))
#submodel = STRUCT(MKPOLS((W,EV)))
#VIEW(larModelNumbering(1,1,1)(W,[WW,EV],submodel,5))

#base =STRUCT(MKPOLS((W,EV)))
#VIEW(base)


"""PRESE D'ARIA"""
#W[171]: [58.17879120879121, 45.53564318034906]
#W[109]:[58.17879120879121, 34.08064641241113]
#W[153]: [61.32688429217841, 32.7706334841629]



EV_si=sorted([54,73,34])
muri_alti=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_si]))
muri_alti=OFFSET([0.3,0.3])(muri_alti)
aria=PROD([muri_alti,Q(46)])
#VIEW(aria)

EV_alti=sorted([220,104,230,109,233,91])
muri=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_alti]))
muri=OFFSET([0.3,0.3])(muri)
passo=T([1,2])([-.12,-.1])(PROD([muri,Q(34)]))
#VIEW(passo)

#parete larga=SQRT((W[65][0]-W[171][0])**2+(W[65][1]-W[171][1])**2)=12.181106137187708
#parete laterale=W[182][0]-W[102][0]=11.454996767937942
parete_front= CUBOID([12.381106137187708,0.3,46])

lines = lines2lines("cerchio_centr.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
grafo=STRUCT(MKPOLS((V,EV))) #grafo pulito
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))
scala=9.5/0.6351
W=((mat(V)-V[43]-[0.6351/2,0])*scala).tolist()


cer_int=R([2,3])(PI/2)(PROD([STRUCT(MKPOLS((W,FV))),Q(2)]))
CERCHIO=T([1,2,3])([12.181106137187708/2,1,40.55])(cer_int)
FV_SI=[0,4,1]
buchi = STRUCT(MKPOLS([W,[FV[k] for k in FV_SI]]))
buchiPROD=R([2,3])(PI/2)(PROD([buchi,Q(2)])) 
buco1=T([1,2,3])([12.181106137187708/2,1,22])(buchiPROD)
buco2=T([1,2,3])([12.181106137187708/2,1,10])(buchiPROD)
BUCHI=STRUCT([buco1,buco2,CERCHIO])
PARETE_FRONT=DIFFERENCE([parete_front,BUCHI])

parete_lat=CUBOID([11.454996767937942,0.3,46])
fin=T([1,2,3])([3,-1,8])(CUBOID([6,2,4]))
fin2=T([1,2,3])([3,-1,14])(CUBOID([6,2,4]))
fin3=T([1,2,3])([3,-1,19])(CUBOID([6,2,1.5]))
fin4=T([1,2,3])([3,-1,22])(CUBOID([6,2,1.5]))
FIN=STRUCT([fin,fin2,fin3,fin4])
PARETE_LAT=DIFFERENCE([parete_lat,FIN])

#VIEW(STRUCT([PARETE_FRONT,PARETE_LAT]))
#ATAN((W[105][1]-W[106][1])/(W[105][0]-W[106][0])):-0.39411468237339375
#W[26]:[59.092753716871364, 32.25272139625081]
#W[23]:[69.20727213962509, 22.148358112475762]
#W[48]: [69.20727213962509, 7.860077569489337]
#W[122]: [59.092753716871364, -2.2442857142857155]
#W[12]: [44.80447317388494, -2.2442857142857155]
#W[86]: [34.70010989010989, 7.860077569489337]
#W[59]: [34.70010989010989, 22.148358112475762]
#W[25]: [44.80447317388494, 32.25272139625081] 


frontale=T([1,2])([58.17879120879121, 45.53564318034906])(R([1,2])(-0.39411468237339375
)(PARETE_FRONT))
lat1=T([1,2])([58.17879120879121, 34.08064641241113])(R([1,2])(PI/2)(T([2])(-.3)(PARETE_LAT)))
lat2=T([1,2])([61.32688429217841, 32.7706334841629])(R([1,2])(PI/4)(T([1,2])([.22,-.24])(PARETE_LAT)))

"""ROTAZIONE CENTRALE"""
parete= CUBOID([14.059425917919919,0.3,34])

buco_circ= CYLINDER([6,2])(100)
buco=R([2,3])(PI/2)(buco_circ)
cerchio=T([1,2,3])([14.059425917919919/2,.7,23])(buco)
frame=STRUCT(MKPOLS(larDisk(6,PI)([100,1])))
semi_circ= PROD([frame,Q(2)]) 
buco2=R([2,3])(PI/2)(semi_circ)
semi_circ=T([1,2,3])([14.059425917919919/2,.7,9])(buco2)
FORI=STRUCT([cerchio,semi_circ])
PARETE=DIFFERENCE([parete,FORI])
WALL=T([1,2])([59.011512605042014, 50.46088558500324])(R([1,2])(-0.39411468237339375
)(PARETE))
porta=T([1,2,3])([6.2,-1,7.5])(CUBOID([2,2,2.5]))
muro0=T([1,2])([-.1,-.01])(CUBOID([14.4,0.3,34]))
muro=DIFFERENCE([muro0,porta])
wall_int=T([1,2])([71.99993535875889, 45.07866192630899])(R([1,2])(-PI/4)(muro))
ARIA=STRUCT([aria,frontale,lat1,lat2,passo,WALL,wall_int])
aria_alcentro=T([1,2])([-59.092753716871364, -32.25272139625081])(ARIA)
aria2=T([1,2])([69.20727213962509, 22.148358112475762])(R([1,2])(-PI/4)(aria_alcentro))
aria3=T([1,2])([69.20727213962509, 7.860077569489337])(R([1,2])(-PI/2)(aria_alcentro))
aria4=T([1,2])([59.092753716871364, -2.2442857142857155])(R([1,2])(-3*PI/4)(aria_alcentro))
aria5=T([1,2])([44.80447317388494, -2.2442857142857155])(R([1,2])(-PI)(aria_alcentro))
aria6=T([1,2])([34.70010989010989, 7.860077569489337])(R([1,2])(-5*PI/4)(aria_alcentro))
aria7=T([1,2])([34.70010989010989, 22.148358112475762])(R([1,2])(-3*PI/2)(aria_alcentro))
aria8=T([1,2])([44.80447317388494, 32.25272139625081])(R([1,2])(-7*PI/4)(aria_alcentro))
COLONNE=STRUCT([ARIA,aria2,aria3,aria4,aria5,aria6,aria7,aria8])
VIEW(STRUCT([COLONNE,mappa,wall_int]))

"""ingresso alla sala"""
#W[108]: [44.80447317388494, 32.25272139625081]
#W[22]: [59.092753716871364, 32.25272139625081]
#W[23]: [69.20727213962509, 22.148358112475762]
#W[92]: [69.20727213962509, 7.860077569489337]
#W[93]: [59.092753716871364, -2.2442857142857155]
#W[91]: [34.70010989010989, 7.860077569489337]
#W[90]: [44.80447317388494, -2.2442857142857155]
#W[107]: [34.70010989010989, 22.148358112475762]
"trave"
V=[[0,0],[1,0],[0,1]]
FV=[[0,1,2]]
triangle=STRUCT(MKPOLS((V,FV)))
triangle=PROD([triangle,Q(14.296910166001808)])
trave=T([2,3])([1.2,16.2])(S([2,3])([-1,-1])(R([1,3])(-PI/2)(triangle)))
#VIEW(STRUCT([trave,ING_PRES,ING,COLONNE]))
"pareti"
par_int=CUBOID([14.296910166001808,1,10.5])
porta1=T([2,3])([-.7,7.5])(CUBOID([1.5,2,2.5]))
porta2=T([1,2,3])([14.296910166001808-1.5,-.7,7.5])(CUBOID([1.5,2,2.5]))
porte=STRUCT([porta1,porta2])
ingr_sala0=DIFFERENCE([par_int,porte])
par_sup=T(3)(19.5)(CUBOID([14.296910166001808,1,14.5]))
ingr_sala=STRUCT([trave,ingr_sala0,par_sup])
ING_sala=T([1,2])([44.80447317388494, 32.25272139625081])(ingr_sala)
ing2=T([1,2])([59.092753716871364, 32.25272139625081])(R([1,2])(-PI/4)(ingr_sala))
ing3=T([1,2])([69.20727213962509, 22.148358112475762])(R([1,2])(-PI/2)(ingr_sala))
ing4=T([1,2])([69.20727213962509, 7.860077569489337])(R([1,2])(-3*PI/4)(ingr_sala))
ing5=T([1,2])([59.092753716871364, -2.2442857142857155])(R([1,2])(-PI)(ingr_sala))
sup6=T([1,2])([44.80447317388494, -2.2442857142857155])(R([1,2])(-5*PI/4)(STRUCT([trave,par_sup])))
sup8=T([1,2])([34.70010989010989, 22.148358112475762])(R([1,2])(-7*PI/4)(STRUCT([trave,par_sup])))
ING=STRUCT([ING_sala,ing2,ing3,ing4,ing5,sup6,sup8])

par_pres=CUBOID([14.296910166001808,1,34])
porta_princ=T([1,2,3])([14.296910166001808/2-1,-.7,7.5])(CUBOID([2,2,2.5]))
por1=T([2,3])([-.7,7.5])(CUBOID([1.3,2,2]))
por2=T([1,2,3])([14.296910166001808-1.3,-.7,7.5])(CUBOID([1.3,2,2]))
porte_pres=STRUCT([por1,por2,porta_princ])
ing_pres=DIFFERENCE([par_pres,porte_pres])
ING_PRES=T([1,2])([34.70010989010989, 7.860077569489337])(R([1,2])(PI/2)(ing_pres))
VIEW(STRUCT([ING_PRES,ING,COLONNE]))
"""LEVEL3"""
#PARETE DA BUCARE=SQRT((W[58][0]-W[81][0])**2+(W[58][1]-W[81][1])**2):14.059425917919919
#da traslare qui=W[40]:[59.011512605042014, 50.46088558500324]
#parete da non bucare=SQRT((W[4][0]-W[5][0])**2+(W[4][1]-W[5][1])**2): 14.059943030716752
#da traslare qui=W[4]: [71.99993535875889, 45.07866192630899]
#SQRT((W[22][0]-W[23][0])**2+(W[22][1]-W[23][1])**2): 14.296910166001808
#INGR_SALA=W[108]: [44.80447317388494, 32.25272139625081]

lines = lines2lines("centro_level3.lines")
grafo = STRUCT(AA(POLYLINE)(lines))

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.5))

#V[0] da portare nell'origine 
#V[51][0]-V[78][0]= 0.3094

scala = 31.42/0.3094

W=((mat(V)-V[0])*scala).tolist()
WW = AA(LIST)(range(len(W)))
submodel = STRUCT(MKPOLS((W,EV)))
mappa=larModelNumbering(1,1,1)(W,[WW,EV,FV],submodel,5)


EV_SI=sorted([56,72,81,10,25,39,42,35,91,26,80,17,94,34,93,86,15,58,84,46,101,78,7,70,28,0,73,1,88,19,11,31,33,5,71,104,102,85,14,76,61,87,24,64,38,4,48,75,20,83,97,13,103,51,59,82,92])
muri_alti0=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_alti0=OFFSET([0.3,0.3])(muri_alti0)
wall_edf=T(3)(7.5)(PROD([muri_alti0,Q(26.5)]))
EV_CORTE=[67,40,98,8,55,66,23,57,2,3,16]
muri_alti=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_CORTE]))
muri_alti=OFFSET([0.3,0.3])(muri_alti)
wall_corte=T(3)(7.5)(PROD([muri_alti,Q(7.5)]))
ESTERNO=STRUCT([wall_corte,wall_edf])
#VIEW(wall_level3)
#VIEW(STRUCT([COLONNE,wall_level3]))
"""
"""LEVEL4"""

lines = lines2lines("centro_level4.lines")
grafo = STRUCT(AA(POLYLINE)(lines))

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[0] da portare nell'origine 
#V[51][0]-V[78][0]= 0.3094

scala = 31.42/0.3094

W=((mat(V)-V[4])*scala).tolist()

muri_alti=STRUCT(MKPOLS((W,EV)))
muri_alti=OFFSET([0.3,0.3])(muri_alti)
wall_level4=T(3)(10.5)(PROD([muri_alti,Q(3)]))
#VIEW(wall_level4)
#VIEW(STRUCT([FOND,wall_level3,wall_level4]))


"""LEVEL5"""

lines = lines2lines("centro_level5.lines")
grafo = STRUCT(AA(POLYLINE)(lines))

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[0] da portare nell'origine 
#V[51][0]-V[78][0]= 0.3094

scala = 31.42/0.3094

W=((mat(V)-V[12])*scala).tolist()

muri_alti=STRUCT(MKPOLS((W,EV)))
muri_alti=OFFSET([0.3,0.3])(muri_alti)
wall_level5=T(3)(13.5)(PROD([muri_alti,Q(3)]))
#VIEW(wall_level5)
#VIEW(STRUCT([FOND,wall_level3,wall_level4,wall_level5]))


"""LEVEL6"""

lines = lines2lines("centro_level6.lines")
grafo = STRUCT(AA(POLYLINE)(lines))

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[0] da portare nell'origine 
#V[51][0]-V[78][0]= 0.3094

scala = 31.42/0.3094

W=((mat(V)-V[10])*scala).tolist()

muri_alti=STRUCT(MKPOLS((W,EV)))
muri_alti=OFFSET([0.3,0.3])(muri_alti)
wall_level6=T(3)(16.5)(PROD([muri_alti,Q(3)]))
#VIEW(wall_level6)
#VIEW(STRUCT([FOND,wall_level3,wall_level4,wall_level5,wall_level6]))



"""LEVEL7 up"""

lines = lines2lines("centro_level7.lines")
grafo = STRUCT(AA(POLYLINE)(lines))

#numerazione vertici e spigoli
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

#V[0] da portare nell'origine 
#V[51][0]-V[78][0]= 0.3094

scala = 31.42/0.3094

W=((mat(V)-V[0])*scala).tolist()

muri_alti=STRUCT(MKPOLS((W,EV)))
muri_alti=OFFSET([0.3,0.3])(muri_alti)
wall_level7=T(3)(19.5)(PROD([muri_alti,Q(14.5)]))
#VIEW(wall_level7)
VIEW(STRUCT([COLONNE,wall_level3,wall_level4,wall_level5,wall_level6,wall_level7]))

"""


VIEW(STRUCT([ING_PRES,ING,COLONNE,ESTERNO]))

