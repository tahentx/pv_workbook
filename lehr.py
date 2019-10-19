
def set_sample_size(e,cv,stdev):
    n = ((cv * stdev)/e)**2
    print(n)

set_sample_size(1,1.96,6.95)
