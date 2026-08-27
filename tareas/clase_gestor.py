from datetime import datetime
from excepct import Variable_vacia as ex
import json
 


class gestor_tarea:
    fecha_actual = datetime.now().strftime("%d/%m/%Y %I:%M")
    def __init__(self):
        pass
    
    def __traer_id(self):
        with open("tareas/tareas.json","r",encoding="utf-8") as file:
            contenido = json.load(file)
            id=contenido[-1].get("id")+1
            return id,contenido


    def crear_tarea(self):
            id,contenido = self.__traer_id()
            while True:
                try:
                    nombre_tarea = input("Ingresa el nombre de tu tarea: ")
                    if not nombre_tarea.strip():
                        raise ex()
                    break
                except ex as error:
                    print(error)

            nueva_tarea = {
                            "id":id,
                            "nombre":nombre_tarea,
                            "completada":False,
                            "fecha":self.fecha_actual
                        }
            
            contenido.append(nueva_tarea)  
            with open("tareas/tareas.json","w",encoding="utf-8") as file:
                return json.dump(contenido,file,indent=4,ensure_ascii=False) 

    def ver_tareas(self):
        with open("tareas/tareas.json","r",encoding="utf-8") as file:
            contenido = json.load(file)

        for i in contenido:
            print("\n")
            for clave,valor in i.items():
                print(f"{clave}: {valor}")
        return contenido


    def actualizar_tarea(self):
        actulizacion = False
        while True:
            try:
                id = int(input("Dame el id de la tarea que quieres actualizar: "))
                break
            except ValueError as error:
                print(error)
        contenido = self.__traer_id()
        tareas = contenido[1]
        for tarea in tareas:
            if tarea["id"]==id:
                if tarea["completada"]==True:
                    print("La tarea ya estaba actualizada")
                    actulizacion=True
                else:
                    actulizacion = tarea["completada"]=True
        if not actulizacion:
            print("La tarea  no existe")
        with open("tareas/tareas.json","w",encoding="utf-8") as file:
            json.dump(tareas,file,indent=4,ensure_ascii=False)


    def buscar_tarea_nombre(self):
        contenido = self.__traer_id()
        tareas = contenido[1]
        nombre_tarea = input("Dame el nombre de la tarea que quieres buscar: ")
        actulizacion = False
        for tarea in tareas:
            # [(print(f"{clave}: {valor}")) for clave,valor in tarea.items() if tarea["nombre"]==nombre_tarea]
            if tarea["nombre"]==nombre_tarea:
                actulizacion = True
                for clave,valor in tarea.items():
                        print(f"{clave}: {valor}")
        if not actulizacion:
            print("No hay una tarea con ese nombre")


    def ver_tareas_pendientes(self):
        contenido = self.__traer_id()
        tareas = contenido[1]
        for tarea in tareas:
            if tarea["completada"]==False:
                for clave,valor in tarea.items():
                    print(f"{clave}: {valor}")
            print("\n")


    def ver_tareas_completadas(self):
        contenido = self.__traer_id()
        tareas = contenido[1]
        for tarea in tareas:
            if tarea["completada"]==True:
                for clave,valor in tarea.items():
                    print(f"{clave}: {valor}")
            print("\n")


    def eliminar_tarea(self):
        contenido = self.__traer_id()
        tareas = contenido[1]
        nueva_lista = []
        while True:
            try:
                id = int(input("Dame el id de la tarea que quieres actualizar: "))
                break
            except ValueError as error:
                print(error)
        [nueva_lista.append(tarea) for tarea in tareas if tarea["id"]!=id]
        with open("tareas/tareas.json","w",encoding="utf-8") as file:
               json.dump(nueva_lista,file,indent=4,ensure_ascii=False)