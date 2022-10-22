list_name = []
list_price = []

def comprobar(nombre, list):
    for item in list:
        if item == nombre:
            return True
            break
    return False

def promedio(list):
    promedio = 0
    for item in list:
        promedio = promedio + item
    promedio = promedio / len(list)
    return promedio

def buscarEnListaPosicion(number, list):
    encontrados = []
    for index in range(len(list)):
        if number == list[index]:
            encontrados.append(index)
    return encontrados

def buscarEnLista(listPosicion, list):
    items = []
    for item in listPosicion:
        items.append(list[item])
    return items

for i in range(2):
    
    while True:
        name = input("dame el nombre")
        comprueba_nombre = comprobar(name,list_name)
        if comprueba_nombre == True:
            print("ey, el nmombre ya esta registrado")
            pass
        else:
            list_name.append(name)
            break

    price = input("dame  el precio")
    list_price.append(float(price))
    
print(list_name)
print(list_price)
promedio = promedio(list_price)
print(promedio)

maximo = max(list_price)
print("Precio mas alto: ", maximo)
itemsPosicion = buscarEnListaPosicion(maximo,list_price)
itemsProducts = buscarEnLista(itemsPosicion, list_name)
print('--prodcuts--')
print(itemsProducts)

