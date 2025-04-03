#1 
#print("Hola, ya se imprimir frases")

#2
#print (int(273))

#3
#print (2.3)

#4
#print(1234+532)

#5
#print(1234-532)

#6
#print(1234*532)

#7
#print(1234/532)

#8 
#c=0
#x=0
#while c<3:
#    print(x+1)
#    c+=1
#    x+=1

#9
#for i in range(1, 10):
#    print(i)

#10
#for i in range(1, 10001):
#    print(i)

#11
#for i in range(5, 11):
#    print(i)
 
#12
#for i in range(5, 16):
#    print(i)

#13
#for i in range(5, 15001):
#    print(i)

#14
#for i in range (200):
#    print ("hola")

#15
#for i in range (1, 31):
#    print (i**2)

#16
#x=1
#for i in range(2, 21):
#    x=x*i
#print(x)

#17
#x=0
#for i in range (1,101):
#    x=x+(i**2)
#print(x)

#18
#x=int(input())
#s=0
#for i in range(x + 1, x + 101):
#    s += i 
#print(s)

#19
#euro=float(input())
#dolar=euro*1.11
#print (dolar)

#20
#x=float(input())
#y=float(input())
#print(x*y)

#21
#x=float(input())
#y=float(input())
#if x>y:
#    print(f"{x} es mayor y {y} es menor")
#if x<y:
#    print(f"{y} es mayor y {x} es menor")
#if x==y:
#    print("son iguales")

#22
#x=int(input())
#for i in range(x, 0, -1):
#    if (i%2)!=0:
#        print(i)

#23
#a=int(input())
#b=int(input())
#while b!=0:
#    a, b=b, a%b
#print(a)

#24
#a=int(input())
#b=int(input())
#c=int(input())
#d= (b**2)-(4*a*c)
#if d>0:
#    print(f"La ecuacion de segundo grado con los coeficientes {a}, {b}, {c}, tiene dos soluciones reales")
#    x1= (-b + (d)**(1/2))/(2*a)
#    x2= (-b - (d)**(1/2))/(2*a)
#    print(f"Las soluciones son {x1} y {x2}")
#if d==0:
#    print(f"La ecuacion de segundo grado con los coeficientes {a}, {b}, {c}, tiene una unica solucion real")
#    x1= (-b + (d)**(1/2))/(2*a)
#    print(f"La solucion es {x1}")
#if d<0:
#    print(f"La ecuacion de segundo grado con los coeficientes {a}, {b}, {c} no tiene solucion en los reales")

#25 recursividad, caso base y caso recursivo.
#def factorial(n):
#    if n==0:
#        return 1
#    else:
#        return n * factorial(n-1)
#print(factorial(5))

#def ackermann(m, n):
#    if m==0:
#        return n+1
#    if n==0:
#        return ackermann(m-1, 1)
#    else:
#        return ackermann(m-1, ackermann(m, n-1))
#print(ackermann(1,2))

#26
#a=int(input())
#b=int(input())
#c=int(input())
#if a>b and a>c and b>c:
#    print(f"{a} es el mayor y {c} es el menor")
#if a>b and a>c and c>b:
#    print(f"{a} es el mayor y {b} es el menor")
#if b>a and b>c and a>c:
#    print(f"{b} es el mayor y {c} es el menor")
#if b>a and b>c and c>a:
#    print(f"{b} es el mayor y {a} es el menor")
#if c>a and c>b and a>b:
#    print(f"{c} es el mayor y {b} es el menor")
#if c>a and c>b and b>a:
#    print(f"{c} es el mayor y {a} es el menor")

#27
#f=float(input())
#def c(f):
#    return (5/9)*(f-32)
#while f!=999:
#   print(c(f))
#    f=float(input())
#print("Programa finalizado")

#28

#29

#30
#n=int(input())
#for i in range(2, n+1):
#    primo = True
#    for j in range (2, i):
#        if (i%j)==0:
#            primo = False
#            break
#    if primo:
#        print(i)   