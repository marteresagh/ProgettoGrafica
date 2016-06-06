TETTO
def CONICALSURFACE (args):
    apex=args[0]
    alpha_fn   = lambda point: apex
    beta_fn = lambda point: [ args[1](point)[i]-apex[i] for i in range(len(apex))]
    return RULEDSURFACE([alpha_fn, beta_fn])
#radius=1
#altezza=SQRT((34.49700711053653/2)**2-(7.1)**2)

domain = EMBED(1)(PROD([INTERVALS(3)(48),INTERVALS(1)(48)]))
beta = lambda point: [COS(point[0]),SIN(point[0]),-1]
out = GMAP(CONICALSURFACE([[0,0,0],beta]))(domain)
VIEW(out)
cono0=S([1,2,3])([7.4,8,18.3])(out)
angle=ATAN(7.1/16.5)
cono1=R([2,3])(3*angle)(cono0)

cubo=T([1,2,3])([-8,34.49700711053653/2,-10])(CUBOID([16,0,20]))
conoR=STRUCT(NN(8)([cono1,R([1,2])((2*PI)/8)]))
conoT=T([1,2,3])([51.95369101486749,15.00421784098255,40])(conoR)
#VIEW(conoT)
centro=[51.95369101486749,15.00421784098255,40]
VIEW(STRUCT([ING,INTERNO,conoT]))

pr=PROD([conoT, QUOTE([1]) ])
VIEW(pr)

