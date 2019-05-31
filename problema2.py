#problema2

suc=open('sucursales.txt','r')
mens1=[]
i=0
for line in suc:
	mens1.append(line.split(","))
	mens1[i].pop(2)
	mens1[i][0]=int(mens1[i][0])
	i=i+1 
print (mens1)
#mens=(f.readline().split(","))
#mens.pop(2)
#print (mens)
art=open('articulos.txt','r')
mens2=[]
i=0
for line in art:
	mens2.append(line.split(","))
	mens2[i].pop(3)
	mens2[i][0]=int(mens2[i][0])
	mens2[i][2]=float(mens2[i][2])
	i=i+1 
print (mens2)

axs=open('articulosXsucursal.txt','r')
mens3=[]
i=0
ceros=[]
for line in axs:
	mens3.append(line.split(","))
	mens3[i].pop(4)
	mens3[i][0]=int(mens3[i][0])
	mens3[i][1]=int(mens3[i][1])
	mens3[i][2]=int(mens3[i][2])
	mens3[i][3]=int(mens3[i][3])
	i=i+1 
	ceros.append(0)
print (mens3)

for i in range (0,len(mens3)):
	if mens3[i][3]==0:
		c=mens3[i][2]
		ceros.insert(mens3[i][1],c)
	elif mens3[i][3]>5:
		if len(ceros)>mens3[i][1]:
			if ceros[mens3[i][1]] is not None:
				print(mens2[mens3[i][1]-1][1])
				ceros[mens3[i][1]]=0
print ('ceros')
print (ceros)

