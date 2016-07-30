#CENTRALE

from larlib import *
from ringhiera import *
from scale import *
from tetto import *
from lampadario import *
from ALLOGGI import *
from INGRESSO_NORD import *
from MENSA import *
from SALA_PREGHIERA import *
from UFFICI import *


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
mappa=larModelNumbering(1,1,1)(W,[WW,EV],submodel,5)


"COLONNE CENTRALI"
#W[171]: [58.17879120879121, 45.53564318034906]
#W[109]:[58.17879120879121, 34.08064641241113]
#W[153]: [61.32688429217841, 32.7706334841629]

"GRIGLIA finestre"
grid=SKEL_1(PROD([Hpc(Grid([3*[2]])),Hpc(Grid([3*[2]]))]))
#SKEL_1(STRUCT(MKPOLS(larCuboids([6,6]))))
gridOFF=OFFSET([0.05,0.05])(grid)
grata=PROD([gridOFF,Q(0.05)])
fin_quad=R([2,3])(PI/2)(grata)
grata1=T([1,2,3])([3,0.15,7.75])(fin_quad)
grata2=T([1,2,3])([3,0.15,13.75])(fin_quad)
#grata3=T([1,2,3])([3,0.15,19.75])(fin_quad)
#grata4=T([1,2,3])([3,0.15,22.75])(fin_quad)

grid_C=SKEL_1(PROD([Hpc(Grid([5*[2]])),Hpc(Grid([5*[2.2]]))]))
#SKEL_1(STRUCT(MKPOLS(larCuboids([10,11]))))
gridOFFC=OFFSET([0.05,0.05])(grid_C)
grataC=PROD([gridOFFC,Q(0.05)])
fin_circ=R([2,3])(PI/2)(grataC)
grataC1=T([1,2,3])([1,0.15,4])(fin_circ)
grataC2=T([1,2,3])([1,0.15,16])(fin_circ)


fin_CIRC=T([1,2])([58.17879120879121, 45.53564318034906])(R([1,2])(-0.39411468237339375
)(STRUCT([grataC1,grataC2])))
GRATA_QUAD=STRUCT([grata1,grata2])

GRATA1=T([1,2])([58.17879120879121, 34.08064641241113])(R([1,2])(PI/2)(T([2])(-.3)(GRATA_QUAD)))
GRATA2=T([1,2])([61.32688429217841, 32.7706334841629])(R([1,2])(PI/4)(T([1,2])([.22,-.24])(GRATA_QUAD)))
grata_alcentro=T([1,2])([-59.092753716871364, -32.25272139625081])(STRUCT([fin_CIRC,GRATA1,GRATA2]))
grata2=T([1,2])([69.20727213962509, 22.148358112475762])(R([1,2])(-PI/4)(grata_alcentro))
grata3=T([1,2])([69.20727213962509, 7.860077569489337])(R([1,2])(-PI/2)(grata_alcentro))
grata4=T([1,2])([59.092753716871364, -2.2442857142857155])(R([1,2])(-3*PI/4)(grata_alcentro))
grata5=T([1,2])([44.80447317388494, -2.2442857142857155])(R([1,2])(-PI)(grata_alcentro))
grata6=T([1,2])([34.70010989010989, 7.860077569489337])(R([1,2])(-5*PI/4)(grata_alcentro))
grata7=T([1,2])([34.70010989010989, 22.148358112475762])(R([1,2])(-3*PI/2)(grata_alcentro))
grata8=T([1,2])([44.80447317388494, 32.25272139625081])(R([1,2])(-7*PI/4)(grata_alcentro))

GRATE=STRUCT([fin_CIRC,GRATA1,GRATA2,grata2,grata3,grata4,grata5,grata6,grata7,grata8])
#VIEW(GRATE)

"PREPARAZIONE DEL PATTERN DA RIPETERE"

"colonne"

EV_si=sorted([54,73,34])
muri_alti=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_si]))
muri_alti=OFFSET([0.3,0.3])(muri_alti)
aria=PROD([muri_alti,Q(46)])
#VIEW(aria)
"entrata"
EV_alti=sorted([220,104,230,109,233,91])
muri=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_alti]))
muri=OFFSET([0.3,0.3])(muri)
passo=T([1,2])([-.12,-.1])(PROD([muri,Q(34)]))
#VIEW(passo)

"parete frontale colonne"
#parete larga=SQRT((W[65][0]-W[171][0])**2+(W[65][1]-W[171][1])**2)=12.181106137187708
#parete laterale=W[182][0]-W[102][0]=11.454996767937942
parete_front1= CUBOID([12.381106137187708,0.3,17])
parete_front2= T(3)(17)(CUBOID([12.381106137187708,0.3,17]))
parete_front3= T(3)(34)(CUBOID([12.381106137187708,0.3,12]))

"buchi tondi parete frontale"
lines = lines2lines("cerchio_centr.lines")
V,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
grafo=STRUCT(MKPOLS((V,EV))) #grafo pulito
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
#VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))
scala=9.5/0.6351
W=((mat(V)-V[43]-[0.6351/2,0])*scala).tolist()

buco=CYLINDER([9.5/2,2.5])(16)
CERCHIO=T([1,2,3])([12.181106137187708/2,1,40.55])(R([2,3])(PI/2)(buco))
FV_SI=[0,4,1]
buchi = STRUCT(MKPOLS([W,[FV[k] for k in FV_SI]]))
buchiPROD=R([2,3])(PI/2)(PROD([buchi,Q(2)])) 
buco1=T([1,2,3])([12.181106137187708/2,1,22])(buchiPROD)
buco2=T([1,2,3])([12.181106137187708/2,1,10])(buchiPROD)
BUCHI=STRUCT([buco1,buco2,CERCHIO])
PARETE_FRONT0=DIFFERENCE([parete_front1,BUCHI])
PARETE_FRONT1=DIFFERENCE([parete_front2,BUCHI])
PARETE_FRONT2=DIFFERENCE([parete_front3,BUCHI])
PARETE_FRONT=STRUCT([PARETE_FRONT0,PARETE_FRONT1,PARETE_FRONT2])

