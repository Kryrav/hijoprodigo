# #hijo prodigo
# nombre = input("Ingrese su nombre: ") #guardar lo que se escribe
# #variables
# dinero = 100
# dignidad = 50
# hambre = 0

# print(f"{nombre} ha recibido su herencia") #100
# print ("Que desea hacer con su herencia?")
# print ("1. Gastarlo todo en fiestas")
# print ("2. Invertir")
# print ("3. Ahorrar")

# opcion = int(input("Elige una opcion: "))
# if opcion == 1:
#     dinero = 0
#     dignidad -=20
#     hambre += 50
# elif opcion == 2:
#     dinero +=20
# elif opcion == 3:
#     print("Muy bien usted esta ahorrando") 
# else:
#     print("Esta opcion es invalida")      
    
# # gastar(dinero, dignidad)
# # trabajar(dinero, hambre)
# def gastar(dinero, dignidad):
#     dinero -= 30
#     dignidad -=10
#     return dinero, hambre

# def trabajar(dinero, hambre):
#     dinero += 15
#     hambre += 5
#     return dinero, hambre
    
# #bucle
# while dinero > 0:
#     print("“Sigues viviendo lejos de casa…”")
#     dinero -= 10
# -------------OBJETOS
# HijoProdigo
# Debe incluir:
# Atributos:
# nombre
# dinero
# dignidad
# hambre
# arrepentimiento
class HijoProdigo : 
    def __init__(self, nombre):
        self.nombre =  nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento =0 
        self.accion ="Salir a vivir la vida loca" 
# gastar_todo()
# invertir()
# ahorrar()
# trabajar()
# reflexionar()
    def gastar_todo(self):
        self.dinero = 0
        self.dignidad -=20
        self.hambre += 50
        
    def invertir(self):
        self.dinero += 20
        print(f"has invertido sabiamente tu dinero : {self.dinero}")      
        
    def ahorrar(self):
        self.dinero += 20
        
    def trabajar(self):
        self.dinero += 15
        self.hambre += 5
        self.dignidad += 5
    
    def reflexionar(self):
        if self.hambre > 40:
            self.arrepentimiento += 10
    #---------------------------------------------------------------
        #Mejoras FUNCIONALES KRYRAV - Rene Alejandro Vasquez Vare
    #---------------------------------------------------------------
    

    def mostrar_estado(self):
        print(f"\n-------- Estado actual de {self.nombre} despues de '{self.accion}' ---------")
        print(f"Dinero: {self.dinero}")
        print(f"Dignidad: {self.dignidad}")
        print(f"Hambre: {self.hambre}")
        print(f"Arrepentimiento: {self.arrepentimiento}")

    def vivir(self):
        self.dinero -= 10
        self.hambre += 5
        self.reflexionar()
    
    def esta_arruinado(self):
        return self.dinero <= 0
    
    def normalizar(self):   #Limitamos los límites del sistema
        if self.dignidad < 0:
            self.dignidad = 0
        if self.hambre < 0:
            self.hambre = 0
        if self.arrepentimiento < 0:
            self.arrepentimiento = 0
    def mostrar_menu(self):
        print("\nQue desea hacer con su herencia?")
        print("1. Gastarlo todo en fiestas")
        print("2. Invertir")
        print("3. Ahorrar")
        print("4. Trabajar")
        print("5. Volver a casa :)")

    def volver_a_casa(self):
        print(f"{self.nombre} ha decidido volver a casa y reflexionar sobre sus acciones :)")

    def jugar(self):
        while not self.esta_arruinado():
            self.mostrar_estado()
            self.mostrar_menu()
            opcion = int(input("Elige una opcion: "))
            print("“Sigues viviendo lejos de casa…”") 
            if opcion == 1:
                self.gastar_todo()
                self.accion = "Gastar todo en fiestas" 
                break # Esto decide salir del juego si el jugador decide gastar todo en fiestas
            elif opcion == 2:
                self.invertir()
                self.accion = "Invertir sabiamente"
            elif opcion == 3:
                self.ahorrar()
                self.accion = "Ahorrar dinero"
            elif opcion == 4:
                self.trabajar()
                self.accion = "Trabajar para ganar dinero"
            elif opcion == 5:
                self.volver_a_casa()
                break # Esto decide salir del juego si el jugador decide volver a casa
            else:
                print("Esta opcion es invalida")
            print("----------------------------------------------------------------")
            self.vivir()  # Aplica el costo de vivir (dinero y hambre) y reflexiona sobre el estado actual
            self.normalizar()  # Aseguramos que los atributos no caigan por debajo de 0
            
        #Mostramos el mensaje final dependiendo de cómo terminó el juego
        if self.esta_arruinado():
            print("El dinero se acabó")
        else:
            print("Has terminado el juego voluntariamente")
                
        print("Su nivel de arrepentimiento esta en :" , self.arrepentimiento)      
        self.mostrar_estado()  
    #---------------------------------------------------------------

jugador =  HijoProdigo(input("Ingrese su nombre: "))      #guardar lo que se escribe

#---------------------------------------------------------------
    #Mejoras Estructura
#---------------------------------------------------------------
print(f"{jugador.nombre} ha recibido su herencia") #100            
print(f"Dispone de este monto: {jugador.dinero}")
print(f"Incia con una dignidad de : {jugador.dignidad}")
print(f"Incia con un hambre de : {jugador.hambre}")
print(f"{jugador.hambre} -> QUE COMIENCE EL JUEGO! ")
jugador.jugar()  # Iniciamos el juego llamando al método jugar del objeto jugador                
            
#---------------------------------------------------------------        
 