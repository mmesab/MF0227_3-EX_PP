# core_modelos.py

class EstadoInvalidoError(Exception):
    """Excepción personalizada para transiciones de estado no permitidas."""
    pass


class TicketTecnico:
    ESTADOS_VALIDOS = ["Abierto", "En Proceso", "Cerrado"]
    TRANSICIONES_PERMITIDAS = {
        "Abierto": ["En Proceso", "Cerrado"],
        "En Proceso": ["Abierto", "Cerrado"],
        "Cerrado": []  # De cerrado no se puede pasar a otro estado directamente
    }

    def __init__(self, ticket_id: int, titulo: str, prioridad: str = "Media"):
        self._id = ticket_id
        self._titulo = titulo
        self._estado = "Abierto"
        self._prioridad = prioridad

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado: str):
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise EstadoInvalidoError(f"El estado '{nuevo_estado}' no es válido.")
        
        if nuevo_estado not in self.TRANSICIONES_PERMITIDAS.get(self._estado, []):
            raise EstadoInvalidoError(
                f"Transición no permitida: de '{self._estado}' a '{nuevo_estado}'."
            )
        
        self._estado = nuevo_estado

    def calcular_sla(self) -> int:
        """Método base para calcular el SLA en horas (a sobrescribir en hijas)."""
        return 48


class TicketHardware(TicketTecnico):
    def __init__(self, ticket_id: int, titulo: str, prioridad: str, componente: str):
        super().__init__(ticket_id, titulo, prioridad)
        self.componente = componente

    def calcular_sla(self) -> int:
        # Polimorfismo: El hardware suele requerir intervención física (SLA más estricto según prioridad)
        if self._prioridad.lower() == "alta":
            return 12
        elif self._prioridad.lower() == "media":
            return 24
        return 48


class TicketSoftware(TicketTecnico):
    def __init__(self, ticket_id: int, titulo: str, prioridad: str, sistema_operativo: str):
        super().__init__(ticket_id, titulo, prioridad)
        self.sistema_operativo = sistema_operativo

    def calcular_sla(self) -> int:
        # Polimorfismo: El software se puede gestionar en remoto
        if self._prioridad.lower() == "alta":
            return 8
        elif self._prioridad.lower() == "media":
            return 16
        return 36


# Pruebas unitarias básicas (Bloque requerido)
if __name__ == "__main__":
    print("--- PRUEBAS UNITARIAS DE POO ---")
    
    # 1. Prueba Ticket Hardware
    t_hw = TicketHardware(1, "Fallo de placa base", "Alta", "Placa Base ASUS")
    print(f"Ticket #{t_hw._id} [{t_hw._titulo}] - Estado inicial: {t_hw.estado} - SLA: {t_hw.calcular_sla()}h")
    
    t_hw.estado = "En Proceso"
    print(f"Nuevo estado válido: {t_hw.estado}")

    # 2. Prueba de excepción por transición inválida
    try:
        t_hw.estado = "Abierto" # De En Proceso a Abierto está permitido, probemos algo inválido luego
    except EstadoInvalidoError as e:
        print(f"Excepción capturada correctamente: {e}")

    try:
        t_hw.estado = "Cerrado"
        t_hw.estado = "En Proceso" # De Cerrado a En Proceso debe fallar
    except EstadoInvalidoError as e:
        print(f"Excepción capturada correctamente (Transición Cerrado -> En Proceso bloqueada): {e}")