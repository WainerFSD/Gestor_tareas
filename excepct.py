class Variable_vacia(Exception):
    def __init__(self,mensaje="Lo siento no puedes crear una tarea sin nombre"):
        super().__init__(mensaje)