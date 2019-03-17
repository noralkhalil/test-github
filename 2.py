print ('hi')
print 'hi'


print (5+3)**2
print ('the sum 5+3 =' , 5+3)

value1 = 6+6
print (value1)
print ('the sum', value1)


value2 = 12
value3 ='text'
value4 =1.2
b= True
value5= bb=False
print (value2 , value3)


print (type (value1))
print (type (value2))
print type  (value3)
print type  (value4)
print type  (b)
print type  (value5)



bb= True
print (bb)

b= True and False
print (b)


print(int(True))    #immer  (True = 1)
print(int(False))   #immer  (False = 0)

print(float(False))
print(float(True))

print(True+6)
print(False+5)   #nur (True und False) konnen als Zahle(integer) ausgedruckt werden



v1=4.0
v2=5
av=(v1+v2)/2     #Rechenen: ( 4 + 5 = 9 ) d.h. ( int + int = int )
print (av)       #aber wenn irgend ein Zahl von diese (integre Zahlen) als (float) geschrieben ist, dann bekommen wir (float) ergebnis


print(divmod(10,3))        # Dieder Funktion (divomd) hilft, dass es uns das Ergebnis und den Rest gibt,
print(divmod (12,7))        # aber man muss achten, dass man ein Komma(,) zwischen die Zahlen hat und keine Geteiltdurch(/)


var1='Noralden'
var2='Alkhalil'
print(var1+var2)
print(var1+ ' '+var2)       # wir haben das hier (+''+) verwendet um platz zwischen die Namen zumachen


print('noralden'+ '\n' +'alkhalil')     #es ist gleich und es gibt keinen unterschied zwischen die Zeile (64 und 65)
print('Noralden\nAlkhalil')             #aber das ist einfacher

print ('Noralden\tAlkhalil')            # (\t) das hier macht 8spaces


print ("Noralden said \"hallo guys\"")      #slash vorteile


#print (+) wenn alle gleich sind z.b. { (int) mit (int) mit (int) }
#print (,)  wenn alle unterschiedlich sind z.b. { (str) mit (int) mit (float) mit ...... }



c='Nor is\nsmart'            #dieser schritt heisst (index)
print (c[0])
print (c[1])
print (c[2])
print (c[3])    #space wurde auch ausgedruckt
print (c[4])
print (c[5])
print (c[6])
print (c[7])    # (\n) auch wird gezeigt
print (c[8])
print (c[9])
print (c[10])
print (c[11])
print (c[-1])   # (-) heisst er zhlt zureuck
print (c[0:])   #doppel



mm= 'Hello people'

print mm.replace ( 'l' , '5' )

print (mm)          # hier kommt es normal wie es in zeile 94 geschrieben ist,  weil es wurde nicht in zeile 96 gespeichert)

bb = mm.replace ( 'l' , '5' )
print (bb)          #hier geht es schon weil wir als (bb) gespeichert haben




ss= 'Noralden is cs'    #  [():()]
print (ss[0:])          #doppelpunkt heisst bis zum Ende [0:]
print (ss[0:4])         #oder bis folgenden Zahl die danach geschrieben wurde [0:4]
# MERKMAL  letzte Zahl wurde nicht gezahlt ( zeile 110 steht bis nr. 4 aber er hat bis nummer 3 ) d.h. immer ein Zahl mehr eingeben


mm= '1234567891011121314151617181920'
print (mm[::])                              #nicht verstanden




print len(mm)       # er zahlt / sagt wie viele Buchstaben haeb ich
                    # aber das ist nur feur (str) /   (int) geht nicht



ss= 'milch , Brot , Mehl , Zucker'
print ss.split(' , ')               # Trennen


v1 = input('enter your favoret number \n         ')     # das ist nur feur Zahlen / oder Text aber mit ( '' oder "" )
v2 = input("Tippen Sie irrgendein taste ein  \n   ") # das ist fuer Zahlen und Buchstaben
v3 = input("Tippen Sie irrgendein taste ein  \n")


print 'Das Ergebnis ist =', v1 +v2 ** v3
print ('Das Ergebnis ist =' , v1 + v2 ** v3)     # gleichcer Ergebnis aber mit Klammern
