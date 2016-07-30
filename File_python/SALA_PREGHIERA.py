#SALA DELLA PREGHIERA
from larlib import *
from scale import *
#BUCHI TONDI
buco_ell= S(1)(0.53)(CYLINDER([7,1.5])(22))
buco=R([1,3])(PI/2)(buco_ell)
circ=COLOR(RED)(T([1,3])([0.8,28])(buco))
buco1=R([1,2])(PI/2)(R([1,3])(PI/2)(buco_ell))
circ1=COLOR(RED)(T([2,3])([0.8,28])(buco1))

#VIEW(STRUCT([circ1,circ]))

frame=R([1,2])(-PI/2)(STRUCT(MKPOLS(larDisk(7,PI)([22,1]))))
buco_circ= S(1)(0.85)(PROD([frame,Q(1.5)])) 
buco2=R([1,3])(PI/2)(buco_circ)
circ2=COLOR(RED)(T([1,3])([.8,14.5])(buco2))
buco3=R([1,2])(PI/2)(R([1,3])(PI/2)(buco_circ))
circ3=COLOR(RED)(T([2,3])([.8,14.5])(buco3))
#VIEW(STRUCT([circ3,circ2]))
BUCHI=STRUCT([circ,circ1,circ2,circ3]) #buchi pilastro

tagli=R([1,2])(PI/2)(BUCHI)
tagli2=T(1)(20.8)(R([1,2])(PI/2)(tagli))
tagli3=T([1,2])([20.8,20.8])(R([1,2])(PI)(tagli))
tagli4=T(2)(20.8)(R([1,2])(-PI/2)(tagli))
apertura_sala=T([1,2,3])([7.7,-.7,13.6])(CUBOID([5.4,2,7.5]))
FORI=STRUCT([apertura_sala,tagli,tagli2,tagli3,tagli4]) #buchi per pareti 


"SALA DELLA PREGHIERA"
base= CUBOID([20.5,20.5])
muri=OFFSET([0.3,0.3])(SKEL_1(base))
pareti=PROD([muri,Q(13.5)])
parete1=T([1,3])([7,13.5])(CUBOID([6.8,0.3,20.5]))
parete1_2=T([1,3])([7+6.8,13.5])(CUBOID([7,0.3,20.5]))
parete1_3=T([3])([13.5])(CUBOID([7,0.3,20.5]))

porta=DIFFERENCE([parete1,FORI])
parete1_b=DIFFERENCE([parete1_2,FORI])
parete2_b=DIFFERENCE([parete1_3,FORI])
parete_b=STRUCT([parete1_b,parete2_b])

parete2=T([2,3])([7,13.5])(CUBOID([0.3,6.8,20.5]))
parete2_1=T(1)(0.3)(R([1,2])(PI/2)(parete_b))
parete3=T([1,2,3])([7,20.5,13.5])(CUBOID([6.8,0.3,20.5]))
parete3_1=T([2])(20.5)(parete_b)
parete4=T([1,2,3])([20.5,7,13.5])(CUBOID([0.3,6.8,20.5]))
parete4_1=T(1)(20.8)(R([1,2])(PI/2)(parete_b))
SALA=STRUCT([pareti,porta,parete_b,parete2,parete2_1,parete3,parete3_1,parete4,parete4_1])
#VIEW(SALA)

"PAV SALA"
pav_sala=T([1,2,3])([0.3,0.3,13.2])(CUBOID([20.5,20.5,0.5]))
soffitto=T([1,2,3])([0.3,0.3,33.5])(CUBOID([20.2,20.2,0.5]))


"COLONNE CILINDRICHE"

"GRIGLIA FINESTRE"

grid=SKEL_1(STRUCT(MKPOLS(larCuboids([5,1]))))
grid2=T([1,2])([.5,1])(SKEL_1(STRUCT(MKPOLS(larCuboids([4,1])))))
grid_rip=STRUCT(NN(2)([(STRUCT([grid,grid2])),T(2)(2)]+[grid]))
#VIEW(grid_rip)
bordo=SKEL_1(CUBOID([5,5]))
#VIEW(STRUCT([bordo,grid_rip]))
seg=T([1])(.5)(R([1,2])(-PI/2)(INTERVALS(2)(1)))
grata1=STRUCT(NN(4)([seg,T(1)(1)]))
grata2=T(2)(7)(grata1)
seg2=T([1,2])([5,1.5])(INTERVALS(2)(1))
grata3=STRUCT(NN(3)([seg2,T(2)(1)]))
grata=STRUCT([bordo,grid_rip,grata1,grata2,grata3])
griglia1=OFFSET([0.05,0.05])(grata)
griglia=PROD([griglia1,Q(0.05)])
finestra1=T([1,2,3])([0.1,0.2,25.5])(R([2,3])(PI/2)(griglia))
finestra2=T([1,2])([.3,0.1])(R([1,2])(PI/2)(finestra1))