"parete laterale"
parete_lat1=CUBOID([11.454996767937942,0.3,7.5])
parete_lat2=T(3)(7.5)(CUBOID([3,0.3,46-7.5]))
parete_lat3=T([1,3])([9,7.5])(CUBOID([11.454996767937942-9,0.3,46-7.5]))
parete_lat4=T([1,3])([3,25.25])(CUBOID([6,0.3,46-25.25]))
parete_lat5=T([1,3])([3,13.75])(CUBOID([6,0.3,0.5]))
parete_lat6=T([1,3])([3,19.75])(CUBOID([6,0.3,0.5]))
parete_lat7=T([1,3])([3,22.75])(CUBOID([6,0.3,0.5]))
PARETE_LAT=STRUCT([parete_lat1,parete_lat2,parete_lat3,parete_lat4,parete_lat5,parete_lat6,parete_lat7])
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

"posizionamento dei pezzi per le colonne centrali"
frontale=T([1,2])([58.17879120879121, 45.53564318034906])(R([1,2])(-0.39411468237339375
)(PARETE_FRONT))
lat1=T([1,2])([58.17879120879121, 34.08064641241113])(R([1,2])(PI/2)(T([2])(-.3)(PARETE_LAT)))
lat2=T([1,2])([61.32688429217841, 32.7706334841629])(R([1,2])(PI/4)(T([1,2])([.22,-.24])(PARETE_LAT)))

"parete secondo cerchio"
parete1= T(3)(9)(CUBOID([14.059425917919919,0.3,4]))
parete2= T(3)(13)(CUBOID([14.059425917919919,0.3,34-13]))
parete3= CUBOID([14.059425917919919,0.3,9])
buco_circ= CYLINDER([6,2])(16)
buco=R([2,3])(PI/2)(buco_circ)
cerchio=T([1,2,3])([14.059425917919919/2,.7,23])(buco)
frame=STRUCT(MKPOLS(larDisk(6,PI)([8,1])))
semi_circ= PROD([frame,Q(2)]) 
buco2=R([2,3])(PI/2)(semi_circ)
semi_circ=T([1,2,3])([14.059425917919919/2,.7,9])(buco2)
FORI=STRUCT([cerchio,semi_circ])
PARETE1=DIFFERENCE([parete1,FORI])
PARETE2=DIFFERENCE([parete2,FORI])
PARETE=STRUCT([PARETE1,PARETE2,parete3])

#posizione della parete
WALL=T([1,2])([59.011512605042014, 50.46088558500324])(R([1,2])(-0.39411468237339375
)(PARETE))

#W[106]: [62.97709437621203, 34.40053329023918]
#W[107]: [71.50233354880413, 25.707734324499036]
#W[153]: [61.32688429217841, 32.7706334841629]
#tetto=SQRT((W[106][0]-W[107][0])**2+(W[106][1]-W[107][1])**2): 12.175568028173133
#SQRT((W[23][0]-W[26][0])**2+(W[26][1]-W[23][1])**2): 14.296910166001808

"travi decoro del tetto"
tetto0=T([1,2,3])([62.97709437621203, 34.40053329023918,34])(R([1,2])(-PI/4)(CUBOID([12.175568028173133,0.3,12])))
tetto1=T([1,2,3])([59.092753716871364, 32.25272139625081,43])(R([1,2])(-PI/4)(CUBOID([14.296910166001808,0.3,3])))
tetto2=T([1,2,3])([59.092753716871364, 32.25272139625081,40])(R([1,2])(-PI/4)(CUBOID([14.296910166001808,0.3,1])))
tetto3=T([1,2,3])([75, 8.794350355526827,43])(CUBOID([1,12.186166774402075,3]))
tetto=STRUCT([tetto0,tetto1,tetto2,tetto3])

"ROTAZIONE CENTRALE"

ARIA=STRUCT([tetto,aria,frontale,lat1,lat2,passo,WALL])
aria_alcentro=T([1,2])([-59.092753716871364, -32.25272139625081])(ARIA)
aria2=T([1,2])([69.20727213962509, 22.148358112475762])(R([1,2])(-PI/4)(aria_alcentro))
aria3=T([1,2])([69.20727213962509, 7.860077569489337])(R([1,2])(-PI/2)(aria_alcentro))
aria4=T([1,2])([59.092753716871364, -2.2442857142857155])(R([1,2])(-3*PI/4)(aria_alcentro))
aria5=T([1,2])([44.80447317388494, -2.2442857142857155])(R([1,2])(-PI)(aria_alcentro))
aria6=T([1,2])([34.70010989010989, 7.860077569489337])(R([1,2])(-5*PI/4)(aria_alcentro))
aria7=T([1,2])([34.70010989010989, 22.148358112475762])(R([1,2])(-3*PI/2)(aria_alcentro))
aria8=T([1,2])([44.80447317388494, 32.25272139625081])(R([1,2])(-7*PI/4)(aria_alcentro))
COLONNE=STRUCT([ARIA,aria2,aria3,aria4,aria5,aria6,aria7,aria8])

#VIEW(COLONNE)
"parete terzo cerchio"
muro0=T([1,2])([-.1,-.01])(CUBOID([14.4,0.3,7.5]))
muro1=T([1,2,3])([-.1,-.01,7.5])(CUBOID([6.2,0.3,2.5]))
muro2=T([1,2,3])([-.1+8.2,-.01,7.5])(CUBOID([14.4-8.2,0.3,2.5]))
muro3=T([1,2,3])([-.1,-.01,10])(CUBOID([14.4,0.3,24]))
muro=STRUCT([muro0,muro1,muro2,muro3])
wall_int=T([1,2])([71.99993535875889, 45.07866192630899])(R([1,2])(-PI/4)(muro))
wall_alcentro=T([1,2])([-59.092753716871364, -32.25272139625081])(wall_int)
wall2=T([1,2])([69.20727213962509, 22.148358112475762])(R([1,2])(-PI/4)(wall_alcentro))
wall3=T([1,2])([69.20727213962509, 7.860077569489337])(R([1,2])(-PI/2)(wall_alcentro))
wall5=T([1,2])([44.80447317388494, -2.2442857142857155])(R([1,2])(-PI)(wall_alcentro))
wall6=T([1,2])([34.70010989010989, 7.860077569489337])(R([1,2])(-5*PI/4)(wall_alcentro))
wall7=T([1,2])([34.70010989010989, 22.148358112475762])(R([1,2])(-3*PI/2)(wall_alcentro))
wall8=T([1,2])([44.80447317388494, 32.25272139625081])(R([1,2])(-7*PI/4)(wall_alcentro))
apertura=T([1,2,3])([44.7, -20.7,16.5])(CUBOID([14.5,0.3,17.5]))
WAY=STRUCT([wall_int,wall2,wall3,apertura,wall5,wall6,wall7,wall8])

