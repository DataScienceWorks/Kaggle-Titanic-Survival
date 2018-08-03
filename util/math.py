import numpy as np

def round_single(n):
	"""
		Rounds given input to single decimal
	"""
	return np.round(n,decimals=1)

def round_double(n):
	"""
		Rounds given input to double decimal
	"""
	return np.round(n,decimals=2)

def range_simple(start,end,step, decimal=1):
	"""
		Returns range of values rounded to single decimal point by default
	"""
	lst = list(np.arange(start,end,step))
	mp = map(round_single, lst) if decimal==1 else map(round_double, lst) # Python's Ternary Operator
	lst = list(mp)
	return lst