"FINESTRE SUD"
grid_sud=SKEL_1(STRUCT(MKPOLS(larCuboids([5,1]))))
grid2_sud=T([1,2])([.5,1])(SKEL_1(STRUCT(MKPOLS(larCuboids([4,1])))))
grid3_sud=T(2)(2)(grid_sud)
gridsud=STRUCT([grid_sud,grid2_sud,grid3_sud])
bordo1=SKEL_1(CUBOID([5,3]))
wind1=T(2)(-1.5)(SKEL_1(STRUCT(NN(9)([CUBOID([1,1.5]),T(1)(0.5)]))))
quad=SKEL_1(T([2])(3)(CUBOID([0.5,1])))
quad1=SKEL_1(T([1,2])([.5,3])(STRUCT(NN(2)([CUBOID([1.5,1]),T(1)(1.5)]))))
seg3=T([1,2])([.5,4])(R([1,2])(PI/2)(INTERVALS(2)(1)))
rip_seg3=STRUCT(NN(3)([seg3,T(1)(1.5)]))
seg4=T([1])([5])(INTERVALS(2)(1))
rip_seg4=STRUCT(NN(2)([seg4,T(2)(1.5)]))
grata2=STRUCT([wind1,gridsud,bordo1,rip_seg3,rip_seg4,quad,quad1])
griglia2=OFFSET([0.05,0.05])(grata2)
griglia_sud=PROD([griglia2,Q(0.05)])
finestra1_sud=T([1,2,3])([0.1,0.2,15.5])(R([2,3])(PI/2)(griglia_sud))
finestra2_sud=T([1,2])([.3,0.1])(R([1,2])(PI/2)(finestra1_sud))
fin_SUD=T(3)(14.5)(S(3)(0.88)(T(3)(-14)(STRUCT([finestra1_sud,finestra2_sud]))))

GRATE=STRUCT([fin_SUD,finestra1,finestra2])
fin2=T(1)(20.8)(R([1,2])(PI/2)(GRATE))
fin3=T([1,2])([20.8,20.8])(R([1,2])(PI)(GRATE))
fin4=T(2)(20.8)(R([1,2])(-PI/2)(GRATE))
FINESTRE_s=STRUCT([GRATE,fin2,fin3,fin4])


"COLONNE"
#funzione modificata per CILINDRI
def larHollowCyl(r,R,height,angle=2*PI):
   def larHollowCyl0(shape=[36,1,1]):
      V,CV = larIntervals(shape)([angle,R-r,1])
      V = larTranslate([0,r,0])(V)
      domain = V,CV
      x = lambda p : p[1] * COS(p[0])
      y = lambda p : p[1] * SIN(p[0])
      z = lambda p : p[2] * height
      return larMap([x,y,z])(domain)
   return larHollowCyl0


base1=larHollowCyl(7.31,7.61,34,3*PI/2)([32,1,1])
cil_vuoto=STRUCT(MKPOLS(base1))
#VIEW(cil_vuoto)

"PILASTRI"

pil_x=T(2)(-0.3)(CUBOID([-7.61,0.3,34]))
pil_y=CUBOID([0.3,7.61,34])
pilastro=STRUCT([pil_x,pil_y])
PIL=DIFFERENCE([pilastro,BUCHI])


croce1=R([1,2])(PI/2)(STRUCT([cil_vuoto,PIL]))
croce2=T(1)(20.8)(R([1,2])(PI/2)(croce1))
croce3=T([1,2])([20.8,20.8])(R([1,2])(PI)(croce1))
croce4=T(2)(20.8)(R([1,2])(-PI/2)(croce1))

SALA_PREG=STRUCT([SALA,croce1,croce2,croce3,croce4])

