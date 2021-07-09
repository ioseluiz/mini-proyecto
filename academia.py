from tabulate import tabulate

profesores = [

    {
    'cedula': '8-111-333',
    'nombre': 'Kevin',
    'apellido': 'Jimenez',
    'direccion': 'Bella Vista calle 77',
    'telefono': '6345-7845'
    },
    {
     'cedula': '8-222-444',
    'nombre': 'Antonio',
    'apellido': 'Gonzalez',
    'direccion': 'San Francisco calle 53',
    'telefono': '6345-7845'   
    }

]

 

cursos = [{
            'codigo_curso': '001',
            'nombre': 'ingles',
            'duracion_horas': 60,
            'fecha_inicio': '2021-07-30',
            'fecha_fin': '2021-10-31',
            'estudiantes_permitidos': 30,
            'cedula_profesor': '8-222-444',
            'estudiantes_matriculados': ['8-791-273']
    },
    {
            'codigo_curso': '002',
            'nombre': 'Fisica',
            'duracion_horas': 80,
            'fecha_inicio': '2021-08-30',
            'fecha_fin': '2021-12-31',
            'estudiantes_permitidos': 25,
            'cedula_profesor': '8-111-333',
            'estudiantes_matriculados': ['8-791-273','9-790-2372'] 
    },

        {
            'codigo_curso': '003',
            'nombre': 'Matematicas',
            'duracion_horas': 100,
            'fecha_inicio': '2021-08-30',
            'fecha_fin': '2021-12-31',
            'estudiantes_permitidos': 15,
            'cedula_profesor': '8-111-333',
            'estudiantes_matriculados': [] 
    }

    ]

empresas = [
    {
    'nombre': "Banco General",
    'direccion': "Costa del Este via principal",
    'telefono': '270-0101'
    },
    {
         'nombre': "ACP",
        'direccion': "Balboa Ancon",
        'telefono': '276-1010'
    }
]

alumnos = [

        {
            'cedula': '8-791-273',
            'nombre':'Jose',
            'apellido': 'Munoz',
            'edad': 23,
            'direccion': 'Villa Lucre calle 20',
            'telefono': '6888-8888',
            'trabaja':'si',
            'nombre_empresa': 'ACP',
            'cursos_matriculados': ['001','002'],
            'notas':[{'codigo_curso': '001', 'evaluacion': 97},
                    {'codigo_curso': '002', 'evaluacion': 95}]
        },
        {
            'cedula': '9-790-2372',
            'nombre':'Maria',
            'apellido': 'Robles',
            'edad': 28,
            'direccion': 'Santiago calle 2',
            'telefono': '6634-2020',
            'trabaja':'no',
            'nombre_empresa': '',
            'cursos_matriculados': ['002'],
            'notas':[{'codigo_curso': '002', 'evaluacion': 80}
                    ]
        }
    ]

#####################################################################################################
# Funciones de Tabla Cursos
def cursos_buscar(codigo_curso):
    for curso in cursos:
        if codigo_curso == curso['codigo_curso']:
            return curso
        else:
            resultado = "No existe ese curso"
    return resultado

 

def cursos_buscar_indice(codigo_curso):
    for curso in cursos:
        if codigo_curso == curso['codigo_curso']:
            return cursos.index(curso)
        else:
            resultado = "No existe este curso"
    return resultado
 
def listar_cursos():
    cadena = ""
    for curso in cursos:
        cadena += f"{curso['codigo_curso']}-{curso['nombre']}, "

    print(f"Listado de Cursos registrados: {cadena[:-2]} ")
    print(tabulate(cursos, headers="keys", tablefmt="psql"))

def agregar_curso(codigo, nombre, duracion_horas, fecha_inicio, fecha_fin,estudiantes_permitidos, cedula_profesor,estudiantes_matriculados):
    datos_curso = {

            'codigo_curso': codigo,
            'nombre': nombre,
            'duracion_horas':duracion_horas,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'estudiantes_permitidos': estudiantes_permitidos,
            'cedula_profesor': cedula_profesor,
            'estudiantes_matriculados': estudiantes_matriculados

    }
    cursos.append(datos_curso)
    print("El curso se agrego de forma exitosa!")
    print("")
    listar_cursos()

