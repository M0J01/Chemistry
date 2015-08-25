
class element:
	def __init__(self, symbol, aomtic_Number, name, conductivity, amu, electro_Neg, melt_P, boil_P, group, block, ionization_Energy, element_Category):
		self.symbol = symbol						#For the English American Periodic Table
		self.atomic_Number = atomic_Number			#
		self.name = name							#
		self.conductivity = conductivity 			# Gasses don't conduct very well under STP. Need a way to declare as NA... Hydrogen has a huge scale of conduction under various situations
		self.amu = amu								#
		self.electro_Neg = electro_Neg 				#Pauling Scale
		self.melt_P = melt_P						#Kelvin at STP
		self.boil_P = boil_P 						#Kelvin at STP
		self.group = group							#Periodic Table as of 8/24/15
		self.block = block							#Periodic Table as of 8/24/15
		self.ionization_Energy = ionization_Energy 	#Kj/mol
		self.element_Category = element_Category 	#Metalloid
	

symbol = 'H'					#For the English American Periodic Table
atomic_Number = 1				#
name = 'Hydrogen'				#
conductivity = '0.0000' 		# Gasses don't conduct very well under STP. Need a way to declare as NA... Hydrogen has a huge scale of conduction under various situations
amu = 1.008						#
electro_Neg = 2.20 				#Pauling Scale
melt_P = 13.99 					#Kelvin at STP
boil_P = 20.271 				#Kelvin at STP
group = 'group 1'				#Periodic Table as of 8/24/15
block = 's-block'				#Periodic Table as of 8/24/15
ionization_Energy = 1312.0 		#Kj/mol
element_Category = 'metalloid' 	#Metalloid

H = element(symbol, atomic_Number, name, conductivity, amu, electro_Neg, melt_P, boil_P, group, block, ionization_Energy, element_Category)

symbol = 'Mg'

Mg = element(symbol, atomic_Number, name, conductivity, amu, electro_Neg, melt_P, boil_P, group, block, ionization_Energy, element_Category)


print Hg		#This prints the memory location of H, where the element is stored...
print Mg		#Which is assigned every time the code is run... I wonder how to use persistent memory? Might be better for my level to use persistant lists or documents.
print Hg			


'''
electron_Config

'''




