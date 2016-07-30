from larlib import *
#TETTO
def CONICALSURFACE (args):
    apex=args[0]
    alpha_fn   = lambda point: apex
    beta_fn = lambda point: [ args[1](point)[i]-apex[i] for i in range(len(apex))]
    return RULEDSURFACE([alpha_fn, beta_fn])
#radius=1
#altezza=SQRT((34.49700711053653/2)**2-(7.1)**2)

domain = EMBED(1)(PROD([INTERVALS(3)(8),INTERVALS(1)(8)]))
#X,FV,EV=UKPOL(domain)
angle0=5*PI/8
beta = lambda point: [COS(point[0]),SIN(point[0])*COS(angle0)+SIN(angle0)+1,SIN(angle0)*SIN(point[0])-COS(angle0)-1.35]
out = GMAP(CONICALSURFACE([[0,0,0],beta]))(domain)
OUToff=OFFSET([0.01,0.01,0.01])(out)
#VIEW(out)
cono0=S([1,2,3])([7.85,10,6.5])(OUToff)
angle=ATAN(7.1/16.5)
conoR=STRUCT(NN(8)([cono0,R([1,2])((2*PI)/8)]))
TETTO_CENTRO=T([1,2,3])([51.95369101486749,15.00421784098255,39.5])(conoR)
#o=[51.95369101486749,15.00421784098255,40]

#VIEW(TETTO_CENTRO)

