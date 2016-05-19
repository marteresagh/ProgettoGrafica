#SCALE
def createFilledSteps(N,dimensioni):
    sx,sy,sz = dimensioni
    V,FV=larCuboids([1,1])
    step = S([1,2])([sx,sy])(STRUCT(MKPOLS((V,FV))))
    step =  steps = PROD([step,INTERVALS(sz)(1)])
    for i in range(1,N):
        stepp = T(3)(-sz*i)(S(1)(1+i)(step))
        steps = STRUCT([steps,stepp])
    return steps

def createSteps(N,dimensioni):
    sx,sy,sz = dimensioni
    V,FV=larCuboids([1,1])
    step = S([1,2])([sx,sy])(STRUCT(MKPOLS((V,FV))))
    step =  steps = PROD([step,INTERVALS(sz)(1)])
    steps = STRUCT(NN(N)([step, T([1,3])([sx,-sz])]))
    return steps
