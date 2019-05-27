#problema2

f=open('sucursales.txt','r')
mens=[]
i=0
for line in f:
	mens.append(line.split(","))
	mens[i].pop(2)
	i=i+1 
print (mens)
#mens=(f.readline().split(","))
#mens.pop(2)
#print (mens)
