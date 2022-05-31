from numpy import *
from random import randint as rd
arregloA = array([rd(0,500) for i in range(1,100)])
indexs = [i for i in arregloA if i%2 == 0]
