L1 = ['Hello','World',18,'Apple',None]
L2 = []
for x in L1:
	if isinstance(x,str):
		L2.append(x.lower())
print(L2)