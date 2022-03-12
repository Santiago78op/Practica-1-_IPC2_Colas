import os
from colorama import Fore
from datetime import datetime, timedelta
#Constructores
from Constructor.Cliente import Cliente
from Constructor.Pizza import Pizza
from Constructor.Ingredientes import Ingredientes
#listas
from Lista.ColaCliente import Cola_Cliente
from Lista.ColaPizza import Cola_Pizza
#Directorios
from Graphivz.Graphivz import Grafica_cola



class Menu():

    def __init__(self):
        self.datosOrden = 1
        self.salir = 0
        self.eliminarOrden = 2
        self.dasarrollador = 3


    def mostrar_menu(self) -> None:
        """
        Función que limpia la pantalla y muestra nuevamente el menu
        """
        os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
        print(Fore.CYAN,f'''\t<--Menu Principal-->\n
Selecciona una opción:\n
    \t{self.datosOrden}) - Cargar Orden
    \t{self.eliminarOrden}) - Desencolar Orden
    \t{self.dasarrollador}) - Desarrollador
    \t{self.salir}) - Salir\n''')


    def menu(self):
        graficar = Grafica_cola()
        lista_Clientes = Cola_Cliente()

        lista_time = []
        aux = ''
        cont = 0
        while True:

            self.mostrar_menu()

            opcionMenu = input("Inserta el numero de la opcion: >> ")
            print(Fore.MAGENTA)

            try:
                opcionMenu = int(opcionMenu)

                os.system('cls')

                if opcionMenu == self.datosOrden:

                    nombre = input("\nIngrese Nombre del Cliente: ")
                    nombre = str(nombre.upper())
                    nit = input("Ingrese NIT del Cliente: ")
                    str(nit)
                    time = input("Ingrese Hora Actual: ")
                    str(time)
                    numOrden = input("Ingrese Numero de Orden: ")
                    int(numOrden)
                    print("\n")

                    nuevoCliente = Cliente(nombre, nit, time, numOrden)
                    lista_Clientes.append(nuevoCliente)

                    if numOrden != None:

                        print(Fore.RED, "1) Ingesar Tipo de Pizza\n"
                                        " 0) salir")

                        opc = input("\nIngrese Opción: ")

                        if opc == "1":

                            print(Fore.YELLOW, "\nAgregar Ingredientes de la siguiente forma\n"
                                               "Para un ingrediente: ingrediente\n"
                                               "Para dos o mas Ingredientes: ingrediente1,ingredeinte2\n"
                                               "PEPPERONI,SALCHICHA,CARNE,QUESO Y PIÑA\n")

                            cliente = lista_Clientes.buscar(numOrden)
                            if cliente is None:
                                print("No tengo esa Orde")
                            else:
                                numOfPizza = input("Ingrese Cantidad Pizzas: ")
                                num = int(numOfPizza)

                                final_time = 0
                                cont = 0
                                total_time = 0

                                nuevaPizza = ''
                                for i in range(1, num + 1):
                                    tipoDePizza = input("\nIngrese Ingrediente de la Pizza: ")
                                    tipo = str(tipoDePizza.upper())
                                    datos = tipo.split(",")

                                    if len(datos) == 1:
                                        if datos[0] == "PEPPERONI":
                                            final_time = 3
                                            nuevaPizza = Pizza(i, datos[0])
                                            nuevoCliente.listPizza.append(nuevaPizza)
                                        elif datos[0] == "SALCHICHA":
                                            final_time = 4
                                            nuevaPizza = Pizza(i, datos[0])
                                            nuevoCliente.listPizza.append(nuevaPizza)
                                        elif datos[0] == "CARNE":
                                            final_time = 10
                                            nuevaPizza = Pizza(i, datos[0])
                                            nuevoCliente.listPizza.append(nuevaPizza)
                                        elif datos[0] == "QUESO":
                                            final_time = 5
                                            nuevaPizza = Pizza(i, datos[0])
                                            nuevoCliente.listPizza.append(nuevaPizza)
                                        elif datos[0] == "PIÑA":
                                            final_time = 2
                                            nuevaPizza = Pizza(i, datos[0])
                                            nuevoCliente.listPizza.append(nuevaPizza)
                                        else:
                                            print("Error en Ingrediente")
                                        cont = cont + final_time
                                    else:
                                        for tp in datos:
                                            if tp == "PEPPERONI":
                                                final_time = 3
                                                total_time = total_time + final_time
                                            elif tp == "SALCHICHA":
                                                final_time = 4
                                                total_time = total_time + final_time
                                            elif tp == "CARNE":
                                                final_time = 10
                                                total_time = total_time + final_time
                                            elif tp == "QUESO":
                                                final_time = 5
                                                total_time = total_time + final_time
                                            elif tp == "PIÑA":
                                                final_time = 2
                                                total_time = total_time + final_time
                                            else:
                                                print(Fore.LIGHTRED_EX, "Error en Ingrediente")
                                        nuevaPizza = Pizza(i, datos)
                                        nuevoCliente.listPizza.append(nuevaPizza)


                                total = total_time + cont
                                if int(numOrden) == 1:
                                    hora_1 = time.split(":")  # 6:10
                                    h1 = timedelta(hours=int(hora_1[0]), minutes=int(hora_1[1]))  # '['6','10']
                                    resultado = h1 + timedelta(minutes=int(total))  # 6:10 + 12 = 6:22
                                    resultado = str(resultado)
                                    lista_time.insert(0, resultado)
                                    nuevoTime = Ingredientes(resultado,resultado,0)
                                    nuevaPizza.listaType.append(nuevoTime)
                                else:
                                    hora_2 = lista_time[0].split(":")  # 6:22
                                    h2 = timedelta(hours=int(hora_2[0]), minutes=int(hora_2[1]))
                                    hora_1 = time.split(":")  # 6:15
                                    h1 = timedelta(hours=int(hora_1[0]), minutes=int(hora_1[1]))
                                    resultado_3 = h2 - h1  # 7min
                                    res = str(resultado_3)
                                    if res >= '00:00':
                                        resultado_2 = h1 + timedelta(minutes=int(total))  # 6:20
                                        resultado_4 = resultado_3 + resultado_2
                                        h3 = str(resultado_4)
                                        nuevoTime = Ingredientes(h3,time,total)
                                        nuevaPizza.listaType.append(nuevoTime,)
                                        lista_time.insert(0, h3)
                                    else:
                                        resultado_2 = h1 + timedelta(minutes=int(total))
                                        resultado_2 = str(resultado_2)
                                        nuevoTime = Ingredientes(resultado_2,time,total)
                                        nuevaPizza.listaType.append(nuevoTime)
                                        lista_time.insert(0, resultado_2)



                                c = lista_Clientes
                                cl = lista_Clientes.devolver_lista()


                                for cli in cl:
                                    print(Fore.RED,"Cliente", cli.numOfOrder)
                                    print(Fore.LIGHTWHITE_EX,"Nombre: ",cli.name,"Nit: ",cli.nit,"Start: ",cli.time,"Numero de Orden: ",cli.numOfOrder)
                                    pizz = cli.listPizza.retornarPizza()
                                    for pi in pizz:
                                        print(Fore.LIGHTWHITE_EX,Fore.LIGHTWHITE_EX,"Numero de Pizzas: ",pi.numOfPizza)
                                        print(Fore.LIGHTWHITE_EX,"Ingrediente: ", pi.type)
                                        ing = pi.listaType.retornar()
                                        for ins in ing:
                                            print(Fore.LIGHTWHITE_EX,"Tiempo de Espera: ", ins.time)


                                graficar.cola(c)
                elif opcionMenu == self.eliminarOrden:
                    print(Fore.RED,"No puede despachar Ordenes fuera del rango del tiempo")
                    print(Fore.RED, "Esto quiere decir que si Orden se entrega a las 6:22 no puede ser despachada a las 6:40\n")
                    lista_Clientes.recorrer()

                    out_time = input("\nIngrese Hora Despacho: ") #6:13
                    print("\n")
                    out_time = str(out_time)

                    lista_cliente = lista_Clientes.devolver_lista()
                    if len(lista_cliente) != 0:
                        for cliente in lista_cliente:
                            lista_pizzas = cliente.listPizza.retornarPizza()
                            for ingrdiente in lista_pizzas:
                                times = ingrdiente.listaType.retornar()
                                for Time in times:
                                    total_tiempo = Time.time
                                    if out_time <= total_tiempo:
                                        lista_Clientes.desencolar()
                                        lista_Clientes.recorrer()
                                        li = lista_Clientes.devolver_lista()
                                        lista = lista_Clientes
                                        if len(li) != 0:
                                            for element in li:
                                                Nt = element.time
                                                Pizz = element.listPizza.retornarPizza()
                                                for elemento in Pizz:
                                                    ing = elemento.listaType.retornar()
                                                    for ING in ing:
                                                        end_time = ING.result
                                                        second = ING.end
                                                        if out_time <= end_time:
                                                            switch = elemento.listaType.buscarIng(Nt)
                                                            for s in switch:
                                                                newTime = s.time
                                                                plus = s.end
                                                                hora_1 = newTime.split(":")
                                                                h1 = timedelta(hours=int(hora_1[0]),minutes=int(hora_1[1]))
                                                                resultado = h1 + timedelta(minutes=int(plus))
                                                                resultado = str(resultado)
                                                                elemento.listaType.switchElment(second,resultado)
                                                        elif out_time > end_time:
                                                            hora_1 = out_time.split(":")
                                                            h1 = timedelta(hours=int(hora_1[0]), minutes=int(hora_1[1]))
                                                            hora_2 = end_time.split(":")
                                                            h2 = timedelta(hours=int(hora_2[0]), minutes=int(hora_2[1]))
                                                            resultado = h1-h2
                                                            resultado_5 = resultado + timedelta(minutes=int(second))
                                                            resultado_6 = h2 + resultado_5
                                                            resultado_6 = str(resultado_6)
                                                            elemento.listaType.switchElment(second, resultado_6)
                                                        else:
                                                            print(Fore.RED,"ERRO!")
                                            graficar.cola(lista)
                                        else:
                                            print("Cola esta Vacia!!!!!!!")
                                    else:
                                        print(Fore.LIGHTMAGENTA_EX,"No puedo realizar la Accion Requerida!!!")
                    else:
                        print("Cola esta Vacia!!!!!!!")


                elif opcionMenu == self.dasarrollador:
                    print(Fore.LIGHTGREEN_EX,"Nombre: Santiago Julián Barrera Reyes -> Carne: 201905884")
                elif opcionMenu == self.salir:
                    print("\nEsto no es un adios sino un asta pronto!!!!!!\n")
                    False
                    break
                else:
                    print(Fore.YELLOW, 'Opcion no válida...')
                input('\nPresiona enter para Ingresar al Menú...')

            except ValueError as error:
                opcionMenu = -1
                print(Fore.RED, f'Error: {error}')
                print(Fore.RED, 'El programa no permite carateres tipo Caracter')
                input('Presione la tecla para continuar@')




m = Menu()
m.menu()