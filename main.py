from models import *
from flask import Flask, request, abort



app = Flask(__name__)

@app.route("/billetera/contactos", methods=['GET'])
def billetera_contactos():
    minumero = request.args.get('minumero')

    if minumero is None:
        abort(422, "No number provided")

    if minumero not in BD:
        abort(404, "No number found")

    lista_contactos = BD[minumero].contactos

    response = ""
    for contacto in lista_contactos:
        response += f"<p>{contacto}: {BD[contacto].nombre}\n</p>"

    return response


@app.route("/billetera/pagar", methods=['GET'])
def billetera_pagar():
    minumero = request.args.get('minumero')

    if minumero is None:
        abort(422, "No number provided")

    if minumero not in BD:
        abort(404, "No number found")

    usuario_emisor = BD[minumero]

    numerodestino = request.args.get('numerodestino')

    if numerodestino is None:
        abort(422, "No number target provided")

    if numerodestino not in usuario_emisor.contactos:
        abort(404, "No number target found")

    valor = request.args.get('valor')

    if valor is None:
        abort(422, "No amount provided")

    usuario_receptor = BD[numerodestino]
    valor = int(valor)
    if valor > usuario_emisor.monto:
        abort(400, f"Can not sent more money than you have\nYou have {usuario_emisor.monto} and trying to send {valor}")

    response = usuario_emisor.pagar(numerodestino, valor)

    return f"<p>Realizado en {response}</p>"


@app.route("/billetera/historial", methods=['GET'])
def billetera_historial():
    minumero = request.args.get('minumero')

    if minumero is None:
        abort(422, "No number provided")

    if minumero not in BD:
        abort(404, "No number found")

    response = BD[minumero].historial()

    return response


if __name__ == '__main__':
    app.run(port=5000, debug=True)