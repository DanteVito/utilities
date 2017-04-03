# importing packages
import re

vltotal = ["vl. 1,00", "vl. total. 21,02", "vl:. R$3999,00"]
qtd = ["qtd.: 2", "qtd.: 300", "qtd.:987"]


pattern = "[1-9]*,[0-9][0-9]|[0-9][0-9]*"

def ret_values(pattern, lista, type):
	result = []
	for item in lista:
		f = re.search(pattern, item)
		f_str = f.group()
		f_str = type(f_str.replace(',','.'))
		result.append(f_str)
	return result

print(ret_values(pattern,qtd,int))