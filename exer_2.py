users = [
    {'dni':'123','nombre':'a','sexo':'hombre','edad':20},
    {'dni':'234','nombre':'b','sexo':'hombre','edad':20},
    {'dni':'345','nombre':'c','sexo':'hombre','edad':20},
]
#users=[]

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

def listarDni(list):
    new_list = []
    for user in list:
        new_list.append(user['dni'])
    return new_list

listDni = []

def user():
    dnis = listarDni(users)
    print('--DATOS--')
    print('ingrese su dni')
    dni = input()
    if len(dnis) > 0:
        comprobador = comprobar(dni, dnis)
        if comprobador == True:
            print('Este dni ya esta registrado')
            return 0
        elif comprobador == False:
            print('Ingrese su nombre')
            nombre = input()
            print('Ingrese su sexo')
            sexo = input()
            print('Ingrese su edad')
            edad = int(input())
            user = {
                'dni':dni,
                'nombre':nombre,
                'sexo':sexo,
                'edad':edad
            }

            return user
#
#for i in range(2):
#    user()
#
def create():
    print('¿cuantos usuarios desea registrar?')
    bucle = int(input())
    for i in range(bucle):
        new_user = user()
        if new_user == 0:
            continue
        users.append(new_user) 

def update():
    dnis = listarDni(users)
    print('--ACTUALIZAR--')
    print('ingrese su dni')
    dni = input()
    print('Ingrese su nombre')
    nombre = input()
    print('Ingrese su sexo')
    sexo = input()
    print('Ingrese su edad')
    edad = int(input())
    user = {
        'dni':dni,
        'nombre':nombre,
        'sexo':sexo,
        'edad':edad
    }
    if len(dnis) > 0:
        comprobador = comprobar(dni, dnis)
        if comprobador == True:
            for item in users:
                if item['dni'] == dni:
                    item['nombre'] = nombre
        elif comprobador == False:
            
            users.append(user)

def delete():
    print("--ELIMINAR--")
    print('ingrese su dni')
    dni = input()
    for user in users:
        if user["dni"] == dni:
            index = users.index(user)
            listDni.remove(dni)
            eliminado = users.pop(index)
            print('valor eliminado:')
            print(eliminado)

def read():
    print('--LISTAR--')
    print('total: ',len(users))
    print(users)

def find():
    dnis = listarDni(users)
    print('--BUSCAR--')
    print('ingrese su dni')
    dni = input()
    comprobador = comprobar(dni, dnis)
    if comprobador == True:
        for user in users:
            if user['dni'] == dni:
                index = users.index(user)
                print(users[index])
    elif comprobador == False:
        print('no se encontro el DNI')

def promedioEdad():
    edades = []
    for user in users:
        edades.append(float(user['edad']))
    promedios = promedio(edades)
    print("promedio de pacientes")
    print(promedios)

print('''
Que accion desea hacer
[1] : Registrar nuevo paciente
[2] : Modificar paciente con dni
[3] : Eliminar paciente
[4] : Buscar paciente
[5] : Mostrar todos los pacientes
[6] : Mostrar promedio de edad de los pacientes
''')
o = input()
if o == '1':
    create()
elif o == '2':
    update()
elif o == '3':
    delete()
elif o == '4':
    find()
elif o == '5':
    read()
elif o == '6':
    promedioEdad()
else:
    print('no es valida esa opcion, Adiós')