"""INTERNO CAMERA ASSEMBLEA"""
#W[108]: [44.80447317388494, 32.25272139625081]
#W[22]: [59.092753716871364, 32.25272139625081]
#W[23]: [69.20727213962509, 22.148358112475762]
#W[92]: [69.20727213962509, 7.860077569489337]
#W[93]: [59.092753716871364, -2.2442857142857155]
#W[91]: [34.70010989010989, 7.860077569489337]
#W[90]: [44.80447317388494, -2.2442857142857155]
#W[107]: [34.70010989010989, 22.148358112475762]

"trave sul pavimento della postazione radio"
V=[[0,0],[1,0],[0,1]]
FV=[[0,1,2]]
triangle=STRUCT(MKPOLS((V,FV)))
triangle=PROD([triangle,Q(14.296910166001808)])
trave0=T([2,3])([1.2,14.5])(S([2,3])([-1,-1])(R([1,3])(-PI/2)(triangle)))
pil=STRUCT(NN(5)([T([1,2,3])([1,1.2,15])(CUBOID([0.05,0.05,3])),T(1)(3)]))
PAV=T([2,3])([1.2,14.5])(CUBOID([14.29,6,0.5]))
trave=STRUCT([trave0,pil])

"pareti delimitanti la camera"
par_int1=CUBOID([14.296910166001808,1.4,7.5])
par_int2=T([1,3])([1.5,7.5])(CUBOID([14.296910166001808-3,1.4,2.5]))
par_int3=T(3)(10)(CUBOID([14.296910166001808,1.4,.5]))
ingr_sala0=STRUCT([par_int1,par_int2,par_int3])
par_sup=T(3)(18)(CUBOID([14.296910166001808,1,16]))
ingr_sala=STRUCT([trave,ingr_sala0,par_sup])
ING_sala=T([1,2])([44.80447317388494, 32.25272139625081])(ingr_sala)
ing2=T([1,2])([59.092753716871364, 32.25272139625081])(R([1,2])(-PI/4)(ingr_sala))
ing3=T([1,2])([69.20727213962509, 22.148358112475762])(R([1,2])(-PI/2)(ingr_sala))
ing4=T([1,2])([69.20727213962509, 7.860077569489337])(R([1,2])(-3*PI/4)(ingr_sala))
ing5=T([1,2])([59.092753716871364, -2.2442857142857155])(R([1,2])(-PI)(ingr_sala))
sup6=T([1,2])([44.80447317388494, -2.2442857142857155])(R([1,2])(-5*PI/4)(STRUCT([trave,par_sup])))
sup8=T([1,2])([34.70010989010989, 22.148358112475762])(R([1,2])(-7*PI/4)(STRUCT([trave,par_sup])))
ING=STRUCT([ING_sala,ing2,ing3,ing4,ing5,sup6,sup8])
#VIEW(ING)

par_pres1=CUBOID([14.296910166001808,1.4,8.6])
par_pres3=T([1,3])([1.3,8.6])(CUBOID([14.296910166001808-1.3-14.296910166001808/2-1.5,1.4,2]))
par_pres4=T([1,3])([14.296910166001808/2+1.5,8.6])(CUBOID([14.296910166001808-1.3-14.296910166001808/2-1.5,1.4,2]))
par_pres5=T([3])([10.6])(CUBOID([14.296910166001808/2-1.5,1.4,1.6]))
par_pres6=T([1,3])([14.296910166001808/2+1.5,10.6])(CUBOID([14.296910166001808/2-1.5,1.4,1.6]))
par_pres7=T([3])([12.2])(CUBOID([14.296910166001808,1.4,21.8]))
ing_pres=STRUCT([par_pres1,par_pres3,par_pres4,par_pres5,par_pres6,par_pres7])
ING_PRES=T([1,2])([34.70010989010989, 7.860077569489337])(R([1,2])(PI/2)(ing_pres))
#VIEW(STRUCT([ING_PRES,ING]))

#VIEW(STRUCT([ING_PRES,ING,COLONNE,WAY]))


"""LEVEL3"""
"ALTRE STRUTTURE"
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
mappa=larModelNumbering(1,1,1)(W,[WW,EV],submodel,5)


EV_SI=sorted([20,51,59,92])
muri_alti0=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_SI]))
muri_alti0=OFFSET([0.3,0.3])(muri_alti0)
wall_edf=T(3)(7.5)(PROD([muri_alti0,Q(26.5)]))
EV_CORTE=[67,40,98,8,55,66,23,57,2,3,16]
muri_alti=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_CORTE]))
muri_alti=OFFSET([0.3,0.3])(muri_alti)
wall_corte=T(3)(7.5)(PROD([muri_alti,Q(7.5)]))
muro1=CUBOID([19.84314156431803,0.3,4.5])
muro2=T(3)(4.5)(CUBOID([7,0.3,3]))
muro3=T([1,3])([19.84314156431803-7,4.5])(CUBOID([7,0.3,3]))
muro=T([1,2,3])([42.021965093729804, -27.53058177117001,7.5])(STRUCT([muro1,muro2,muro3]))
ESTERNO=STRUCT([wall_corte,wall_edf,muro])