def reg_cursos():
    print("REGISTRO DE CURSOS")
    listar_cursos()
    print("")
    registrar = input('¿Desea registrar un nuevo curso? si/no: ')
    if registrar == 'si':
        print("Ingresar Curso")
        codigo_curso = input('Ingresar codigo del curso:')
        nombre = input('Ingresar Nombre del Curso: ')
        duracion_horas = input('Ingresar duracion en horas: ')
        fecha_inicio = input('Ingresar Fecha de Inicio: ')
        fecha_fin = input('Ingresar Fecha de Finalizacion: ')
        estudiantes_permitidos = input('Ingresar estudiantes permitidos: ')
        cedula_profesor = input('Ingresar cedula del profesor: ')
        estudiantes_matriculados = []
        agregar_curso(codigo_curso, nombre, duracion_horas, fecha_inicio, fecha_fin, estudiantes_permitidos, cedula_profesor,estudiantes_matriculados)


################################################################################################################
# Funciones de Tabla Profesores
def profesores_buscar(cedula):
    for profesor in profesores:
        if cedula == profesor['cedula']:
            return profesor
        else:
            resultado = "No existe ese profesor"
    return resultado

def profesores_agregar(cedula, nombre, apellido, direccion, telefono):
    resultado = profesores_buscar(cedula)
    if resultado == "No existe ese profesor":
        datos_profesor = {
            'cedula': cedula,
            'nombre': nombre,
            'apellido': apellido,
            'direccion': direccion,
            'telefono': telefono
        }

        profesores.append(datos_profesor)
        mensaje = "Profesor agregado satisfactoriamente"
        return mensaje

    return "Ya existe un profesor con esa cedula"

def listar_profesores():
    cadena = ""
    for profesor in profesores:
        cadena += f"{profesor['nombre']} {profesor['apellido']}, "
    print(f"Listado de Profesores: {cadena[:-2]}")
    print(tabulate(profesores, headers="keys", tablefmt="psql"))

def registro_profesores():
    print('REGISTRO DE PROFESORES')
    listar_profesores()
    print("")
    registrar = input('¿Desea registrar un nuevo profesor? si/no: ')
    if registrar == 'si':
        cedula = input('Ingresar cedula de profesor: ')
        nombre = input('Ingresar nombre de profesor: ')
        apellido = input('Ingresar apellido de profesor: ')
        direccion = input('Ingresar direccion de profesor: ')
        telefono = input('Ingresar telefono de profesor: ')
        
        profesores_agregar(cedula, nombre, apellido, direccion, telefono)
        print('Profesor registrado de forma exitosa!')
        listar_profesores()
        print("")


#############################################################################################################
# Funciones de Tabla Alumnos
def registro_alumnos():
    listar_alumnos()
    print("")
    registrar = input('¿Desea registrar un nuevo alumno? si/no: ')
    if registrar == 'si':
        print("Ingresar Alumno")
        cedula = input('Ingresar cedula: ')
        nombre = input('Ingresar nombre: ')
        apellido = input('Ingresar apellido: ')
        edad = input('Ingresar edad: ')
        telefono = input('Ingresar telefono: ')
        direccion = input('Ingresar direccion: ')
        trabajo = input('¿Estudiante trabaja? si/no: ')

        if trabajo == 'si':
            mostrar_empresas()
            nombre_empresa = input('Ingrese el nombre de la empresa de la lista: ')
        elif trabajo == 'no':
            nombre_empresa = ""

        datos_alumno = {
                'cedula': cedula,
                'nombre':nombre,
                'apellido': apellido,
                'edad': int(edad),
                'direccion': direccion,
                'telefono': telefono,
                'trabaja':trabajo,
                'nombre_empresa': nombre_empresa,
                'cursos_matriculados': [],
                'notas':[]

        }

        alumnos.append(datos_alumno)
        print('Alumno registrado de forma exitosa!')
        listar_alumnos()
        print("")


def listar_alumnos():
    cadena = ""
    for alumno in alumnos:
        cadena += f"{alumno['nombre']} {alumno['apellido']}, "
    print(f"Listado de Alumnos: {cadena[:-2]}")
    print(tabulate(alumnos, headers="keys", tablefmt="psql"))

 
def alumnos_buscar(cedula):
    for alumno in alumnos:
        if cedula == alumno['cedula']:
            return alumno
        else:
            resultado = "No existe ese alumno"
    return resultado

 
def alumnos_buscar_indice(cedula):
    for alumno in alumnos:
        if cedula == alumno['cedula']:
            return alumnos.index(alumno)
        else:
            resultado = "No existe este alumno"

    return resultado

 
