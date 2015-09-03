#! /usr/bin/python


def main():


    listaQueContieneElSudoku = sudoku("mySudoku.txt")
    # print(listaQueContieneElSudoku)

    contadorRenglones = 0 #inicia en 0 y aumentara hasta 8, dando 9 renglones
    laListaEsUnSudoku = True
    

    for n in range(0,27):

        segmento = []

        #Chequeo para busqueda de renglones.
        if n < 9:
            segmento = listaQueContieneElSudoku[contadorRenglones:contadorRenglones+9]
            contadorRenglones += 9
        #Chequeo para busqueda de columnas
        elif n >= 9 and  n < 18:
            segmento = generaColumna(n-9, listaQueContieneElSudoku)
        #Busqueda de cuadrantes
        else:
            segmento = generaCuadrante(n-18,listaQueContieneElSudoku)

        if not esFactorial(segmento) or not esGauss(segmento):
            laListaEsUnSudoku = False
            break


    print("Es un sudoku readl? {}".format(laListaEsUnSudoku))

        #Chequeo para busqueda de cuadrantes

def generaCuadrante(indice, sudoku):

    #Contenedor del cuadrante visto como lista [range(9)]3x3
    # print(indice)
    cuadrante = []
    adelantador = indice
    #Remedio para switch

    if indice < 3:


        if indice == 0:
            adelantador=0
        if indice == 1:
            adelantador=3
        if indice == 2:
            adelantador=6 

        for m in range(adelantador, 27 ,9):
            for x in range(m,m+3):
                cuadrante.append(sudoku[x])


    elif indice >= 3 and indice < 6:
        if indice == 3:
            adelantador=0
        if indice == 4:
            adelantador=3
        if indice == 5:
            adelantador=6 

        for m in range(adelantador+27, 27*2 ,9):
            for x in range(m,m+3):
                cuadrante.append(sudoku[x])
        
    elif indice >= 6:
        if indice == 6:
            adelantador=0
        if indice == 7:
            adelantador=3
        if indice == 8:
            adelantador=6 

        for m in range(adelantador+27*2, 27*3 ,9):
            for x in range(m,m+3):
                cuadrante.append(sudoku[x])

    return cuadrante

def esGauss(renglon):
    total = 0
    esFactor  = False
    for number in renglon:
        total = total + int(number)

    if total == 45:
        esFactor = True

    return esFactor


def esFactorial(renglon):

    total = 1
    esFactor  = False
    for number in renglon:
        total = total * int(number)

    if total == factorial(9):
        esFactor = True

    return esFactor

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sudoku(nombreDeArchivo):
    # print("hola")
        mySudokuFile = open(nombreDeArchivo,"r")
        sudoku =[]
        for line in mySudokuFile.readlines():
            for c in line:
                if not c == "\n" and not c == "\t":
                    sudoku.append(c)

        return sudoku


def generaColumna(numeroDeColumna, sudokuInicial):
    columna = []
    for index in range(numeroDeColumna,81,9):
         columna.append(sudokuInicial[index])

    return columna



#    billete = 40
#    monedas = [24,20]
#    print(rebice(billete, monedas))
#\

#    monedasUsadas= []
#    while(billete>=0):
#        
#        tempBill = billete
#        qRecibe = rebice(tempBill,monedas)
#        print( qRecibe)
#        if tempBill - qRecibe >= 0:
#            monedasUsadas.append(qRecibe)
#            billete -= qRecibe
#
#    print(monedasUsadas)




# def rebice(billete, monedas):
#     maxModulo = False
#     print("Bill:{} Coins:{} ".format(billete,monedas))
    
#     for i in  monedas():
#         if (billete % i) == 0:
#             maxModulo = i
#     return maxModulo

#
#    
#    i = 0
#    for n in range(42101000,421011000):
#        if isAuto(n):
#            print(n)
#
#    mi = 1000
#    print(isAuto(1210))

#NO mnumeros distinos
#Suma de digitos 

# def isAuto(n):
#     ar = str(n)
#     miBool = True
#     m = 0
    
# #    print(ar)
#     for first in ar:

#         c= 0
#         for clone in ar:
#             if int(clone) == m:
#                 c+=1
#         m+=1
#         if int(first) != c:
#             miBool = False
#             break

#     return miBool





# def splitStringIntoArray(string):
#     l = []
#     for s in string:
#         l.append(s)
#     return l


#    f = Fib()
#    outFile = open('../Shared/outFile.txt', 'w')
#    c= 0
#    for p in f.series():
#        
#        if c >=10 or p >=2147483648:
#            break
#        c+=1
#        
#        print('{}\t{}'.format(c,p),file=outFile)


#-----FIBBIONACI CLASS
# class Fib():
#     def __init__(self):
#         self.a = 0
#         self.b = 1

#     def series(self):
#         while(True):
#             yield(self.b)
#             self.a,self.b = self.b, self.a + self.b


#----- isPrime Method
# def isPrime(n):
#     if n == 1:
#         return False
#     for x in range(2, n):
#         if n % x == 0:
#             return False
#     return True

# #---Iterative function for primes detection
# def primes(n=1):
#     while(True):
#         if isPrime(n):yield n
#         n+=1

#----TEXT FORMATTING
#    print("A({}) is bigger than B({})".format(a,b))


#-----GREAT FIBBONACCI
#x,y,c = 0,1,0
#
#while c < 100:
#    print(y)
#    x,y,c = y,x+y,c+1
#
#print(len(str(y)))

#------Reading Lines
#
#f = open("line.txt")
#
#for line in f.readlines():
#    print(line)#!/usr/bin/python3

if __name__ == '__main__' : main()