"muro ovest"
#W[44][1]-W[46][1]: 7.860077569489338
#W[46][0]-W[57][0]: -3.1785585003232075

EV_OVEST=[15,84,101,7,24,87,61,64]
muri_ovest=STRUCT(AA(POLYLINE)([[W[EV[e][0]],W[EV[e][1]]] for e in EV_OVEST]))
muri_ovest=OFFSET([0.3,0.3])(muri_ovest)
wall_ovest=PROD([muri_ovest,Q(34)])

"balconi"
part1=CUBOID([0.3,7.860077569489338/3,34])
part2=T(2)(2*7.860077569489338/3)(CUBOID([0.3,7.860077569489338/3,34]))
rail_ovest1=STRUCT([CUBOID([0.3,7.860077569489338/3,0.5])])
travi=STRUCT(NN(7)([T([2,3])([7.860077569489338/3,10])(rail_ovest1),T(3)(3)]))
muro_top=T([2,3])([7.860077569489338/3,31])(CUBOID([0.3,7.860077569489338/3,3]))
rail_ovest2=STRUCT([CUBOID([3.1785585003232075,0.3,0.5])])
travi2=STRUCT(NN(7)([T(3)(10)(rail_ovest2),T(3)(3)]))
muro_top2=T(3)(31)(CUBOID([3.1,0.3,3]))
parete=STRUCT(NN(2)([T(2)(7.860077569489338/3+0.3),T(2)(-0.6)(S(1)(-1)(CUBOID([6.34,0.3,34])))]))
pareteOVEST=T([1,2])([13.455559146735618, 22.138202973497094])(STRUCT([muro_top,travi,part1,part2,travi2,muro_top2,parete]))
WALL_OVEST=STRUCT([wall_ovest,pareteOVEST])
pareteOVEST2=T(2)(29.998280542986432/2)(S(2)(-1)(T(2)(-29.998280542986432/2)(WALL_OVEST)))

"RINGHIERE BALCONI"
"RINGHIERE OVEST"
#W[44][1]-W[46][1]: 7.860077569489338
#W[46][0]-W[57][0]: -3.1785585003232075

rail_ovest1=STRUCT([T([1,3])([0.15,.5])(R([1,2])(PI/2)(ringhiera(12)))])
travi=STRUCT(NN(7)([T([2,3])([7.860077569489338/3,10])(rail_ovest1),T(3)(3)]))
rail_ovest2=STRUCT([T([1,2,3])([0.15,0.15,.5])(ringhiera(13))])
travi2=STRUCT(NN(7)([T(3)(10)(rail_ovest2),T(3)(3)]))
pareteOVEST=T([1,2])([13.455559146735618, 22.138202973497094])(STRUCT([travi,travi2]))
RAIL_OVEST=STRUCT([pareteOVEST])
RAIL_OVEST2=T(2)(29.998280542986432/2)(S(2)(-1)(T(2)(-29.998280542986432/2)(RAIL_OVEST)))

"RINGHIERE EST"
rail_ovest1=STRUCT([T([1,3])([0.15,.5])(R([1,2])(PI/2)(ringhiera(12)))])
travi=STRUCT(NN(7)([T([2,3])([7.860077569489338/3,10])(rail_ovest1),T(3)(3)]))
rail_ovest2=STRUCT([T([1,2,3])([0.15,0.15,.5])(ringhiera(13))])
travi2=STRUCT(NN(7)([T(3)(10)(rail_ovest2),T(3)(3)]))
a=S(1)(-1)(STRUCT([travi,travi2]))

railEST1=T([1,2])([90.6,22.1])(STRUCT([a]))
railEST2=T([1,2])([90.6,8])(S(2)(-1)(STRUCT([a])))

rin1=STRUCT(NN(4)([T([1,2,3])([97, 0,10.5])(R([1,2])(PI/2)(ringhiera(3))),T(3)(6)]))
rin2=STRUCT(NN(4)([T([1,2,3])([95.75, 30.5,10.5])(R([1,2])(-PI/2)(ringhiera(4))),T(3)(6)]))

railEST_OVEST=STRUCT([rin1,rin2,RAIL_OVEST,RAIL_OVEST2,railEST1,railEST2])

"muri est"
part1=CUBOID([0.3,7.860077569489338/3,34])
part2=T(2)(2*7.860077569489338/3)(CUBOID([0.3,7.860077569489338/3,34]))
rail_ovest1=STRUCT([CUBOID([0.3,7.860077569489338/3,0.5])])
travi=STRUCT(NN(7)([T([2,3])([7.860077569489338/3,10])(rail_ovest1),T(3)(3)]))
muro_top=T([2,3])([7.860077569489338/3,31])(CUBOID([0.3,7.860077569489338/3,3]))
rail_ovest2=STRUCT([CUBOID([3.1785585003232075,0.3,0.5])])
travi2=STRUCT(NN(7)([T(3)(10)(rail_ovest2),T(3)(3)]))
muro_top2=T(3)(31)(CUBOID([3.1,0.3,3]))
parete=STRUCT(NN(2)([T(2)(7.860077569489338/3+0.3),T(2)(-0.6)(S(1)(-1)(CUBOID([6.34,0.3,34])))]))
a=S(1)(-1)(STRUCT([muro_top,travi,part1,part2,travi2,muro_top2,parete]))
b=STRUCT(NN(2)([CUBOID([6.34,0.3,34]),T(2)(7.860077569489338-0.3)]))
part01=T(1)(6.34)(CUBOID([0.3,7.860077569489338/3,34]))
part02=T([1,2])([6.34,2*7.860077569489338/3])(CUBOID([0.3,7.860077569489338/3,34]))
pareteEST1=T([1,2])([90.6,22.1])(STRUCT([a,b,part01,part02]))
pareteEST2=T([1,2])([90.6,8])(S(2)(-1)(STRUCT([a,b,part01,part02])))

#VIEW(STRUCT([pareteOVEST2,pareteEST2]))

