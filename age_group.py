import numpy as np

def age_group(age):
	""" Given an input Age as number, this method returns the groups it belongs to -- baby, child, teen, adults, aged. """
	if(age == np.nan):
		return np.nan
	elif(age<3): 
		return 'baby'
	elif(age<12): 
		return 'child'
	elif(age<20): 
		return 'teen'
	elif(age<60): 
		return 'adult'
	else: 
		return 'aged'
