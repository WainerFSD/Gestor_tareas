from tareas.clase_gestor import gestor_tarea



""" lista = [
    {
        "id": 1,
        "nombre": "Estudiar Python",
        "completada": False,
        "fecha": "20/08/2026 10:30"
    },
    {
        "id": 2,
        "nombre": "",
        "completada": False,
        "fecha": "21/08/2026 08:20"
    },
    {
        "id": 3,
        "nombre": "hola",
        "completada": False,
        "fecha": "22/08/2026 04:13"
    }]
tare = []
for tarea in lista:
        tarea_encontrada = [(print(v), tare.append(v)) for t,v in tarea.items() if tarea["id"]==3 ]
        print(tare) """

gestor = gestor_tarea()

# tarea1 = gestor.crear_tarea()
#leer = gestor.ver_tareas() 
#actualizar_tarea = gestor.actualizar_tarea()
#buscar_tarea_nombre = gestor.buscar_tarea_nombre()
#tareas_pendientes = gestor.ver_tareas_pendientes()
#tareas_completadas = gestor.ver_tareas_completadas()
eliminar_tarea = gestor.eliminar_tarea()