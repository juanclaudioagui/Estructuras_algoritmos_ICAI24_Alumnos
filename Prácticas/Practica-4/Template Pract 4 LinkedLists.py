"""
    Descripción: Práctica 4 de Algoritmos y Estructuras de Datos.
                Creación de listas enlazadas
    Autor: Atilano Fernández-Pacheco Sánchez-Migallón
    Updated Juan C. Agui ( actualizado a Pep-8)
    Fecha: 28/01/2022 / Feb 24
"""
class Equipo:
    def __init__(self, nombre=None, estadio=None, capacidad_estadio=None, num_ligas=0, num_copas_europa=0):
        self.nombre            = nombre
        self.estadio           = estadio
        self.capacidad_estadio = capacidad_estadio
        self.num_ligas         = num_ligas
        self.num_copas_europa  = num_copas_europa
        self.next              = None
        
    # __str__ () nos permite imprimir un objeto con una descripción clara
    def __str__(self):
        return f"Equipo: Nombre: {self.nombre}, Estadio: {self.estadio}, {self.capacidad_estadio} Seats, Ligas:{self.num_ligas}, Champions:{self.num_copas_europa}"
    
    # __repr__() permite al debugger mostrar una visualización clara del objeto
    def __repr__(self) -> str:
        return self.__str__()
        
class ListaEnlazada:
    
    # Constructor
    def __init__(self):
        # la lista está iniciamente vacía.
        self.head=None
    
    def __str__(self):
        return f"Lista Enlazada con {self.num_nodos()} Equipos"
        
    def num_nodos(self) -> int:
        """
            retorna el número de nodos en la lista
        Returns:
            int: 
        """
        node = self.head
        
        if node is None: 
            count = 0 
        else:
            count = 1
            while node.next is not None:
                node = node.next 
                count += 1
        return count
    
    def anadir_nodo_principio(self,nuevo_nodo:Equipo,TRACE=False):
        """
            Inserta el nodo dado al ppio de la lista
        Args:
            nuevo_nodo (Equipo): nodo a insertar. Debe incorporar el memberdata ".next"
            TRACE (bool, optional): Activa la traza por pantalla de la ejecución. 
                   Defaults to False
        """
        if TRACE:
            print (f"Trace:: Insertando equipo {nuevo_nodo.nombre} al ppio de la lista")
        
        # asegura que el next el nodo nuevo es igual al head de la lista ( un nodo, o None... )        
        nuevo_nodo.next = self.head
        
        # asegura que el head de la lista es el nuevo nodo....
        self.head = nuevo_nodo
            
    def mostrar_lista(self):
        pass
      
    def buscar_nodo_por_nombre(self, nombre):
        pass
      
    def borrar_node_por_nombre(self, nombre):
        pass
       
    def actualizar_nodo(self, nombre,nodo):
        # busca un nodo por nombre dado y lo reemplaza por el nodo dado
        pass
    
    def borrar_list(self):
        pass
      
    def anadir_nodo_final(self,nodo=Equipo()):
        pass
############################################################################
############################################################################
# Si quieres utilizar el menú descomenta las líneas siguientes

# def Menu():
#     print("MENU");
#     print("1. Insertar un nuevo equipo.")
#     print("2. Borrar un equipo.")
#     print("3. Buscar equipo por nombre de equipo.")
#     print("4. Listar todos los Equipos del Sistema. ");   
#     print("5. Actualizar nodo.")
#     print("6. Borrar toda la lista enlazada.")
#     print("7. Salir.")
#     opc=int(input("Introduzca una opcion: "))
#     return opc           

# if __name__ == "__main__":
#     lista=ListaEnlazada()
#     opc=Menu()
#     while(opc!=7):
#         if (opc==1):
#             pass
            
#         elif (opc==2):
#             pass
            
#         elif(opc==3):
#             pass
          
#         elif(opc==4):
#             pass
           
#         elif(opc==5):
#             pass
          
#         elif(opc==6):
#             pass
           
#         elif(opc==7):
#             print("Gracias por utilizar software ICAI")
#         opc=Menu()


#################################################################33
#################################################################33
# Driver code... para probar funcionalidades básicas

realMadrid = Equipo('RealMadrid', 'Bernabeu',100000)
barcelona = Equipo('Barcelona CF', 'Montjuic',500)
print (realMadrid)
print (barcelona)
le = ListaEnlazada()
print (le)
le.anadir_nodo_principio(realMadrid,TRACE=True)
print (le)
le.anadir_nodo_principio(barcelona,TRACE=True)
print (le)

