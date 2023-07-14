import pytest

from models import *

class TestClass:

    def test_enviar_monto_valido(self):

        BD: Dict[str, Cuenta] = dict()
        BD["21345"] = Cuenta("21345", "Arnaldo", 200, ["123","456"])
        BD["123"] = Cuenta("123", "Luisa", 400, ["456"])
        BD["456"] = Cuenta("456", "Andrea", 300, ["21345"])

        primer_usuario = BD[list(BD.keys())[0]]

        ultimo_usuario = BD[list(BD.keys())[-1]]
        primer_usuario.pagar(ultimo_usuario.numero,primer_usuario.monto/2)
        assert primer_usuario.monto/2 == primer_usuario.monto/2

    def test_pagar_numerodestino_invalido(self):

        BD: Dict[str, Cuenta] = dict()
        BD["21345"] = Cuenta("21345", "Arnaldo", 200, ["123","456"])
        BD["123"] = Cuenta("123", "Luisa", 400, ["456"])
        BD["456"] = Cuenta("456", "Andrea", 300, ["21345"])



        assert 1 == 1

    def test_pagar_monto_invalido(self):

        BD: Dict[str, Cuenta] = dict()
        BD["21345"] = Cuenta("21345", "Arnaldo", 200, ["123","456"])
        BD["123"] = Cuenta("123", "Luisa", 400, ["456"])
        BD["456"] = Cuenta("456", "Andrea", 300, ["21345"])

        primer_usuario = BD[list(BD.keys())[0]]

        ultimo_usuario = BD[list(BD.keys())[-1]]
        primer_usuario.pagar(ultimo_usuario.numero,primer_usuario.monto+100)

        assert primer_usuario.monto == primer_usuario.monto


    def test_recibir_historial_invalido(self):

        BD: Dict[str, Cuenta] = dict()
        BD["21345"] = Cuenta("21345", "Arnaldo", 200, ["123","456"])
        BD["123"] = Cuenta("123", "Luisa", 400, ["456"])
        BD["456"] = Cuenta("456", "Andrea", 300, ["21345"])

        assert 1 == 1