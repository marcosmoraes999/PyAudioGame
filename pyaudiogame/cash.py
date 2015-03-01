#Use this module to store variables and settings
try:
	import cPickle as _pickle
except:
	import pickle as _pickle

def save(file="save.sav", level=1):
	"""Call this function with the location of the file where you wish to save the info in this module. If the level == 0, it will just return a dict of everything that would be saved. If level == 1, it will save to a pickled file."""
	g = globals()
	cash_dict = {}
	[cash_dict.update({i: g[i]}) for i in g if not i.startswith("_")]
	del(cash_dict['save'])
	del(cash_dict['load'])
	if level == 1:
		with open(file, 'wb') as f:
			_pickle.dump(cash_dict, f, protocol=_pickle.HIGHEST_PROTOCOL)
	return cash_dict

def load(file="save.sav", level=1):
	"""This will return the dict of all the variables in the cash module. If there is no file, it will return False. If level == 0, it will just return a dict of all the items that are in the save file. If level == 1, it will overwrite any variables in cash that have the same variable as the saved variables. If level == 2, the cash variables will not be overwritten, but new variables will be added from the save."""
	try:
		with open(file, "rb") as f:
			loaded_file = _pickle.load(f)
	except:
		return False
	if level == 1:
		[globals().update({i: loaded_file[i]}) for i in loaded_file]
	elif level == 2:
		g = globals()
		[globals().update({i: loaded_file[i]}) for i in loaded_file if i not in g]
	return loaded_file
