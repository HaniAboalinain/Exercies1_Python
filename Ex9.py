import sympy as sym
import numpy as np
from sympy import symbols
from sympy import *
from sympy.plotting import plot
from sympy.plotting import plot3d
import xlsxwriter
from xlwt import Workbook, Formula
from xlrd import open_workbook


print("==========================Exercise one=====================")

x, y , z = symbols('x y z')

expr = x**2+x**3+21*x**4+10*x+1
print (expr.subs(x, 7))
print( sym.expand((x+y)**2) )
print( sym.simplify((4*x**3 + 21*x**2 + 10*x + 12)))
print(sym.limit(1/(x**2), x,sym.oo))
i,n = sym.symbols('i n')
print(sym.summation(2*i + i-1, (i, 5, n)))
print(sym.integrate(sin(x) + exp(x)*cos(x)+tan(x), x))
print( sym.factor(x**3 + 12*x*y*z + 3*y**2*z) )
print (sym.solveset(x-4, x) )
m1 = sym.Matrix([[5, 12, 40], [30, 70, 2]])
m2 = sym.Matrix([2, 1, 0])
print( m1*m2 )

plot(x**3+3, (x, -10, 10))

f=x**2*y**3
plot3d(f, (x, -6, 6), (y, -6, 6))

print("==========================Exercise two=====================")

workbook = xlsxwriter.Workbook('forEx.xlsx')
worksheet = workbook.add_worksheet()

text1 = 'This is Example'
text2 = 'My first export examlpe'

Fformat = workbook.add_format({	'bold': True, 'font_color': 'red', 'font_size': 14})

Sformat = workbook.add_format({'font_size': 14})

worksheet.write('A1', text1, Fformat)
worksheet.write('A2', text2, Sformat)
worksheet.write('A3', 1, Sformat)
worksheet.write('A4', 2, Sformat)
worksheet.write('A5', 3, Fformat)

workbook.close()

print("==========================Exercise three=====================")

wb = open_workbook('sample.xlsx')

for i in wb.sheets():
    print('Sheet:',i.name)
    for j in range(i.nrows):
        values = []
        for k in range(i.ncols):
            values.append(i.cell(j, k).value)
        print(values)