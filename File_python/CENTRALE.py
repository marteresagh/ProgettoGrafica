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
ARIA=STRUCT([aria,frontale,lat1,lat2,passo])
aria_alcentro=T([1,2])([-59.092753716871364, -32.25272139625081])(ARIA)
aria2=T([1,2])([69.20727213962509, 22.148358112475762])(R([1,2])(-PI/4)(aria_alcentro))
aria3=T([1,2])([69.20727213962509, 7.860077569489337])(R([1,2])(-PI/2)(aria_alcentro))
aria4=T([1,2])([59.092753716871364, -2.2442857142857155])(R([1,2])(-3*PI/4)(aria_alcentro))
aria5=T([1,2])([44.80447317388494, -2.2442857142857155])(R([1,2])(-PI)(aria_alcentro))
aria6=T([1,2])([34.70010989010989, 7.860077569489337])(R([1,2])(-5*PI/4)(aria_alcentro))
aria7=T([1,2])([34.70010989010989, 22.148358112475762])(R([1,2])(-3*PI/2)(aria_alcentro))
aria8=T([1,2])([44.80447317388494, 32.25272139625081])(R([1,2])(-7*PI/4)(aria_alcentro))
COLONNE=STRUCT([ARIA,aria2,aria3,aria4,aria5,aria6,aria7,aria8])
VIEW(STRUCT([COLONNE]))


"""LEVEL3"""
#PARETE DA BUCARE=SQRT((W[58][0]-W[81][0])**2+(W[58][1]-W[81][1])**2):86.3369407167611
#da traslare qui=W[40]:[13.455559146735618, 11.790116354234007]
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
EV_NO=sorted([36,37,9,27,77,18,22,6,43,30,53,49])
EV_SI= set(range(len(EV))).difference(EV_NO)
muri_alti=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_alti=OFFSET([0.3,0.3])(muri_alti)
wall_level3=T(3)(7.5)(PROD([muri_alti,Q(3)]))
#VIEW(wall_level3)
#VIEW(STRUCT([FOND,wall_level3]))
"""parete da bucare"""
parete= CUBOID([86.3369407167611,0.3,34])


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
