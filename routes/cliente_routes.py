from flask import Blueprint, render_template, request, redirect, url_for, flash
from dao.cliente_dao_impl import ClienteDAOImpl
from models.cliente import Cliente

# Crear Blueprint para las rutas de cliente
cliente_bp = Blueprint('cliente', __name__, url_prefix='/clientes')

# Instancia del DAO
cliente_dao = ClienteDAOImpl()

@cliente_bp.route('/')
def listar():
    """Listar todos los clientes"""
    clientes = cliente_dao.listar_todos()
    return render_template('cliente/listar.html', clientes=clientes)

@cliente_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    """Crear un nuevo cliente"""
    if request.method == 'POST':
        # Obtener datos del formulario
        datos = {
            'nombre': request.form.get('nombre'),
            'email': request.form.get('email'),
            'telefono': request.form.get('telefono')
        }
        
        # Verificar si el email ya existe
        if cliente_dao.buscar_por_email(datos['email']):
            flash('El email ya está registrado', 'danger')
            return render_template('cliente/crear.html')
            
        # Crear objeto Cliente y registrar
        cliente = Cliente.from_dict(datos)
        cliente_dao.registrar(cliente)
        
        flash('Cliente registrado exitosamente', 'success')
        return redirect(url_for('cliente.listar'))
        
    return render_template('cliente/crear.html')

@cliente_bp.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    """Editar un cliente existente"""
    cliente = cliente_dao.leer_por_id(id)
    
    if not cliente:
        flash('Cliente no encontrado', 'danger')
        return redirect(url_for('cliente.listar'))
    
    if request.method == 'POST':
        # Obtener datos del formulario
        datos = {
            'nombre': request.form.get('nombre'),
            'email': request.form.get('email'),
            'telefono': request.form.get('telefono')
        }
        
        # Verificar si hay cambio de email y si ya existe
        email_actual = cliente_dao.buscar_por_email(datos['email'])
        if email_actual and str(email_actual.id) != id:
            flash('El email ya está registrado por otro cliente', 'danger')
            return render_template('cliente/editar.html', cliente=cliente)
            
        # Actualizar cliente
        cliente_actualizado = Cliente.from_dict(datos)
        cliente_dao.actualizar(id, cliente_actualizado)
        
        flash('Cliente actualizado exitosamente', 'success')
        return redirect(url_for('cliente.listar'))
        
    return render_template('cliente/editar.html', cliente=cliente)

@cliente_bp.route('/eliminar/<id>')
def eliminar(id):
    """Eliminar un cliente"""
    if cliente_dao.eliminar(id):
        flash('Cliente eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar cliente', 'danger')
    
    return redirect(url_for('cliente.listar'))

@cliente_bp.route('/activos')
def activos():
    """Listar clientes activos"""
    clientes = cliente_dao.clientes_activos()
    return render_template('cliente/listar.html', clientes=clientes, titulo='Clientes Activos')