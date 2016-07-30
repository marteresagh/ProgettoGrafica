"""ringhiera"""
from larlib import *

def ringhiera(N):
	pil=CUBOID([0.06,0.015,1])
	rip_pil=STRUCT(NN(N)([pil,T(1)(0.16+0.06)]))
	mano=T([1,2,3])([-0.1,-0.05,1])(CUBOID([N*0.06+(N-1)*0.16+0.2,0.1,0.03]))
	ringhiera=STRUCT([rip_pil,mano])
	return ringhiera

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



def ringhiera_circle(n,radius,d):
	pil=CUBOID([0.06,0.06,1])
	rip_pil=[]
	for k in range(n):
		rip_pil+=LIST(T([1,2])([radius*COS((k+1)*d),radius*SIN((k+1)*d)])(pil))
	corrimano=T(3)(1)(STRUCT(MKPOLS(larHollowCyl(radius-0.1,radius+0.1,0.03,PI)([32,1,1]))))
	return STRUCT([corrimano,STRUCT(rip_pil)])


def stepsRing(N,dimensioni):
	sx,sy,sz = dimensioni
	base1=T(3)(1)(CUBOID([sx*N,0.1,0.03]))
	m=MAT([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,-(sz*(N-1))*1./(sx*N),0,1]])
	hand=STRUCT(NN(2)([T(2)(0.05)(m(base1)),T(2)(sy-0.1)]))	   
	pil=CUBOID([0.06,0.015,1])
	rip_pil=STRUCT(NN(N)([T(1)(sx/2)(pil),T(1)(sx)]))			
	ringh=STRUCT(NN(2)([T(2)(0.05)(m(rip_pil)),T(2)(sy-0.1)]))			
	return STRUCT([ringh,hand])

