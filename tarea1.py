# Ana Jimena Gallegos Rongel
# A01252605
# Tarea 1, Modulo 3

#STACK

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
    
    def peek(self):
        if self.isEmpty():
            return "stack esta vacio"
        return self.stack[-1]

    def pop(self):
        if self.isEmpty():
            return "stack esta vacio"
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        return str(self.stack)

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def peek(self):
        if self.isEmpty():
            return "queue esta vacio"
        return self.queue[0]

    def dequeue(self):
        if self.isEmpty():
            return "queue esta vacio"
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def __str__(self):
        return str(self.queue)
    
class HashTable:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def hash_func(self, key):
        sum_of_chars = 0
        for char in key:
            sum_of_chars += ord(char)
        return sum_of_chars % self.capacity

    def add(self, element):
        index = self.hash_func(element)
        self.table[index].append(element)

    def contains(self, element):
        index = self.hash_func(element)
        if element in self.table[index]:
            return "Si"
        else: 
            return "No"
    
    def remove(self, element):
        index = self.hash_func(element)
        if element in self.table[index]:
            self.table[index].remove(element)
            print("Elemento eliminado correctamente")
        else:
            print("No se encontro el elemento")
    
    def __str__(self):
        return str(self.table)


# Test cases realizados STACK
# Inicializar Stack
print("STACK: ")
myStack = Stack() 

#Agregar 3 elementos a stack e imprimir el stack actual
myStack.push('A')
myStack.push('B')
myStack.push('C')
print(myStack)

#Imprimir el ultimo elemento del stack con Peek
print("Ultimo elemento del stack", myStack.peek())

#Eliminar el ultimo elemento agregado al stack e imprimir el stack nuevo
myStack.pop()
print("Mi stack despues del pop: ",myStack)

#Mostrar el tamaño actual del stack
print("El tamaño de mi stack: ",myStack.size())

# Test cases realizados QUEUE
# Inicializar Queue
print("\n QUEUE:")
myQueue = Queue() 

#Agregar 3 elementos a stack e imprimir el stack actual
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print(myQueue)

#Imprimir el primer elemento del Queue con Peek
print("Primer elemento de mi Queue:", myQueue.peek())

#Eliminar el primer elemento agregado al queue e imprimir el queue nuevo
myQueue.dequeue()
print("Mi queue despues del dequeue: ",myQueue)

#Mostrar el tamaño actual del queue
print("El tamaño de mi queue: ",myQueue.size())

# Test cases realizados HASH TABLE
# Inicializar Hash Table
print("HASH TABLE: ")
myHashTable = HashTable()

# Agregar 3 elementos a la Hash table e imprimir hash
myHashTable.add("Jimena")
myHashTable.add("Regina")
myHashTable.add("America")
print(myHashTable) # Las hash table guardan los elementos en posiciones hash 

#Eliminar un elemento que no existe
myHashTable.remove("Maria")

#Agregar un elemento, Eliminar un elemento que si existe e imprimir la hash table
myHashTable.add("Victor")
myHashTable.remove("Regina")
print(myHashTable)

#Revisar si la hash table contiene un elemento
print("La hash table contiene Victor? : ", myHashTable.contains("Victor"))
print("\n")