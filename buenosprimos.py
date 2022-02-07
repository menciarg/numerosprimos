n=21
cont=0
primos={}
for i in range (1, n+1):
	divisor=[]
	for x in range(1,i+1):
		if (i%x==0):
			divisor.append(x)
		primos[i]=divisor
for k,v in primos.items():
	if (len(v)==2):
		cont+=1
		print(' ', k, end ='')
print('\nHay %u numeros primos. '%cont)
print('\n',primos)
	