"ARCHI ANGOLATI: decoro tetto"
para=CUBOID([20,0.3,6.3])
semi_circ=STRUCT(MKPOLS(larDisk(9.6/2,PI)([16,1])))
shape=T([1,2,3])([10,0.5,-0.15])(R([2,3])(PI/2)(PROD([semi_circ,Q(1)])))
shapeTETTO=DIFFERENCE([para,shape])
shape1=T(1)(-5.2)(shapeTETTO)

shapeR=R([1,2])(-PI/4)(R([2,3])(-PI/9)(shape1))
tetto=COLOR(RED)(T([1,2,3])([0.2,7,28])(shapeR))
cubo1=T([2,3])([-10,15])(CUBOID([20,10,20]))
cubo2=T([1,3])([-10,15])(CUBOID([10,20,20]))
eccesso=STRUCT([cubo1,cubo2])
tetto_finale1=DIFFERENCE([tetto,eccesso])
tetto_finale=T([1,2])([-4.8,-4.8])(tetto_finale1)
tetto_finale2=T([1,2])([16,16])(S([1,2])([-1,-1])(tetto_finale))
tetto_finale3=T([1,2])([16,4.8])(R([1,2])(PI/2)(tetto_finale))
tetto_finale4=T([1,2])([4.8,16])(S([1,2])([-1,-1])(R([1,2])(PI/2)(tetto_finale)))
TETTO=STRUCT([tetto_finale1,tetto_finale2,tetto_finale3,tetto_finale4])

"PAVIMENTO DI TRANSITO"

lines = lines2lines("pav_transito.lines")
Y,FV,EV,polygons = larFromLines(lines) 
#prova=STRUCT(MKPOLS((Y,FV))) 
#VIEW(prova)
"""
YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))
"""
#EV[107]:Y[8][0]-Y[0][0]== 0.39929999999999993

scala =5.73/0.39929999999999993
Z=((mat(Y)-Y[0])*scala).tolist()
"""
ZZ = AA(LIST)(range(len(Z)))
submodel = STRUCT(MKPOLS((Z,EV)))
VIEW(larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,0.1))
"""
#celle vuote
buchi = STRUCT(MKPOLS([Z,[FV[k] for k in [5,6,7]]]))
tot = STRUCT(MKPOLS([Z,FV]))
pav_frame= DIFFERENCE([tot,buchi])
pavrefl=S([1,2])([1.05,-1.09])(PROD([pav_frame,Q(0.3)]))
pav_transtop=T([1,3])([7.4,33.7])(pavrefl)
pav_trans5=T([1,3])([7.4,13.2])(pavrefl)
PAV_TRANS=STRUCT([pav_transtop,pav_trans5])



"""STRUTTURE"""
MURI_s=STRUCT([TETTO,SALA_PREG])
PAVIMENTI_s=STRUCT([soffitto,pav_sala,PAV_TRANS])
#FINESTRE_s
SALA_PREGHIERA=STRUCT([COLOR([0.6,0.6,0.6])(MURI_s),PAVIMENTI_s,FINESTRE_s])
#VIEW(SALA_PREGHIERA)



#rotazione di 6 gradi
rot_sala=R([1,2])(-PI-0.10472)(T([1,2])([-10.475,-10.475])(SALA_PREGHIERA))
tras_sala=T([1,2])([13.7,-29])(rot_sala)
SALA=tras_sala

"CORTE"

#W[112]: [14.625077902128593, 0.0]
#W[99]: [19.116875137151634, 0.0]
#FINESTRONE
buco=CYLINDER([5,1.5])(32)
buco_fin=T([1,2,3])([16.83,0.75,24.5])(R([2,3])(PI/2)(buco))


frame=R([1,2])(PI/2)(STRUCT(MKPOLS(larDisk(2,PI)([16,1]))))
buco_circ= S(2)(1.2)(PROD([frame,Q(1.5)])) 
buco0=T(3)(.5)(R([1,3])(-PI/2)(buco_circ))
buco1=S(3)(-1)(buco0)
buco2=T(2)(-1.5)(R([1,2])(PI/2)(STRUCT([buco0,buco1])))


fin_cut1=T([1,2,3])([25.4,-6,29])(R([1,2])(PI/3)(buco2))
fin_cut2=T([1,2,3])([25.4,-6,20])(R([1,2])(PI/3)(buco2))
fin_cutsx=STRUCT([fin_cut1,fin_cut2])
fin_cutdx=T(1)(16)(S(1)(-1)(T(1)(-17.1)(fin_cutsx)))

