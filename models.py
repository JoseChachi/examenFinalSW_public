from typing import List, Dict, Tuple
import datetime

class Operacion:

    def __init__(self, numeroOrigen, numeroDestino, fecha, valor) -> None:
        self.numeroOrigen: int = numeroOrigen
        self.numeroDestino: int = numeroDestino
        self.fecha: str = fecha
        self.valor: int = valor

class Cuenta:

    recibidos: List[Tuple[str, Operacion]] = list()
    enviados: List[Tuple[str, Operacion]] = list()

    def __init__(self, numero, nombre, monto, contactos) -> None:
        self.numero: int = numero
        self.nombre: str = nombre
        self.monto: int = monto
        self.contactos: List[str] = contactos

    def historial(self):
        response = ""
        usuario = BD[self.numero]
        response += f"<p>Saldo de {usuario.nombre}: {usuario.monto}</p>\n"
        response += f"<h2>Operaciones de {usuario.nombre}</h2>\n"

        print(self.recibidos)
        print(self.enviados)
        for recibido in self.recibidos:
            if recibido[1].numeroOrigen != self.numero:
                response += f"<p>Pago recibido de {recibido[1].valor} de {BD[recibido[1].numeroOrigen].nombre}</p>\n"

        for enviado in self.enviados:
            if enviado[1].numeroDestino != self.numero:
                response += f"<p>Pago realizado de {enviado[1].valor} de {BD[enviado[1].numeroDestino].nombre}</p>\n"

        return response

    def pagar(self, destino, valor):
        
        fecha = str(datetime.datetime.now().date())
        usuario_emisor = BD[self.numero]
        usuario_destino = BD[destino]
        
        operacion = Operacion(self.numero, destino, fecha, valor)
        
        usuario_destino.recibidos.append((self.numero, operacion))
        usuario_emisor.enviados.append((destino, operacion))

        BD[self.numero].monto -= valor
        BD[destino].monto += valor

        return fecha


BD: Dict[str, Cuenta] = dict()
BD["21345"] = Cuenta("21345", "Arnaldo", 200, ["123","456"])
BD["123"] = Cuenta("123", "Luisa", 400, ["456"])
BD["456"] = Cuenta("456", "Andrea", 300, ["21345"])
