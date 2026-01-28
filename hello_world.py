print("hola, mundo")

name = "brook"
print("hola " + name)

print(4+5)

print(4-5)

print(8/2) #este seria division

print(8*2)

print(2**3) #este seria elevado al cuadrado

print(7+"8") #no puedeir entre comillas porque lo lee como texto
#this will throw an error

print(7 + 8,5) #inter + float es posible (conversión implicita)

print("a" + "b" + "c") #imprime abc

print("this " + "is " + "pretty " + "near!")  #imprime this is pretty near

base = 6
height = 3
area = (base*height)/2
print("the area of the triangle is:" + str(area))  #para sumar int + string se debe llamar a str()
                                                    entonces asi imprime the area of the triangle is 9.0
                                                    conversión explícita - cuando se escribe código para convertir manualmente un tipo de datos a otro usando una función de conversión de tipos de datos:

str() - convierte un valor (a menudo numérico) a un tipo de datos string 

int() - convierte un valor (normalmente un flotante) en un tipo de datos entero 

float() - convierte un valor (normalmente un entero) a un tipo de datos float 

# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
 
print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
 
# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.
opcion moderna
print(f"{salutation} {first_name} {middle_name} {last_name}, {suffix}") 
