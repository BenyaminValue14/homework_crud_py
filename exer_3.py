from asyncio.windows_events import NULL
from queue import Empty
import modules.crud as crud

productos = [
    {
        "code":'123',
        "name":"a",
        "brand":"express",
        "cost":5,
        "price":12,
        "stock":100
    }
]
crud.greetings()

def product():
    codes = crud.listador(productos,'code')
    print('--DATOS--')
    print('ingrese su código')
    code = input()
    if len(codes) > 0:
        #comprobador = comprobar(dni, dnis)
        comprobador = crud.comprobar(code, codes)
        if comprobador == True:
            print('Este codigo ya esta registrado')
            return
        elif comprobador == False:
            print('Ingrese su nombre')
            nombre = input()
            print('Ingrese la marca')
            marca = input()
            print('Ingrese el precio de compra')
            costo = float(input())
            print('Ingrese el precio de venta')
            venta = float(input())
            print("Ingrese el stock del produ cto")
            stock = int(input())

            user = {
                "code":code,
                "name":nombre,
                "brand":marca,
                "cost":costo,
                "price":venta,
                "stock":stock
            }

            return user
    return 0

def register():
    new_product = product()
    if new_product != 0:
        productos.append(new_product)


def update(list, keyBuscar):
    dnis = crud.listador(list, keyBuscar)
    print(dnis)
    print('--ACTUALIZAR--')
    print('ingrese su código')
    code = input()
    print('Ingrese su nombre')
    nombre = input()
    print('Ingrese la marca')
    marca = input()
    print('Ingrese el precio de compra')
    costo = float(input())
    print('Ingrese el precio de venta')
    venta = float(input())
    print("Ingrese el stock del produ cto")
    stock = int(input())
    user = {
        "code":code,
        "name":nombre,
        "brand":marca,
        "cost":costo,
        "price":venta,
        "stock":stock
    }
    if len(dnis) > 0:
        comprobador = crud.comprobar(code, dnis)
        if comprobador == True:
            for item in list:
                if item[keyBuscar] == code:
                    item["name"] = nombre
                    item["brand"] = marca
                    item["cost"] = costo
                    item["price"] = venta
                    item["stock"] = stock
        elif comprobador == False:
            
            productos.append(user)
    print(list)


print('''
Que accion desea hacer
[1] : Registrar nuevo paciente
[2] : Modificar paciente con dni
[3] : Eliminar paciente
[4] : Buscar paciente
[5] : Listar todos los pacientes
[6] : salir
''')
o = input()
if o == '1':
    register()
elif o == '2':
    update(productos,'code')
elif o == '3':
    crud.delete(productos,'code')
elif o == '4':
    crud.find(productos,'code')
elif o == '5':
    crud.read(productos)
elif o == '6':
    print('adios!')
else:
    print('no es valida esa opcion, Adiós')