"muro nord"
rail_nord1=T([1,2,3])([45, 53.99487394957984,13.5])(R([1,2])(-PI/2)(ringhiera(16)))
rail_nord2=T([1,2,3])([59.1, 53.99487394957984,13.5])(R([1,2])(-PI/2)(ringhiera(16)))
wall_nord=T([1,2,3])([44.9466451195863, 53.99487394957984])(CUBOID([14.064867485455714,0.3,34]))
rail_NORD=STRUCT([rail_nord1,rail_nord2])


"STRUTTURE EST E OVEST"
EST_OVEST=STRUCT([pareteEST1,pareteEST2,pareteOVEST2,WALL_OVEST])

"CORRIDOIO ESTERNO"
#W[6],W[68]:SQRT((W[6][0]-W[68][0])**2+(W[6][1]-W[68][1])**2)=43.20811153293262
#W[99],W[75]:SQRT((W[99][0]-W[75][0])**2+(W[99][1]-W[75][1])**2)=42.747549408870746
#W[33],W[34]:SQRT((W[33][0]-W[34][0])**2+(W[33][1]-W[34][1])**2)=43.357941172843034
#W[42],W[69]:SQRT((W[42][0]-W[69][0])**2+(W[42][1]-W[69][1])**2)=42.440380341310124
"facciata degli uffici"
lines = lines2lines("facciata_uff.lines")
V,FV,EV,polygons = larFromLines(lines) 
"""
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))
"""
scala = 34/0.8114
W=((mat(V)-V[181])*scala).tolist()
FV_NO=[7,4,2,5,1,3,6]
buchi = STRUCT(MKPOLS([W,[FV[k] for k in FV_NO]]))
tot=STRUCT(MKPOLS((W,FV)))
frame=DIFFERENCE([tot,buchi])
muro_uff=PROD([frame,Q(0.3)])
wall_uff=T(1)((41.90288390436283-38)/2)(S(1)(38/41.90288390436283)(R([2,3])(PI/2)(muro_uff)))

#VIEW(wall_uff)

wall1=T([1,2])([7.108597285067875, 0.0])(R([1,2])(-PI/4)(wall_uff))
wall2=T([1,2])([7.108597285067875, 29.998280542986432])(R([1,2])(PI/4)(wall_uff))
wall3=T([1,2])([66.26228183581125, 60.30121525533292])(R([1,2])(-PI/4)(wall_uff))
wall4=T([1,2])([97.06281835811248, -0.21325791855203527])(R([1,2])(-3*PI/4)(wall_uff))
facciate_uff=STRUCT([wall2,wall3,wall4,wall1])
#VIEW(STRUCT([facciate_uff,ING_PRES,ING,COLONNE]))

STRUTTURA=STRUCT([ING_PRES,ING,COLONNE,ESTERNO,WAY,facciate_uff,wall_nord,EST_OVEST])

"RINGHIERE sulla parete degli uffici"
ringhiera0=T(3)(10.5)(ringhiera(9))
rip_ring=T(2)(-0.15)(STRUCT(NN(4)([ringhiera0,T(3)(6)])))
rip_ring2=T(1)(41.90288390436283-(41.90288390436283-38)/2)(rip_ring)
#VIEW(rip_ring)

ring_uff=STRUCT([rip_ring,rip_ring2])
ring1=T([1,2])([7.108597285067875, 0.0])(R([1,2])(-PI/4)(ring_uff))
ring2=T([1,2])([7.108597285067875, 29.998280542986432])(R([1,2])(PI/4)(ring_uff))
ring3=T([1,2])([66.26228183581125, 60.30121525533292])(R([1,2])(-PI/4)(ring_uff))
ring4=T([1,2])([97.06281835811248, -0.21325791855203527])(R([1,2])(-3*PI/4)(ring_uff))
ringhiere_uff=STRUCT([ring2,ring3,ring4,ring1])


"RINGHIERE A SUD SULLA CORTE"
ringh_sala=T([1,2,3])([36.65, -29.687,22.5])(ringhiera(17))
ringh_sala2=T([1,2,3])([36.65, -29.687,28.5])(ringhiera(17))
ringh_sala3=T([1,2,3])([40.3, -29.8,22.5])(R([1,2])(-PI/2)(ringhiera(14)))
ringh_sala4=T([1,2,3])([40.3, -29.8,28.5])(R([1,2])(-PI/2)(ringhiera(14)))
ringh_SALA=STRUCT([ringh_sala,ringh_sala2,ringh_sala3,ringh_sala4])
ringh_SALA2=T(1)(51.6)(S(1)(-1)(T(1)(-52.30912087912088)(ringh_SALA)))
ring01=T([1,2,3])([36.6, -29.8,16.5])(R([1,2])(-3*PI/4)(ringhiera(17)))
ring02=T([1,2,3])([36.6, -29.8,10.5])(R([1,2])(-3*PI/4)(ringhiera(17)))
ring03=T(1)(51.65)(S(1)(-1)(T(1)(-52.30912087912088)(STRUCT([ring01,ring02]))))
ringhiere_sud=STRUCT([ring01,ring02,ring03,ringh_SALA,ringh_SALA2])

#VIEW(STRUCT([ringhiere_sud,ING_PRES,ING,COLONNE,ESTERNO,WAY,facciate_uff,EST_OVEST]))

"PAVIMENTI"

"level3"

lines = lines2lines("centrale_pav3.lines")
Y,FV,EV,polygons = larFromLines(lines) 
#prova=STRUCT(MKPOLS((Y,FV))) 
#VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
#VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))

#Y[67]=[0.0147, 0.3803]
#Y[65][0]-Y[64][0]=0.29929999999999995

scala = 31.42/0.29929999999999995
Z=((mat(Y)-Y[67])*scala).tolist()

"""
ZZ = AA(LIST)(range(len(Z)))
submodel = STRUCT(MKPOLS((Z,EV)))
MAPPA=larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,10)
"""

#celle vuote
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [0,1,2,3,13,14,15,16,17,18,19,20,21]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level3= DIFFERENCE([tot,buchi])
pavimento_level3=T(3)(7.2)(PROD([frame_level3,Q(0.3)]))
top=T(3)(32)(PROD([frame_level3,Q(0.3)]))