"""porta"""
#apertura=T([1,2,3])([15,-.7,10.4])(CUBOID([4,1.5,3]))
apertura1=T([1,2,3])([15,-13,13.4])(CUBOID([4,5,4.5]))
apertura2=T([1,2,3])([15,-17,13.4])(CUBOID([4,4,7.5]))


CUT=STRUCT([apertura1,apertura2,buco_fin,fin_cutsx,fin_cutdx])
#VIEW(STRUCT([COLOR(RED)(CUT),MURI]))
#VIEW(STRUCT([tras_SALA,SALA_INGRESSO,COLOR(RED)(CUT)]))
"MURI CORTE TONDI"

#Z[72][0]-Z[71][0]=34.842292014700966 #larghezza totale corte, misura presa da level 3 del centrale
#Z[34][0]-Z[36][0]=28.291149914387987 #misura cilindro esterno, presa dalla pav_corte del centrale
#Z[28][0]-Z[24][0]=23.017704047777045 #misura del cilindro interno, presa da piano livello 8

frame_tondo1=larHollowCyl(23.017704047777045/2,23.017704047777045/2-0.3,34,-PI)([16,1,1])
muro_tondo1=T(1)(16.586897081413213)(STRUCT(MKPOLS(frame_tondo1)))
frame_tondo2=larHollowCyl(28.291149914387987/2,28.291149914387987/2-0.3,34,-PI)([16,1,1])
muro_tondo2=T(1)(16.886897081413213)(STRUCT(MKPOLS(frame_tondo2)))
muri_1=T([1,3])([4.709034452490674,10.4])(CUBOID([10.3,0.3,3]))
muri_2=T([1,3])([4.709034452490674+14.290965547509327,10.4])(CUBOID([23.755725257845075-14.290965547509327,0.3,3]))
muri_3=T(1)(4.709034452490674)(CUBOID([23.755725257845075,0.3,10.4]))
muri_4=T([1,3])([4.709034452490674,13.4])(CUBOID([23.755725257845075,0.3,20.6]))
#VIEW(STRUCT([muri_1,muri_2,muri_3,muri_4]))

#VIEW(STRUCT([muri_1,muro_tondo1,muro_tondo2,MAPPA]))

MURO1=DIFFERENCE([muro_tondo1,CUT])
MURO2=DIFFERENCE([muro_tondo2,CUT])
MURO3=DIFFERENCE([muri_4,CUT])

"chiusura muri frontali"
front1=T(1)(2.7)(CUBOID([2.2,0.3,13.5]))
front2=T(1)(28.4)(CUBOID([2.5,0.3,13.5]))

"pareti scale"
parete1=T([1,2,3])([4.709034452490674+14.290965547509327,-2.8,10])(CUBOID([0.3,3,4]))
parete2=T([1,2,3])([14.75,-2.8,10])(CUBOID([0.3,3,4]))


corte=STRUCT([MURO1,MURO2,MURO3,muri_1,muri_2,muri_3,front1,front2,parete1,parete2])
#VIEW(corte)

"""PAVIMENTI CORTE"""

#LEVEL4.5:togli spigolo sulle scale
lines = lines2lines("corte_pav4.lines")
Y,FV,EV,polygons = larFromLines(lines) 
#prova=STRUCT(MKPOLS((Y,FV))) 
#VIEW(prova)

#MODIFICHE MISURE
Y[174]=[0.4376, 1]

Y[27]=[0.572, 1]

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EV)))
#VIEW(larModelNumbering(1,1,1)(Y,[YY,EV,FV],submodel,0.1))
scala = 28.291149914387987/0.9114
Z=((mat(Y)-Y[166])*scala).tolist()
#ZZ = AA(LIST)(range(len(Z)))
#submodel = STRUCT(MKPOLS((Z,EV)))
#VIEW(larModelNumbering(1,1,1)(Z,[ZZ,EV,FV],submodel,0.1))
#**celle vuote**
#celle vuote sono 0,1,2,7,65,4, mi serve solo la 3
buchi = STRUCT(MKPOLS([Z,[FV[4]]]))
tot = STRUCT(MKPOLS([Z,[FV[9]]]))
pav0= DIFFERENCE([tot,buchi])
"pavimento a metà piano"
pav4=T([1,3])([2.7,11.75])(PROD([pav0,Q(0.3)])) 
#VIEW(pav4)

