stringDigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def longitudString(cadena):
  i = 0
  for c in cadena:
    i += 1

  return i

def esNumeroEntero(cadena):
  if (len(cadena) > 0):
    if(cadena[0] == "-"):
      cadena = cadena[1:]
  for c in cadena:
    if (c not in stringDigits):
      return False
  return cadena != ""

def trimEntero(cadena):
  #Comprobamos si es un número negativo
  esNegativo = cadena[0] == "-"
  if(esNegativo):
    cadena = cadena[1:]

  #Comprobamos si es cero o esta precedido de ceros
  cerosIzquierda = 0
  for c in cadena:
    if (c != "0"):
      break
    cerosIzquierda += 1
  cadena = cadena[cerosIzquierda:-2]

  #Si es negativo y no es 0, volvemos a añadir el signo
  if (esNegativo and cadena != "0"):
    cadena = "-"+cadena

  return cadena

num = ""
while(not esNumeroEntero(num)):
  num = input("Introduce un número entero: ")

num = trimEntero(num)
if (num[0] == "-"):
  print(f"El numero {num} es negativo")
elif (num == "0"):
  print(f"El numero {num} es cero")
else:
  print(f"El numero {num} es positivo")