###############################################################################################################
# Funciones de Tabla Empresas
def empresas_buscar(nombre):
    for empresa in empresas:
        if nombre == empresa['nombre']:
            return empresa
        else:
            resultado = "No existe esta empresa"

        return resultado


def empresas_agregar(nombre, direccion, telefono):
    resultado = empresas_buscar(nombre)
    if resultado == "No existe esta empresa":
        datos_empresa = {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono
        }
        empresas.append(datos_empresa)
        mensaje = "Empresa agregada satisfactoriamente"
        return mensaje

    return "Ya existe una empresa con ese nombre"
def mostrar_empresas():
    cadena = ""
    for empresa in empresas:
        cadena += f"{empresa['nombre']}, "

    print(f"Lista de Empresas registradas: {cadena[:-2]}")
    print(tabulate(empresas, headers="keys", tablefmt="psql"))

def registro_empresas():
    mostrar_empresas()
    print("")
    registrar = input('¿Desea registrar una nueva empresa? si/no: ')
    if registrar == 'si':
        print("Ingresar Empresa")
        print("")
        nombre = input('Ingresar nombre de la Empresa: ')
        direccion = input('Ingresar direccion de la Empresa: ')
        telefono = input('Ingresar telefono de la Empresa: ')
        empresas_agregar(nombre, direccion, telefono)
        print('Alumno registrado de forma exitosa!')
        print("")
        mostrar_empresas()
        print("")

##############################################################################################################################
# Acciones
def matricula_alumno():
    print('Matricula')
    print("")
    print('Listado de Cursos')
    listar_cursos()
    cedula = input('Ingrese la cedula del alumno: ')
    codigo_curso = input('Ingrese el codigo del curso: ')
    cursos_matricular(cedula, codigo_curso)

def cursos_matricular(cedula_alumno,codigo_curso):
    curso = cursos_buscar(codigo_curso)
    alumno = alumnos_buscar(cedula_alumno)
    indice_curso = cursos_buscar_indice(codigo_curso)
    indice_alumno = alumnos_buscar_indice(cedula_alumno)
    #print(indice_alumno)
    if len(curso['estudiantes_matriculados']) <  int(curso['estudiantes_permitidos']):
        cursos[indice_curso]['estudiantes_matriculados'].append(cedula_alumno)
        alumnos[indice_alumno]['cursos_matriculados'].append(codigo_curso)
        notas = {'codigo_curso': codigo_curso,
                  'evaluacion': 0}
        alumnos[indice_alumno]['notas'].append(notas)
        #print(cursos[indice_curso]['estudiantes_matriculados'])
        #print(alumnos[indice_alumno]['cursos_matriculados'])
        print(f"Alumno con cedula {alumno['cedula']} matriculado en el curso {curso['nombre']}")
    else:
        print(f"No fue posible la matricula. El curso {curso['nombre']} ya no tiene cupos disponibles.")
def actualizar():
    cedula = input('Ingresar cedula del alumno: ')
    codigo_curso = input('Ingresar el Codigo del curso: ')
    evaluacion = input('Ingresar nota: ')
    actualizar_notas(cedula, codigo_curso, evaluacion)
# Actualizar Notas
def actualizar_notas(cedula_alumno, codigo_curso, evaluacion):
    alumno = alumnos_buscar(cedula_alumno)
    curso = cursos_buscar(codigo_curso)
    indice_alumno = alumnos_buscar_indice(cedula_alumno)

    # Verificar que el alumno esta matriculado en ese curso
    if codigo_curso in alumno['cursos_matriculados']:
        indice_curso = alumno['cursos_matriculados'].index(codigo_curso)
        alumnos[indice_alumno]['notas'][indice_curso]['evaluacion'] = evaluacion
        print(f"Evaluacion del alumno con cedula {cedula_alumno} en el curso {curso['nombre']} ha sido actualizada")

# Consulta cursos matriculados por un estudiante
def consulta_cursos_matriculados(cedula_alumno):
    alumno = alumnos_buscar(cedula_alumno)
    return alumno['cursos_matriculados']

# Consulta cursos dictados por un profesor X

def consulta_cursos_dictados_profesor(cedula_profesor):
    profesor = profesores_buscar(cedula_profesor)
    cadena = ""
    for curso in cursos:
        if cedula_profesor == curso['cedula_profesor']:
            print(curso['nombre'])
            cadena += f"{curso['nombre']}, "
    print(f"El Profesor {profesor['nombre']} {profesor['apellido']} dicta los siguientes cursos: {cadena[:-2]}")

