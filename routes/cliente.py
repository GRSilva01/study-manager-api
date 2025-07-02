from flask import Blueprint, render_template

cliente_route = Blueprint("cliente", __name__)

@cliente_route.route("/")
def lista_cliente():
    return render_template('lista_clientes.html')


@cliente_route.route("/", methods=['POST'])
def inserir_cliente():
    pass

@cliente_route.route("/new")
def form_cliente():
    return render_template('form_clientes.html')

@cliente_route.route("/<int:cliente_id>")
def detalhe_cliente():
    pass

@cliente_route.route("/<int:cliente_id>/edit")
def form_edit_cliente():
    pass

@cliente_route.route("/<int:cliente_id>/update", methods=['PUT'])
def update_cliente():
    pass

@cliente_route.route("/<int:cliente_id>/dalete")
def dalete_cliente():
    pass
