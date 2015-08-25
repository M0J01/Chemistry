
elements = []
temp = []
									#Holds string of e_L
e_L_F = open("Elementalist.txt") 	#Elemental List File
e_L = e_L_F.read()					#Elemental List Object
e_L_2 = ''

n_E_L_F = open("Computer_Elementalist.txt",'w')		#Making a computer readable version of the elemental list


for object in e_L:									#Takes away tabs and spaces from e_L
	if object != '\t':								#Apparently \t is read as a single character... FORMATING!
		if object != ' ':
			e_L_2 += object
		
e_L_3 = e_L_2.split('\n') 							#e_L_3 splitting e_L_2 by lines

for entry in e_L_3:							#creating a new container with one list of attributes for each element
	if entry:
		sorted = entry.split(',')
		temp.append(sorted)
#print temp

for item in temp:
	elements.append(item)
	
	


'''
eL1 = e_L.split('\n')

for object in eL1:
	eL2 = object.split('\t')
	temp.append(eL2)
	
print temp

'''