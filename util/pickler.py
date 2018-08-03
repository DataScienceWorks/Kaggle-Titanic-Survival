import pickle

def pickle_in(obj, filename):
	"""
		Write the object to  `filename` using pickle
	"""
	outfile = open(filename,'wb')
	pickle.dump(obj, outfile)
	outfile.close()
	
def pickle_out(filepath):
	"""
		Read the object from  `filename` using pickle
	"""
	infile = open(filepath,'rb')
	obj = pickle.load(infile)
	infile.close()
	return obj
