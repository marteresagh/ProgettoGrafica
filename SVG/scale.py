#SCALE
from larlib import *
def createFilledSteps(N,dimensioni,rail=False,spessore=0.3,altezza=1.5):
	sx,sy,sz = dimensioni
	V,FV=larCuboids([1,1])
	step = S([1,2])([sx,sy])(STRUCT(MKPOLS((V,FV))))
	step =  steps = PROD([step,INTERVALS(sz)(1)])
	for i in range(1,N):
	        stepp = T(3)(-sz*i)(S(1)(1+i)(step))
	        steps = STRUCT([steps,stepp])
	if(rail==True):
		base=CUBOID([sx*N,spessore,altezza])
		m=MAT([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,-(sz*(N-1))*1./(sx*N),0,1]])
		ringhiera=STRUCT(NN(2)([m(base),T(2)(sy-spessore)]))	   
		return STRUCT([ringhiera,steps])	
	return steps

def createSteps(N,dimensioni,full=False,spessore=0.3,altezza=1.5):
	sx,sy,sz = dimensioni
	V,FV=larCuboids([1,1])
	step = S([1,2])([sx,sy])(STRUCT(MKPOLS((V,FV))))
	step =  steps = PROD([step,INTERVALS(sz)(1)])
	steps = STRUCT(NN(N)([step, T([1,3])([sx,-sz])]))
	if(full==True):
		base=CUBOID([sx*(N-1),sy,sz])
		m=MAT([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,-(sz*N)*1./(sx*N),0,1]])
		filled=m(base)	   	
		base1=CUBOID([sx*N,spessore,altezza])
		m=MAT([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,-(sz*(N-1))*1./(sx*N),0,1]])
		ringhiera=STRUCT(NN(2)([m(base1),T(2)(sy-spessore)]))	   
		return STRUCT([ringhiera,steps,filled])
	return steps