#VIEW(STRUCT([pavimento_level3,top]))

"level4 e 5"
"CORRIDOI ESTERNI PIANO 4 E 5"
lines = lines2lines("centrale_pav5.lines")
Y,FV,EV,polygons = larFromLines(lines) 
#prova=STRUCT(MKPOLS((Y,FV))) 
#VIEW(prova)
"""
YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))
"""
#assert Y[10]==[0.0256, 0.3872]
#Y[32][0]-Y[42][0]=0.2963
scala = 31.42/0.2963
Z=((mat(Y)-Y[10])*scala).tolist()
"""
ZZ = AA(LIST)(range(len(Z)))
submodel = STRUCT(MKPOLS((Z,EV)))
MAPPA=larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,10)
"""
#celle vuote
FV[17]=[25,33,43,37,36,39,24,20]
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [1,2,12,13,7,6,17,3,4,14,8,5]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level5= DIFFERENCE([tot,buchi])
pavimento_level4=T(3)(10.2)(PROD([frame_level5,Q(0.3)]))
pavimento_level5=T(3)(16.2)(PROD([frame_level5,Q(0.3)]))
"PAVIMENTI BALCONI"
balcone0=T([1,2,3])([87.5, 7.85,10.2])(CUBOID([3.075194060074253,14.453412082348969,0.3]))
rip_balcone1=STRUCT(NN(7)([balcone0,T(3)(3)]))
balcone1=T([1,2,3])([13.2, 7.8,10.2])(CUBOID([3.075194060074253,14.453412082348969,0.3]))
rip_balcone2=STRUCT(NN(7)([balcone1,T(3)(3)]))

balcone2=T([1,2,3])([90.4, 2,10.2])(CUBOID([6.2,5,0.3]))
balcone02=T([1,2,3])([90.4, 23,10.2])(CUBOID([6.2,5,0.3]))
rip_balcone3=STRUCT(NN(7)([STRUCT([balcone2,balcone02]),T(3)(3)]))

balcone3=T([1,2,3])([7.4, 2,10.2])(CUBOID([6.2,5,0.3]))
balcone03=T([1,2,3])([7.4, 23,10.2])(CUBOID([6.2,5,0.3]))
rip_balcone4=STRUCT(NN(7)([STRUCT([balcone3,balcone03]),T(3)(3)]))

balcone5=T([1,2,3])([44.8, 50.5,13.2])(CUBOID([14.45,3.7,0.3]))


balconi=STRUCT([rip_balcone1,rip_balcone2,rip_balcone3,rip_balcone4,balcone5])
#VIEW(balconi)

"level8 e 10"
"corridoi piani 8 e 10"
lines = lines2lines("centrale_pav8.lines")
Y,FV,EV,polygons = larFromLines(lines) 
#prova=STRUCT(MKPOLS((Y,FV))) 
#VIEW(prova)
"""
YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))
"""
#assert Y[43]==[0.009, 0.3767]
#Y[7][0]-Y[8][0]=0.30139999999999995
scala = 31.42/0.30139999999999995
Z=((mat(Y)-Y[43])*scala).tolist()
"""
ZZ = AA(LIST)(range(len(Z)))
submodel = STRUCT(MKPOLS((Z,EV)))
MAPPA=larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,10)
"""
#**celle vuote**
FV[0]=[17,9,3,26,25,38,37,16]
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [1,2,6,7,11,12,13,3,4,5,8,0]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame_level8= DIFFERENCE([tot,buchi])
pavimento_level8=T(3)(22.2)(PROD([frame_level8,Q(0.3)]))
PAV8_10=STRUCT(NN(2)([pavimento_level8,T(3)(6)]))
PAVIMENTI0=T(1)(-0.3)(STRUCT([pavimento_level3,pavimento_level4,PAV8_10,pavimento_level5]))

"PAVIMENTO CORTE" 
lines = lines2lines("pav_corte.lines")
Y,FV,EV,polygons = larFromLines(lines) #taglia le parti di troppo
prova=STRUCT(MKPOLS((Y,FV))) #grafo pulito
#VIEW(prova)

"""
YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))
"""

#assert Y[25]==[0.0, 0.5928]
#Y[65][0]-Y[64][0] 
scala = 19.84314156431803/0.6355999999999999
Z=((mat(Y)-Y[23])*scala).tolist()
"""
ZZ = AA(LIST)(range(len(Z)))
submodel = STRUCT(MKPOLS((Z,EV)))
MAPPA=larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,10)
"""

#celle vuote

buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [0,1]]]))
tot = STRUCT(MKPOLS([Z,FV]))
frame= DIFFERENCE([tot,buchi])
pav_corte=T([1,2,3])([42.2, -27.1,13.25])(PROD([frame,Q(0.3)]))



"RINGHIERE CORTE"

corrimano=T([1,2,3])([52.1, -33,13.25])(ringhiera_circle(156,14,0.02))
corrimano2=T([1,2,3])([43.53, -27.53058177117001-5.19082740788623,13.5])(R([1,2])(PI/2)(ringhiera(13)))
corrimano3=T([1,2,3])([60.5, -27.53058177117001-5.19082740788623,13.5])(R([1,2])(PI/2)(ringhiera(13)))

CORRIMANO=STRUCT([corrimano,corrimano3,corrimano2])

"SCALE"
scale=T([1,2,3])([33.8, 7.860077569489337,8.3])(S(1)(-1)(createSteps(7,[0.28, 14.288280542986424,0.14])))
scale2=T([1,2,3])([35.7, 13.5,8.3+0.15*3])(S(1)(-1)(createFilledSteps(3,[0.37, 3,0.15])))

