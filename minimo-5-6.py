from typing import Optional

# --- CLASES BASE TEMPORALES (Para poder probar los Mínimos 5 y 6) ---
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Cliente('{self.nombre}')"

class Zona:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return f"Zona({self.codigo}, '{self.nombre}')"

class Paquete:
    def __init__(self, codigo_seguimiento, cliente, estado="En recepción"):
        self.codigo_seguimiento = codigo_seguimiento
        self.cliente = cliente # Guardamos el objeto Cliente
        self.estado = estado



class Busquedas:

    @staticmethod
    def ordenar_zonas(zonas: list[Zona]) -> list[Zona]:
        return sorted(zonas, key = lambda x: x.codigo)

    @staticmethod
    def busqueda_binaria_zona(codigo_buscado: int, zonas_ordenadas: list[Zona]) -> tuple[Optional[Zona], int]:

        if not zonas_ordenadas:
            return None, 0

        inicio = 0
        fin = len(zonas_ordenadas) - 1
        comparaciones = 0

        while (inicio <= fin):
            medio = (inicio + fin) // 2
            comparaciones += 1

            if zonas_ordenadas[medio].codigo == codigo_buscado:
                return zonas_ordenadas[medio], comparaciones
            elif codigo_buscado < zonas_ordenadas[medio].codigo:
                fin = medio - 1
            else:
                inicio = medio + 1

        return None, comparaciones

    @staticmethod
    def busquedaSecuencial(nombre_cliente: str, paquetes: list[Paquete]) -> tuple[list[Paquete], int]:
        paquetes_encontrados: list[Paquete] = []
        comparaciones = 0

        for p in paquetes:
            comparaciones += 1
            if p.cliente.nombre.strip().lower() == nombre_cliente.strip().lower():
                paquetes_encontrados.append(p)

        return paquetes_encontrados, comparaciones

    

#Pruebas para busquedas binarias
zonas = [
        Zona(105, "Norte"),
        Zona(101, "Centro"),
        Zona(103, "Sur"),
        Zona(110, "Este"),
    ]

zona, comparaciones = Busquedas.busqueda_binaria_zona(110, Busquedas.ordenar_zonas(zonas))

print(f"Búsqueda 110 → {zona} | comparaciones: {comparaciones}")



#Pruebas para busquedas secuenciales
juan = Cliente("Juan Pérez")
maria = Cliente("María López")
pedro = Cliente("Pedro Ruiz")

paquetes = [
    Paquete("PKG-001", juan),
    Paquete("PKG-002", maria),
    Paquete("PKG-003", juan),
    Paquete("PKG-004", pedro),
    Paquete("PKG-005", juan),
]

encontrados, comparaciones = Busquedas.busquedaSecuencial("María López", paquetes)
print(f"Encontrados: {len(encontrados)} | Comparaciones: {comparaciones}")
