# """
#     Descripción: Práctica 4 de Algoritmos y Estructuras de Datos.
#                 Creación de listas enlazadas
#     Autor: Atilano Fernández-Pacheco Sánchez-Migallón
#     Fecha: 28/01/2022
    
#     Implementado por JCA, Feb 23
    
#     Esta versión requiere que el objeto a gestionar en la lista enlazada herede de la clase Node, ç
#     que le proporciona los atributos previous and next, y que implemente un método privado _key() 
#     que indica la clave de búsqueda
    
#     Esta lista no admite claves duplicadas
    
# """

        
# base class for an object so that listaEnlazada can handle it.

class LE_Object:
    """ Class from which objects managed by ListaEnlazada must inherit"""
    def __init__(self):
        self.previous = None
        self.next     = None
    def _key(self):
        """must be implemented by ListaEnlazada by object to be handled by ListaEnlazada  """
        raise Exception("NotImplementedError")

class ListaEnlazada:
    
    def __init__(self):
        self.head=None
        self.count = 0
        self.keys = []
    
    def isEmpty(self):
        return self.head == None
    
    def show(self):
        print (f"\n\n List of {self.count} elements: ")
        node = self.head
        pos = 1
        while node is not None:
            print (pos, node._key(), node)
            node = node.next
            pos += 1
    
    def clear(self):
        self.head = None
        self.count = 0
        self.keys = [] 
    
    def first(self):
        """ Returns the first element in list, None if empty """
        if self.head:
            return self.head
        else:
            return None
        
    def last(self):
        """ Returns the last element in list, None if empty """
        if self.isEmpty():
            return None
        object = self.head
        while object.next:
            object = object.next
        return object
    
    def addFirst( self, object):    
        """ 
            inserts given object at the head of the list.
            Raises Duplicate key if object with the same key exists in list
        """    
        if object._key() in self.keys:
            raise Exception("Duplicate key, object not valid")
        
        object.next = self.head
        object.previous = None

        if self.head:
            self.head.previous = object
        
        self.head = object
        self.count += 1
        self.keys.append(object._key())
        return 
    
    def addLast( self, object):
        if self.isEmpty():
            return self.addFirst(object)
        else:
            lastNode = self.last()
            return self.insertAfter(lastNode, object)

    def searchByKey(self, aKey):
        
        if self.isEmpty():
            raise Exception("Empty List !!")    
    
        object = self.head
        while True:
            if object._key() == aKey:
                return object
            if object.next:
                object = object.next
            else:
                break
        raise Exception("Key not found")        

    def deleteByKey(self, aKey):
        node = self.searchByKey(aKey)
        
        # deleting first
        if node.previous is None:
            self.head = node.next 
        # and in all cassses
        else:
            node.previous.next = node.next
            
        self.count -= 1
        self.keys.remove(node._key())

        return None
    
    def deleteObject(self, anObject):
        return self.deleteByKey(anObject._key())
    
    def contains(self, anObject):
        try:
            self.searchByKey(anObject._key())
            return True
        except:
            return False
    
    def containsKey(self, aKey):
        try:
            self.searchByKey(aKey)
            return True
        except:
            return False
    
    def insertAfter(self, existingObject, newObject):
                
        if newObject._key() in self.keys:
            raise Exception ("Duplicate key, object not inserted")
        if not self.contains(existingObject):
            raise Exception ("ExistingObject is not in list")
        
        newObject.previous  = existingObject
        newObject.next      = existingObject.next
        existingObject.next = newObject
        
        self.count += 1
        self.keys.append(newObject._key())
        return None
    
    def insertBefore(self, existingObject, newObject):
        
        if newObject._key() in self.keys:
            raise Exception ("Duplicate key, object not inserted")
        if not self.contains(existingObject):
            raise Exception ("ExistingObject is not in list")
        
        newObject.next          = existingObject
        newObject.previous      = existingObject.previous
        existingObject.previous = newObject
        
        self.count +=1 
        self.keys.append(newObject._key())
        return None

    def insertAfterKey(self, aKey,anObject):
        baseObject = self.searchByKey(aKey)
        return self.insertAfter(baseObject, anObject)
    
    def insertBeforeKey(self, aKey,anObject):
        baseObject = self.searchNodeByKey(aKey)
        return self.insertBefore(baseObject, anObject)
          
    def replaceObject(self, existingObject, newObject):

        if not self.contains(existingObject):
            raise Exception ("ExistingObject is not in list")
        
        if newObject._key() in self.keys:
            raise Exception ("Duplicate Key, duplicate object cannot be placed in list")
        
        newObject.next     = existingObject.next
        newObject.previous = existingObject.previous
        
        self.keys.remove(existingObject._key())
        self.keys.append(newObject._key())
        return None
        
    def list_backwards(self,startObjectKey = None):
        
        if self.isEmpty(): return
        
        if startObjectKey is None:
            node = self.last()
        else:
            node = self.searchByKey(startObjectKey)
    
        while True:
            print (node._key(), node)
            if node.previous is None:  ## llegué al ppio...
                break                  ## salir
            else:
                node = node.previous   ## avanzar
            
        return
        

    def swapObjects(self,object1, object2):
        
        # Verify both objects do exist
        if (not self.contains(object1)) or  (not self.contains(object2)):
            raise Exception("objects not in list")
        
        # swap backward pointers
        object1.previous, object2.previous = object2.previous, object1.previous
        
        # swap fw pointers
        object1.next, object2.next = object2.next, object1.next 
        
        # fix head if applicable
        if self.head == object1 : 
            self.head = object2
        if self.head == object2 : 
            self.head = object1
        
        return None
    
        

