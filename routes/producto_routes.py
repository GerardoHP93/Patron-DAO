from flask import Blueprint, render_template, request, redirect, url_for, flash
from dao.producto_dao_impl import ProductoDAOImpl
from models.producto import Producto

# Crear Blueprint para las rutas de producto
producto_bp = Blueprint('producto', __name__, url_prefix='/productos')

# Instancia del DAO
producto_dao = ProductoDAOImpl()

@producto_bp.route('/')
def listar():
    """Listar todos los productos"""
    productos = producto_dao.listar_todos()
    return render_template('producto/listar.html', productos=productos)

@producto_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    """Crear un nuevo producto"""
    if request.method == 'POST':
        # Obtener datos del formulario
        try:
            datos = {
                'nombre': request.form.get('nombre'),
                'descripcion': request.form.get('descripcion'),
                'precio': float(request.form.get('precio', 0)),
                'stock': int(request.form.get('stock', 0))
            }
        except (ValueError, TypeError):
            flash('Error en los datos del formulario', 'danger')
            return render_template('producto/crear.html')
            
        # Crear objeto Producto y registrar
        producto = Producto.from_dict(datos)
        producto_dao.registrar(producto)
        
        flash('Producto registrado exitosamente', 'success')
        return redirect(url_for('producto.listar'))
        
    return render_template('producto/crear.html')

@producto_bp.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    """Editar un producto existente"""
    producto = producto_dao.leer_por_id(id)
    
    if not producto:
        flash('Producto no encontrado', 'danger')
        return redirect(url_for('producto.listar'))
    
    if request.method == 'POST':
        # Obtener datos del formulario
        try:
            datos = {
                'nombre': request.form.get('nombre'),
                'descripcion': request.form.get('descripcion'),
                'precio': float(request.form.get('precio', 0)),
                'stock': int(request.form.get('stock', 0))
            }
        except (ValueError, TypeError):
            flash('Error en los datos del formulario', 'danger')
            return render_template('producto/editar.html', producto=producto)
            
        # Actualizar producto
        producto_actualizado = Producto.from_dict(datos)
        producto_dao.actualizar(id, producto_actualizado)
        
        flash('Producto actualizado exitosamente', 'success')
        return redirect(url_for('producto.listar'))
        
    return render_template('producto/editar.html', producto=producto)

@producto_bp.route('/eliminar/<id>')
def eliminar(id):
    """Eliminar un producto"""
    if producto_dao.eliminar(id):
        flash('Producto eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar producto', 'danger')
    
    return redirect(url_for('producto.listar'))

@producto_bp.route('/buscar', methods=['GET'])
def buscar():
    """Buscar productos por nombre"""
    nombre = request.args.get('nombre', '')
    productos = producto_dao.buscar_por_nombre(nombre)
    return render_template('producto/listar.html', productos=productos, busqueda=nombre)

@producto_bp.route('/disponibles')
def disponibles():
    """Listar productos disponibles"""
    productos = producto_dao.productos_disponibles()
    return render_template('producto/listar.html', productos=productos, titulo='Productos Disponibles')

@producto_bp.route('/actualizar_stock/<id>', methods=['POST'])
def actualizar_stock(id):
    """Actualizar el stock de un producto"""
    try:
        cantidad = int(request.form.get('cantidad', 0))
        if producto_dao.actualizar_stock(id, cantidad):
            flash('Stock actualizado exitosamente', 'success')
        else:
            flash('Error al actualizar stock', 'danger')
    except (ValueError, TypeError):
        flash('Cantidad inválida', 'danger')
    
    return redirect(url_for('producto.listar'))