# Consulta de cursos tomados por un alumno y su evaluacion
def consulta_cursos_evaluaciones_alumno(cedula_alumno):
    alumno = alumnos_buscar(cedula_alumno)
    print(f"El alumno {alumno['nombre']}  {alumno['apellido']} tiene las siguientes calificaciones: ")

    for nota in alumno['notas']:
        codigo_curso = nota['codigo_curso']
        curso = cursos_buscar(codigo_curso)
        calificacion = nota['evaluacion']
        print(f"{curso['nombre']}: {calificacion}")

# Consulta de curso con mayor numero de estudiantes matriculados
def consulta_curso_mayor_cant_estudiantes():
    cantidades = []
    for curso in cursos:
        estudiantes_matriculados = len(curso['estudiantes_matriculados'])
        cantidades.append(estudiantes_matriculados)
    cant_mayor_estudiantes = max(cantidades)
    indice_curso = cantidades.index(cant_mayor_estudiantes)
    curso_max = cursos[indice_curso]
    print(f"El curso {curso_max['nombre']} es el curso con mayor numero de estudiantes matriculados. Tiene {cant_mayor_estudiantes} matriculados. ")

def consultas():
    print("MENU DE CONSULTAS")
    print('')
    print('1. Cursos matriculados por Estudiante')
    print('2. Cursos dictados por profesor')
    print('3. Cursos tomados por alumno y su evaluacion')
    print('4. Curso con mayor cantidad de alumnos matriculados')
    print('5. Regresar al menu principal.')
    opcion = input("Ingrese opcion: ")
    if opcion == '1':
        cedula = input('Ingrese la cedula del estudiante: ')
        alumno = alumnos_buscar(cedula)
        cursos_matriculados = consulta_cursos_matriculados(cedula)
        print(f"Cursos Matriculados por el alumno {alumno['nombre']} {alumno['apellido']}:")
        for curso in cursos_matriculados:
            nombre = cursos_buscar(curso)['nombre']
            print(nombre)
            print("")
        main()
    elif opcion == '2':
        cedula = input('Ingrese la cedula del profesor: ')
        consulta_cursos_dictados_profesor(cedula)
        main()
    elif opcion == '3':
        cedula = input('Ingrese la cedula del estudiante: ')
        consulta_cursos_evaluaciones_alumno(cedula)
        main()
    elif opcion == '4':
        consulta_curso_mayor_cant_estudiantes()
        main()
    elif opcion == '5':
        main()


###################################################################################################################################################

def main():

    #print(profesores)
    #print(cursos)
    #curso = cursos_buscar('001')
    #print(curso)
    #profesor = profesores_buscar('8-222-444')
    #print(profesor)
    #alumno = alumnos_buscar('9-790-2372')
    #print(alumnos)
    #print(cursos)
    #cursos_matricular('9-790-2372', '001')
    #print(alumnos)
    #print(cursos)
    #profesores_agregar('6-111-222','Sergio', 'Vega', 'Albrook','6555-0000')
    #print(profesores)
    #actualizar_notas('9-790-2372', '001',87)
    #print(alumnos)
    #consulta_cursos_dictados_profesor('8-111-333')
    #consulta_cursos_evaluaciones_alumno('9-790-2372')
    #consulta_curso_mayor_cant_estudiantes()
    menuControl = True

    while menuControl:

        print("SISTEMA DE MATRICULA")
        print('')
        print('1. Registro Alumnos')
        print('2. Empresas registradas')
        print('3. Registro de curso')
        print('4. Registro de profesores')
        print('5. Matricularse en curso')
        print('6. Actualizar notas')
        print('7. Consultas')
        print('8. Salir')
        opcion = input("Ingrese opcion: ")
        if opcion == '1':
            registro_alumnos()
        elif opcion == '2':
            registro_empresas()
        elif opcion == '3':
            reg_cursos()
        elif opcion == '4':
            registro_profesores()
        elif opcion == '5':
            matricula_alumno()
        elif opcion == '6':
            actualizar()
        elif opcion == '7':
            consultas()
            break
        elif opcion == '8':
            print('saliendo del sistema, que tengas un buen dia')
            menuControl = False
            break
        else:
            print("error opcion no valida")

if __name__ == '__main__':
    main()

 
