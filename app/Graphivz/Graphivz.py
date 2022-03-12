from Lista.ColaCliente import Cola_Cliente
import os

class Grafica_cola():

    def __init__(self):
        self.cadena = ''

    def cola(self,c=Cola_Cliente()):

        clientes = c.devolver_lista()

        digraph = '''
        digraph R {
            node [shape=box fillcolor="#FFEDBB" style=filled]

            subgraph cluster_p{
            label = "Lista tipo Cola Ordenes Pizza Entrega"
            raiz[label = "Ordenes"]
            bgcolor = "#398D9C"
            edge[dir = "both"]
            Fila1[label="En Cola", group=1,fillcolor=green];
        '''

        i = 1
        for dato in clientes:
            cadena = f"Orden: {dato.numOfOrder}\nStart: {dato.time}\n"
            digraph = (digraph+'''
            Columna'''+str(i)+'''[label="'''+str(cadena)+'''",group=2,fillcolor=brown];
            ''')
            i = i+1


        if len(clientes)==1:
            cadena = ''
            digraph = (digraph+
            cadena
                )
        else:
            cadena = ''
            for i in range(1,len(clientes)):
                cadena = '''Columna'''+str(i)+'''->Columna'''+str(i+1)+"\n"
                digraph = (digraph+cadena)

        digraph = (digraph +'''
            raiz->Fila1;
            raiz->Columna1;
            ''')

        cadena = ''
        pt = ';'
        for i in range(1,len(clientes)+1):
            cadena = cadena + '''Columna'''+str(i)+str(pt)

        digraph = (digraph+ '''
            {rank=same;raiz;'''+cadena+'''}
        ''')


        cadena = ''
        aux = ''
        cont = 1
        for i in clientes:
            cantidad = i.listPizza.retornarPizza()
            for l in cantidad:
                temp = f"Pizzas: {l.numOfPizza}"
                cadena = str(temp)+"\n"
                tempo = l.listaType.retornar()
                for j in tempo:
                    temp = f"End: {j.time}"
                    cadena = cadena + str(temp)+""
            aux = '''nodo1_''' + str(cont)
            digraph = (digraph +
            aux + '''[label="''' + str(cadena) + '''",fillcolor="#66CDAA",group=2]
                    ''')
            cont = cont + 1


        digraph = (digraph + '''
            Fila1->nodo1_1;
        ''')

        if len(clientes)==1:
            cadena=''
            digraph = (digraph+cadena)
        else:
            for i in range(1,len(clientes)):
                cadena = ('''nodo1_'''+str(i)+'''->nodo1_'''+str(i+1)+''';''')
                digraph = (digraph + cadena)

        cadena = ''
        pt = ';'
        for i in range(1, len(clientes) + 1):
            cadena = cadena + '''nodo1_''' + str(i) + str(pt)

        digraph = (digraph+'''
            {rank=same;Fila1;'''+cadena+'''}
        ''')

        for i in range(1,len(clientes)+1):
            digraph = (digraph+'''
            Columna'''+str(i)+'''->nodo1_'''+str(i)+''';''')

        digraph = (digraph+'''
            }
        }
        ''')


        ruta = 'Graphivz\\imagen.txt '
        file = open(ruta, 'w')
        file.write(f"{digraph}")
        file.close()
        ver = "dot -Tpng Graphivz\\imagen.txt -o Graphivz\\grafica.png"
        status = os.system(ver)
        img = "Graphivz\\grafica.png"
        stado = os.startfile(img)