scala_corte1=T([1,2,3])([42.021965093729804+19.84314156431803-7, -27.53058177117001-5.29082740788623,10.4])(createSteps(20,[0.28,5.29082740788623/2,0.15],full=True,rail=False))
scala_corte2=T([1,2,3])([42.021965093729804+7, -27.53058177117001-5.29082740788623,10.4])(S(1)(-1)(createSteps(20,[0.27,5.29082740788623/2,0.15],full=True,rail=False)))
scala_corte3=T([1,2,3])([42.021965093729804+1.6, -27.53058177117001-5.29082740788623/2,13.4])(createSteps(20,[0.27,5.29082740788623/2,0.15],full=True,rail=False))
scala_corte4=T([1,2,3])([42.221965093729804+19.84314156431803-1.6, -27.53058177117001-5.29082740788623/2,13.4])(S(1)(-1)(createSteps(20,[0.28,5.29082740788623/2,0.15],full=True,rail=False)))

SCALE_pietra=STRUCT([scale,scala_corte1,scala_corte2,scala_corte3,scala_corte4])


ring1=T([1,2,3])([42.021965093729804+19.84314156431803-7, -27.53058177117001-5.29082740788623,10.4])(stepsRing(20,[0.28,5.29082740788623/2,0.15]))
ring2=T([1,2,3])([42.021965093729804+7, -27.53058177117001-5.29082740788623,10.4])(S(1)(-1)(stepsRing(20,[0.27,5.29082740788623/2,0.15])))
ring3=T([1,2,3])([42.021965093729804+1.6, -27.53058177117001-5.29082740788623/2,13.4])(stepsRing(20,[0.27,5.29082740788623/2,0.15]))
ring4=T([1,2,3])([42.221965093729804+19.84314156431803-1.6, -27.53058177117001-5.29082740788623/2,13.4])(S(1)(-1)(stepsRing(20,[0.28,5.29082740788623/2,0.15])))

RINGHSTEPS=STRUCT([ring1,ring2,ring3,ring4])

ringh=STRUCT([CORRIMANO,RINGHSTEPS])

pianerottolo=T([1,2,3])([42.021965093729804+7, -27.53058177117001-5.29082740788623,10.4])(CUBOID([5.8431415643180316,5.29082740788623,0.15]))


PAVIMENTI=STRUCT([PAVIMENTI0,top,pav_corte,pianerottolo,balconi])


#VIEW(STRUCT([corrimano,corrimano2,corrimano3,pav_corte,pianerottolo,SCALE_pietra]))
#VIEW(STRUCT([CORRIMANO,pav_corte,pianerottolo,SCALE_pietra,]))

RINGHIERE=STRUCT([ringh,rail_NORD,railEST_OVEST,ringhiere_sud,ringhiere_uff])

#VIEW(STRUCT([STRUTTURA,PAVIMENTI,RINGHIERE,GRATE,SCALE_pietra]))



"CAMERA ASSEMBLEA"

#SQRT((W[59][0]-W[25][0])**2+(W[59][1]-W[25][1])**2)
trib0=T([1,3])([2.05,7.5])(CUBOID([8,0.3,3]))
trib1=T([2,3])([2,7.5])(CUBOID([13,0.3,7.5]))
m=MAT([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,3./2,1]])
trib2=T([1,3])([2.05,4.5])(m(CUBOID([0.3,2,6])))
trib3=T([1,3])([2.05+8,4.5])(m(CUBOID([0.3,2,6])))
trib=STRUCT([trib0,trib1,trib2,trib3])
tri1=T([1,2])([42.84453135100194, -2.9754557207498378])(R([1,2])(-5*PI/4)(trib))
tri2=T([1,2])([34.222818358112484, 24.128610213316094])(R([1,2])(-7*PI/4)(trib))
#VIEW(STRUCT([tri1,tri2,STRUTTURA]))

"pavimento camera assemblea"
lines = lines2lines("pav_chamber.lines")
Y,FV,EV,polygons = larFromLines(lines) 
#prova=STRUCT(MKPOLS((Y,FV))) 
#VIEW(prova)

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
#VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))

#assert Y[81]==[0.285, 0.0826]
#Y[109][1]-Y[55][1]=0.37989999999999996
#misure prese dalla prima mappa
scala = 14.288280542986424/0.37989999999999996
Z=((mat(Y)-Y[81])*scala).tolist()
"""
ZZ = AA(LIST)(range(len(Z)))
submodel = STRUCT(MKPOLS((Z,EV)))
MAPPA=larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,2)
"""
#celle vuote

gradino2 = STRUCT(MKPOLS([Z,[FV[k] for k in [18,9,27,26]]]))
gradino3 = STRUCT(MKPOLS([Z,[FV[k] for k in [17,8]]]))
gradino4 = STRUCT(MKPOLS([Z,[FV[k] for k in [22,10]]]))
gradino5 = STRUCT(MKPOLS([Z,[FV[k] for k in [29,28,0,1,5,3]]]))
gradino6 = STRUCT(MKPOLS([Z,[FV[k] for k in [21,13]]]))
gradino7 = STRUCT(MKPOLS([Z,[FV[k] for k in [20,7]]]))
gradino8 = STRUCT(MKPOLS([Z,[FV[k] for k in [16,6]]]))
gradino9 = STRUCT(MKPOLS([Z,[FV[k] for k in [15,12]]]))
gradino10 = STRUCT(MKPOLS([Z,[FV[k] for k in [19,11]]]))
gradino11 = STRUCT(MKPOLS([Z,[FV[k] for k in [23,14]]]))
gradino12 = STRUCT(MKPOLS([Z,[FV[k] for k in [41,36,37]]]))
gradino13 = STRUCT(MKPOLS([Z,[FV[k] for k in [31,25,24]]]))
gradino14 = STRUCT(MKPOLS([Z,[FV[k] for k in [30,33,2]]]))
gradino15 = STRUCT(MKPOLS([Z,[FV[k] for k in [32]]]))
gradino16 = STRUCT(MKPOLS([Z,[FV[k] for k in [40]]]))
buchi = STRUCT(MKPOLS([Z,[FV[40]]]))
tot = STRUCT(MKPOLS([Z,[FV[34]]]))
gradino17= DIFFERENCE([tot,buchi])
buchi = STRUCT(MKPOLS([Z,[FV[34]]]))
tot = STRUCT(MKPOLS([Z,[FV[35]]]))
gradino18= DIFFERENCE([tot,buchi])
buchi = STRUCT(MKPOLS([Z,[FV[35]]]))
tot = STRUCT(MKPOLS([Z,[FV[38]]]))
gradino19= DIFFERENCE([tot,buchi])
buchi = STRUCT(MKPOLS([Z,[FV[38]]]))
tot = STRUCT(MKPOLS([Z,[FV[39]]]))
gradino20= DIFFERENCE([tot,buchi])

