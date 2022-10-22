def greetings():
    print("holaa")

def comprobar(nombre, list):
    for item in list:
        if item == nombre:
            return True
            break
    return False

def listador(list, _key):
    new_list = []
    for user in list:
        new_list.append(user[_key])
    return new_list




def read(list):
    print('--LISTAR--')
    print('total: ',len(list))
    print(list)

def find(list, keyBuscar):
    codes = listador(list, keyBuscar)
    print('--BUSCAR--')
    print('ingrese su ' + keyBuscar)
    dni = input()
    comprobador = comprobar(dni, codes)
    if comprobador == True:
        for user in list:
            if user[keyBuscar] == dni:
                index = list.index(user)
                print(list[index])
    elif comprobador == False:
        print('no se encontro el ' + keyBuscar)


def delete(list, keyEliminar):
    print("--ELIMINAR--")
    print('ingrese su ' + keyEliminar)
    code = input()
    for user in list:
        if user[keyEliminar] == code:
            index = list.index(user)
            eliminado = list.pop(index)
            print('valor eliminado:')
            print(eliminado)

