
class element:
	def __init__(self, in_List): #list[self, symbol, aomtic_Number, name, conductivity, amu, electro_Neg, melt_P, boil_P, group, block, ionization_Energy, element_Category]
		self.symbol = in_List[0]						#For the English American Periodic Table
		self.atomic_Number = in_List[1]			#
		self.name = in_List[2]							#
		self.conductivity = in_List[3] 			# Gasses don't conduct very well under STP. Need a way to declare as NA... Hydrogen has a huge scale of conduction under various situations
		self.amu = in_List[4]								#
		self.electro_Neg = in_List[5] 				#Pauling Scale
		self.melt_P = in_List[6]						#Kelvin at STP
		self.boil_P = in_List[7] 						#Kelvin at STP
		self.group = in_List[8]							#Periodic Table as of 8/24/15
		self.block = in_List[9]							#Periodic Table as of 8/24/15
		self.ionization_Energy = in_List[10] 	#Kj/mol
		self.element_Category = in_List[11] 	#Metalloid



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
	elements.append(element(item))

print elements[2].name
	


'''
eL1 = e_L.split('\n')

for object in eL1:
	eL2 = object.split('\t')
	temp.append(eL2)
	
print temp

'''