gradino0=T([1,2])([-10.834363936137027, 15.343649558014945])(CUBOID([1.5299361931371482,6.236503060972229,2.1]))
gradino2 = PROD([gradino2,Q(2.1)])
gradino3 = PROD([gradino3,Q(1.95)])
gradino4 = PROD([gradino4,Q(1.8)])
gradino5 = PROD([gradino5,Q(1.65)])
gradino6 = PROD([gradino6,Q(1.5)])
gradino7 = PROD([gradino7,Q(1.35)])
gradino8 = PROD([gradino8,Q(1.2)])
gradino9 = PROD([gradino9,Q(1.05)])
gradino10 = PROD([gradino10,Q(0.9)])
gradino11= PROD([gradino11,Q(0.75)])
gradino12= PROD([STRUCT([gradino12,gradino20]),Q(0.6)])
gradino13= PROD([STRUCT([gradino13,gradino19]),Q(0.45)])
gradino14= PROD([STRUCT([gradino14,gradino18]),Q(0.3)])
gradino15= PROD([STRUCT([gradino15,gradino17]),Q(0.15)])
gradino16= PROD([gradino16,Q(0.01)])

gradini0=STRUCT([gradino2,gradino3,gradino4,gradino5,gradino6,gradino7,gradino8,gradino9,gradino10,gradino11,gradino12,gradino13,gradino14,gradino15,gradino16])

pav_camera=T([1,2,3])([44.80447317388494, -2.2442857142857155,6.9])(gradini0)
#VIEW(STRUCT([STRUTTURA,COLOR(GREEN)(pav_camera)]))

"GRADINATE"
pav=T([1,2,3])([-11,0.2,1.4])(CUBOID([6,12.1,0.5]))
gradinata0=STRUCT([pav,T([1,2,3])([-5,0.2,1.3])(createFilledSteps(4,[1.5, 12.2,3./5]))])
gradinata1=T([1,2])([61.32688429217841, 32.7706334841629])(R([1,2])(-3*PI/4)(gradinata0))
gradinata2=T([1,2])([71.27892049127344, 20.980517129928902])(R([1,2])(-PI)(gradinata0))
gradinata3=T([1,2])([69.94859728506788, 5.666567550096964])(R([1,2])(-5*PI/4)(gradinata0))
gradinata4=T([1,2])([58.158480930833875, -4.305778926955397])(R([1,2])(-3*PI/2)(gradinata0))
gradinata5=T([1,2])([45.982469295410475, 34.08064641241113])(R([1,2])(-PI/2)(gradinata0))

GRADINATA=T(3)(10.5)(STRUCT([gradinata1,gradinata2,gradinata3,gradinata4,gradinata5]))

"pavimento radio"
PAV=T([1,2,3])([1.2,1.2,14.5])(CUBOID([12.3,12,0.5]))
toppa=T([2,3])([-0.1,7.2])(CUBOID([15,3,0.3]))

ING_sala=T([1,2])([44.80447317388494, 32.25272139625081])(PAV)
ing2=T([1,2])([59.092753716871364, 32.25272139625081])(R([1,2])(-PI/4)(PAV))
ing3=T([1,2])([69.20727213962509, 22.148358112475762])(R([1,2])(-PI/2)(PAV))
ing4=T([1,2])([69.20727213962509, 7.860077569489337])(R([1,2])(-3*PI/4)(PAV))
ing5=T([1,2])([59.092753716871364, -2.2442857142857155])(R([1,2])(-PI)(PAV))
sup6=T([1,2])([44.80447317388494, -2.2442857142857155])(R([1,2])(-5*PI/4)(STRUCT([toppa,PAV])))
sup8=T([1,2])([34.70010989010989, 22.148358112475762])(R([1,2])(-7*PI/4)(STRUCT([PAV,toppa])))
PAV_RADIO=STRUCT([ING_sala,ing2,ing3,ing4,ing5,sup6,sup8])
#VIEW(STRUCT([PAV_RADIO,GRADINATA,ING,ING_PRES]))


"TOTALE"
ringh=STRUCT([CORRIMANO,RINGHSTEPS])
PAV_camera=STRUCT([scale2,pav_camera,GRADINATA])
PAVIMENTI=STRUCT([PAVIMENTI0,top,pav_corte,pianerottolo,balconi])
MURA=STRUCT([STRUTTURA,tri1,tri2])
RINGHIERE=STRUCT([ringh,rail_NORD,railEST_OVEST,ringhiere_sud,ringhiere_uff])
SCALE_pietra=STRUCT([scale,scala_corte1,scala_corte2,scala_corte3,scala_corte4])
VIEW(STRUCT([COLOR([0,0.3,0.7])(GRADINATA),PAV_RADIO,COLOR([0.5,0.6,0])(PAV_camera),COLOR([0.6,0.6,0.6])(MURA),PAVIMENTI,COLOR([0.4,0.3,0.3])(RINGHIERE),GRATE,SCALE_pietra,COLOR([0.6,0.6,0.6])(TETTO_CENTRO),lampadario]))

CENTRALE=STRUCT([COLOR([0,0.3,0.7])(GRADINATA),PAV_RADIO,COLOR([0.5,0.6,0])(PAV_camera),COLOR([0.6,0.6,0.6])(MURA),PAVIMENTI,COLOR([0.4,0.3,0.3])(RINGHIERE),GRATE,SCALE_pietra,COLOR([0.6,0.6,0.6])(TETTO_CENTRO),lampadario])
VIEW(STRUCT([CENTRALE,SUD,OVEST,NORD,EST,EDF_UFFICI]))