# ################################################################################################
# Definimos la clase equipo como hija de LE_Object para que pueda ser gestionado directamente por la
# lista enlazada. Este debe implementar el método _key, para ser buscable por un clave dada
class Equipo(LE_Object):
    def __init__(self, nombre=None, estadio=None, capacidad_estadio=None, num_ligas=0, num_copas_europa=0):
        super().__init__()
        self.nombre=nombre
        self.estadio=estadio
        self.capacidad_estadio=capacidad_estadio
        self.num_ligas=num_ligas
        self.num_copas_europa=num_copas_europa
    def __str__(self):
        str= (f' Equipo Nombre: {self.nombre}')        
        str+=(f' Estadio es: {self.estadio}')
        str+=(f' Capacidad: {self.capacidad_estadio}')
        str+=(f' Ligas: {self.num_ligas}')
        str+=(f' C.Europa es: {self.num_copas_europa}')
        return str
    
    def __repr__(self):
        return f"Object Equipo Nombre: {self.nombre}"
    
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre=nombre
    def getEstadio(self):
        return self.estadio
    def setEstadio(self, estadio):
        self.estadio=estadio
    def getCapacidadEstadio(self):
        return self.capacidad_estadio
    def setCapacidadEstadio(self, capacidad_estadio):
        self.capacidad_estadio=capacidad_estadio
    def getNumLigas(self):
        return self.num_ligas
    def setNumLigas(self, num_ligas):
        self.num_ligas=num_ligas
    def getNumCopasEuropa(self):
        return self.num_copas_europa
    def setNumCopasEuropa(self, num_copas_europa):
        self.num_copas_europa=num_copas_europa

    
    def _key(self):
        return self.getNombre()
    
# ############################################################
# execute tests
# ############################################################


liga = ListaEnlazada()    
RealMadrid = Equipo('Real Madrid', estadio='Bernaeu')
Barcelona  = Equipo('Barcelona', estadio='Campo Nou')
Betis      = Equipo('Betis', estadio='Benito Villamarin')
Atletic    = Equipo('Atletic', estadio='Calderon')

liga.show()
liga.addFirst(RealMadrid)
liga.show()
liga.addFirst(Barcelona)
liga.show()
print("First element is ",liga.first())
print("Last element is ",liga.last())
liga.addLast(Betis)
liga.show()
# print ("Search by key Barcelona produces", liga.searchByKey('Barcelona'))

# print ("\n\ninserting Atletics after Real Madrid")
# liga.insertAfterKey('Real Madrid',Atletic)
# liga.show()

# print ("\n\ndeleting  Barcelona")
# liga.deleteByKey('Barcelona')
# liga.show()


# print ("\n\nReplacing Betis with  Barcelona")
# liga.replaceObject(Betis,Barcelona)
# liga.show()

# print ("\n\nLets clear the list")
# liga.clear()
# liga.show()

# print ("\n\nLets insert Barcelona twice")
# liga.addFirst(Barcelona)
# liga.show()
# try:
#     liga.addFirst(Barcelona)
# except:
#     print(f"Error inserting twice")

# print ("\n\n**Busqueda por clave")
# for key in ['Barcelona','Barsa'] : 
#     try:
#         print (f"Buscando por clave {key}...")
#         equipo = liga.searchByKey(key)
#         print (f"\tEquipo con clave {key} encontrado")
#     except: 
#         print (f"\tEquipo con clave {key} No encontrado, excepción capturada")

# liga.addFirst(RealMadrid)
# liga.addLast(Betis)

# print ("\n\n** FW listing")
# liga.show()

# print ("\n\n** Back Listing")
# liga.list_backwards()

    
# testing swap
# print("\n\n Swapping RM y Barsa")
liga.swapObjects(Barcelona,RealMadrid)
liga.show()
    
    
    
   
