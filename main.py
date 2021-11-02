from my_simple_bd import My_simple_bd

myBd = My_simple_bd("./mybd.db")
myBd.set('SashaG', '11/01/1990')
myBd.set('SashaV', '11/01/1991')

print(myBd.get('SashaV'))

