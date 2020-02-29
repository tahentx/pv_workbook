import pydecisions as pyd
# a = pyd.fin()
# cashflows = [-100,50,30,20,10]
# print(a.npv(.3,cashflows))

earned_value = pyd.evm(100,0.5,0.4,45)
print(earned_value.results())


# a = pyd.evm(100,0.5,0.4,45)
# print(a.results())
