# importing packages
import re

pattern = "[1-9]*,[0-9][0-9]|[0-9][0-9]*"

def ret_values(pattern, lista, type):
	result = []
	for item in lista:
		f = re.search(pattern, item)
		f_str = f.group()
		f_str = type(f_str.replace(',','.'))
		result.append(f_str)
	return result
