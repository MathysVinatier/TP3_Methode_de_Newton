import math


#================= Point Fixe =================

def PointFixe (g, x0, epsilon, Nitermax) :
    n = 1
    xold = x0
    xnew = g(xold)
    alpha = xnew-xold
       
    while abs(alpha) > epsilon and n < Nitermax :
        xnew = g(xold)
        n= n+1
        alpha = xnew - xold
        xold = xnew
    print('===> alpha = ',xnew ,'N = ',n)


print ("="*5,"Fonction 1","="*5)

def g1(x):
    return(9-3*x)**(1/4)

a = PointFixe (g1, -2, 1E-5, 1E4)
print("Voila le resultat\n")

def g1bis(x):
    return -((9-3*x)**(1/4))

b = PointFixe (g1bis, 2, 1E-5, 1E4)
print("Voila le résultat\n\n")

print ("="*5,"Fonction 2","="*5)

def g2(x):
    return (math.acos((x+2)/3))
c = PointFixe (g2, 0, 1E-5, 1E4)
print ("Voila le resultat\n")


def g2bis(x):
    return -(math.acos((x+2)/3))
cbis = PointFixe (g2bis, 0, 1E-5, 1E4)
print ("Voila le resultat\n\n")

print ("="*5,"Fonction 3","="*5)

def g3(x):
    return math.log(7/x)
d= PointFixe (g3, 6.9, 1E-5, 1E4)
print("Voila le résultat\n\n")

print ("="*5,"Fonction 4","="*5)

def g4(x):
    return math.log(10+x)
e= PointFixe (g4, -9.99, 1E-5, 1E4)
print(e, "Voila le résultat\n")

def g4bis(x):
    return math.exp(x)-10
ebis=PointFixe(g4bis,2.5,1E-5,1E4)
print("Voila le résultat\n\n")

print ("="*5,"Fonction 5","="*5)

def g5(x):
    return math.atan(((x+5)/2))
f= PointFixe (g5, 1.2, 1E-5, 1E4)
print("voila le resultat\n\n")

print ("="*5,"Fonction 6","="*5)

def g6(x):
    return math.log((x**2)+3)
g= PointFixe (g6, 1.9, 1E-5, 1E4)
print ("Voila le résultat\n\n")

print ("="*5,"Fonction 7","="*5)

def g7(x):
    return (7-4*math.log(x))/3
h=PointFixe(g7,1.7,1E-5,1E4)
print("Voila le resultat\n\n")

print ("="*5,"Fonction 8","="*5)

def g8(x):
    return ((2*(x**2)-(4*x)+17)**0.25)
i=PointFixe(g8,-2,1E-5,1E4)
print("Voila le résultat\n")

def g8bis(x):
    return -((2*(x**2)-(4*x)+17)**0.25)
j=PointFixe(g8bis,3,1E-5,1E4)
print ("Voila le résultat\n\n")

print ("="*5,"Fonction 9","="*5)

def g9(x):
    return math.log(2*math.sin(x)+7)
k = PointFixe(g9,3,1E-5,1E4)
print("Voila le resultat\n\n")

print ("="*5,"Fonction 10","="*5)

def g10(x):
    return math.log(10)-math.log(math.log(x**2+4))
l = PointFixe(g10,2,1E-5,1E4)
print ("Voila le résultat\n\n")






#================= Newton =================

def Newton (f, fder, x0, epsilon, Nitermax) :
    n = 1
    xold = x0
    xnew = xold-(f(xold)/fder(xold))
    delta = xnew-xold
    
    while abs(delta) > epsilon and n < Nitermax :
        xnew = xold-(f(xold)/fder(xold))
        n += 1
        delta = xnew - xold
        xold = xnew
        print (xnew, n, delta)
    
    return print('===>','alpha = ',xnew ,'N = ',n)




#========== Fonction 1: ==========

def f1(x):
    return x**4+3*x-9

def f1der(x):
    return 4*x**3+3

print('========== Fonction 1: ==========\n')
Newton(f1,f1der,-2,1e-5,20)
Newton(f1,f1der,2,1e-5,20),print('\n\n')




#========== Fonction 2: ==========

def f2(x):
    return 3*math.cos(x)-2-x

def f2der(x):
    return -3*math.sin(x)-1

print('========== Fonction 2: ==========\n')
Newton(f2,f2der,-5,1e-5,20)
Newton(f2,f2der,-1,1e-5,20)
Newton(f2,f2der,0,1e-5,20),print('\n\n')




#========== Fonction 3: ==========

def f3(x):
    return x*math.exp(x)-7

def f3der(x):
    return math.exp(x)+x*math.exp(x)

print('========== Fonction 3: ==========\n')
Newton(f3,f3der,7,1e-5,20),print('\n\n')




#========== Fonction 4: ==========

def f4(x):
    return math.exp(x)-x-10

def f4der(x):
    return math.exp(x)-1

print('========== Fonction 4: ==========\n')
Newton(f4,f4der,-10,1e-5,20)
Newton(f4,f4der,3,1e-5,20),print('\n\n')




#========== Fonction 5: ==========

def f5(x):
    return 2*math.tan(x)-x-5

def f5der(x):
    return 2/((math.cos(x))**2)-1

print('========== Fonction 5: ==========\n')
Newton(f5,f5der,1.2,1e-5,20),print('\n\n')




#========== Fonction 6: ==========

def f6(x):
    return x**2+3-math.exp(x)

def f6der(x):
    return 2*x-math.exp(x)

print('========== Fonction 6: ==========\n')
Newton(f6,f6der,1.9,1e-5,20),print('\n\n')




#========== Fonction 7: ==========

def f7(x):
    return 3*x+4*math.log(x)-7

def f7der(x):
    return 3+4/x

print('========== Fonction 7: ==========\n')
Newton(f7,f7der,1.7,1e-5,20),print('\n\n')




#========== Fonction 8: ==========

def f8(x):
    return x**4-2*x**2+4*x-17

def f8der(x):
    return 4*x**3-4*x+4

print('========== Fonction 8: ==========\n')
Newton(f8,f8der,-2,1e-5,20)
Newton(f8,f8der,3,1e-5,20),print('\n\n')




#========== Fonction 9: ==========

def f9(x):
    return math.exp(x)-2*math.sin(x)-7

def f9der(x):
    return math.exp(x)-2*math.cos(x)

print('========== Fonction 9: ==========\n')
Newton(f9,f9der,3,1e-5,20),print('\n\n')




#========== Fonction 10: ==========

def f10(x):
    return math.log(x**2+4)*math.exp(x)-10

def f10der(x):
    return (2*x*math.exp(x))/(x**2+4)+math.log(x**2+4)*math.exp(x)

print('========== Fonction 10: ==========\n')
Newton(f10,f10der,2,1e-5,20),print('\n\n')




