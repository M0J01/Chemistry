temp = []

e_L_F = open("Elementalist.txt") 	#Elemental List File
e_L = e_L_F.read()					#Elemental List Object

eL1 = e_L.split('\n')

for object in eL1:
	eL2 = object.split('\t')
	temp.append(eL2)
	
print temp