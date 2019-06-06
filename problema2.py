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
aux=[]
for line in axs:
	mens3.append(line.split(","))
	mens3[i].pop(4)
	mens3[i][0]=int(mens3[i][0])
	mens3[i][1]=int(mens3[i][1])
	mens3[i][2]=int(mens3[i][2])
	mens3[i][3]=int(mens3[i][3])
	i=i+1 
	aux.append([0,0])
print (mens3)
salida=open('Infsal.txt', 'w')
salida.write("Articulos a reponer \r\n")
salida.write("CodSuc - CodArt - Nombre Articulo \n")
naxs=len(mens3)
for i in range (0,naxs):
	codart=mens3[i][1]
	codsuc=mens3[i][2]
	cant=mens3[i][3]
	cantaux=aux[codart][1]
	sucaux=aux[codart][0]
	if cant==0:
		if cantaux>5:
			salida.write("%5i \t %5i \t %s \n" % (codsuc,codart,mens2[codart-1][1]) ) 
			cantaux=None		
		else:
			aux[codart]=[codsuc,cant]
	elif cant>5:
		if cantaux==0 and sucaux!=0:
			salida.write("%5i \t %5i \t %s \n" % (sucaux,codart,mens2[codart-1][1]) ) 
			cantaux=None
		else:
			aux[codart]=[codsuc,cant]
print ('auxiliar')
print (aux)
 
salida.close()
suc.close()
art.close()
axs.close()
