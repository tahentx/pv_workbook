import pydecisions as pyd
# a = pyd.fin()
# print(a.npv(.3,[-100,50,30,20,10]))
a = pyd.evm(100,0.5,0.4,45)
print(a.results())
