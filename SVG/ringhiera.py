"""ringhiera"""
from larlib import *

def ringhiera(N):
	pil=CUBOID([0.06,0.015,1])
	rip_pil=STRUCT(NN(N)([pil,T(1)(0.16+0.06)]))
	mano=T([1,2,3])([-0.1,-0.05,1])(CUBOID([N*0.06+(N-1)*0.16+0.2,0.1,0.03]))
	ringhiera=STRUCT([rip_pil,mano])
	return ringhiera