"CORRIDOI"
pavimento=larHollowCyl(28.291149914387987/2-0.1,23.017704047777045/2-0.1,0.3,-PI)([16,1,1])
pav5=T([1,3])([16.75,13.2])(STRUCT(MKPOLS(pavimento)))
pav8=T([1,3])([16.75,22.2])(STRUCT(MKPOLS(pavimento)))
pav10=T([1,3])([16.75,28.2])(STRUCT(MKPOLS(pavimento)))
top=T([1,3])([16.75,32.25])(STRUCT(MKPOLS(pavimento)))
PAVIMENTI_C=STRUCT([pav5,pav4,pav8,pav10,top])

#VIEW(STRUCT([corte,PAVIMENTI_C]))

"GRATE"
#grata finestrone
grid_corte=SKEL_1(STRUCT(MKPOLS(larCuboids([7,1]))))
grid_corte2=T([1,2])([.5,1])(SKEL_1(STRUCT(MKPOLS(larCuboids([6,1])))))
grid_ripcorte=STRUCT(NN(3)([(STRUCT([grid_corte,grid_corte2])),T(2)(2)]+[grid_corte]))
bordofin=SKEL_1(CUBOID([7,7]))
seg_corte=T([1])(1.5)(R([1,2])(-PI/2)(INTERVALS(2)(1)))
grata_corte=STRUCT(NN(5)([seg_corte,T(1)(1)]))
grata_corte2=T(2)(9)(grata_corte)
grata_corte3=T(1)(-2)(R([1,2])(PI/2)(grata_corte))
grata_corte4=T(1)(9)(grata_corte3)
GRID=STRUCT([grata_corte,grata_corte2,grata_corte3,grata_corte4,bordofin,grid_ripcorte])
gridOFF=OFFSET([0.05,0.05])(GRID)
GRATA_fin=T([1,2])([-3.5,-3.5])(PROD([gridOFF,Q(0.05)]))
GRATA_corte=T([1,2,3])([16.83,0.15,24.5])(R([2,3])(PI/2)(GRATA_fin))

"grata fessure"

#dimensione fessure=(34.842292014700966-28.291149914387987)/2=3.27557105015649

frame0=SKEL_1(PROD([Hpc(Grid([2*[3.8/2]])),Hpc(Grid([35*[31./35]]))]))
frame1=T(2)(-1.5)(CUBOID([3.8,1.5]))
frame2=T(2)(31)(CUBOID([3.8,1.5]))
mur=STRUCT([frame1,frame2])
gridOFF=OFFSET([0.05,0.05])(frame0)
grid_fess=T(3)(0.15)(PROD([gridOFF,Q(0.05)]))
muretti=COLOR([0.6,0.6,0.6])(PROD([mur,Q(0.3)]))
FESSURE0=R([2,3])(PI/2)(T(2)(1.5)(STRUCT([muretti,grid_fess])))
FESS1=T([1,2])([-0.6,0.3])(FESSURE0)
FESS2=T([1,2])([30.8,0.3])(FESSURE0)
FESSURE=STRUCT([FESS1,FESS2])

#VIEW(STRUCT([corte,FESSURE]))
"""scale"""
SCALA1=T([1,2,3])([19.3,-2.717136273864386,11.75])(R([1,2])(PI/2)(createFilledSteps(10,[0.3,5,0.15])))
SCALA2=T([1,2,3])([19.6,-11.85,13.35])(R([1,2])(PI/2)(createFilledSteps(9,[0.45,5.2,0.16],rail=True,spessore=0.6)))

"STRUTTURE"
#corte
#PAVIMENTI_C
GRATE_C=STRUCT([GRATA_corte,FESSURE])
SCALE=STRUCT([SCALA1,SCALA2])
VIEW(STRUCT([SCALE,GRATE_C,PAVIMENTI_C,COLOR([0.6,0.6,0.6])(corte),SALA]))
SALA_PREGHIERA=STRUCT([SCALE,GRATE_C,PAVIMENTI_C,COLOR([0.6,0.6,0.6])(corte),SALA])

SUD=T([1,2])([35.3, -33.1])(SALA_PREGHIERA)


