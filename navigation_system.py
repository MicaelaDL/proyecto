from algo1 import *
import sys

def create(local_path):
  # código para probar sys (puede ser borrado)
  with open(local_path,'r') as f:
    flota_list = f.readlines()
  print(flota_list) 

  return #lo puse para no tener problemas con el resto del código... se puede borrar obviously

"================================================================================="
"FUNCIONES SYS MODULE"

if len(sys.argv) > 1:  
  if sys.argv[1] == "-create":
    create(sys.argv[2]) # el argv 2 debería ser el archivo o la ubicación de este
  else:
    print ("Error (╥﹏╥)") 
