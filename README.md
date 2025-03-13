# Proyecto de Implementación del Patrón Data Access Object (DAO) en Flask

- **Nombre:** Gerardo Isidro Herrera Pacheco
- **Matrícula:** ISC 68612
- **Semestre:** 8vo
- **Materia**: Temas selectos de Programación
- **Maestro:** Jose C Aguilar Canepa
- **Institución:** Universidad Autónoma de Campeche, Facultad de Ingeniería

# Sistema de Gestión con Patrón DAO en Flask y MongoDB

Este proyecto es una implementación del patrón de diseño Data Access Object (DAO) utilizando Flask y MongoDB. El sistema permite la gestión de clientes y productos a través de una interfaz web, demostrando la aplicación práctica de este patrón en una aplicación real.

## Tecnologías Utilizadas
- **Hosting**: Se desplegó el programa usando el hosting Render, puede acceder entrando a este link: https://patron-dao.onrender.com
- **MongoDB Atlas**: Servicio en la nube que proporciona hosting para bases de datos MongoDB.
- **Framework Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Bibliotecas Frontend**:
  - Bootstrap 5.3 (Estilos y componentes UI)
- **Dependencias Python**:
  - Flask (Framework web)
  - PyMongo (Conector para MongoDB)
  - Bson (Manejo de ObjectId para MongoDB)

## Estructura del Proyecto

```
proyecto_dao_flask/
├── app.py                  # Archivo principal de Flask
├── config.py               # Configuración de la aplicación
├── static/
│   └── css/
│       └── styles.css      # Hoja de estilos personalizada
├── templates/              # Plantillas HTML
│   ├── base.html           # Plantilla base
│   ├── cliente/            # Plantillas para clientes
│   │   ├── listar.html
│   │   ├── editar.html
│   │   └── crear.html
│   └── producto/           # Plantillas para productos
│       ├── listar.html
│       ├── editar.html
│       └── crear.html
├── dao/                    # Implementación del patrón DAO
│   ├── __init__.py
│   ├── base_dao.py         # Clase base abstracta (equivalente a CRUD.java)
│   ├── cliente_dao.py      # Interface DAO para Cliente
│   ├── cliente_dao_impl.py # Implementación concreta de Cliente
│   ├── producto_dao.py     # Interface DAO para Producto
│   └── producto_dao_impl.py # Implementación concreta de Producto
├── models/                 # Modelos de datos
│   ├── __init__.py
│   ├── cliente.py          # Modelo Cliente
│   └── producto.py         # Modelo Producto
└── routes/                 # Rutas y controladores
    ├── __init__.py
    ├── cliente_routes.py   # Rutas para Cliente
    └── producto_routes.py  # Rutas para Producto
```

##  Diagrama de Clases UML

![Diagrama de clases DAO](https://github.com/user-attachments/assets/ef8fe426-4931-43a6-b3b3-b346031f4030)


### Relaciones principales

#### **Herencia de interfaces**
- `ClienteDAO` y `ProductoDAO` **extienden** `BaseDAO<T>`, una interfaz genérica que define las operaciones **CRUD** básicas.
- Esto refleja el principio de **herencia** del patrón DAO, donde las interfaces específicas heredan de una interfaz base común.

#### **Implementación de interfaces**
- `ClienteDAOImpl` **implementa** `ClienteDAO`.
- `ProductoDAOImpl` **implementa** `ProductoDAO`.
- Estas clases proporcionan la **implementación concreta para MongoDB** de las operaciones definidas en las interfaces.

#### **Relación de uso**
- `ClienteDAOImpl` usa la clase `Cliente` para realizar operaciones de la capa de datos.
- `ProductoDAOImpl` usa la clase `Producto` de manera similar.
- Los controladores (`cliente_routes` y `producto_routes`) **usan** las implementaciones de DAO para acceder a los datos.

### Componentes principales

#### **Interfaces**
- `BaseDAO<T>` → Interfaz genérica que define operaciones **CRUD** básicas.
- `ClienteDAO` → Interfaz específica para operaciones de **Cliente**.
- `ProductoDAO` → Interfaz específica para operaciones de **Producto**.

#### **Implementaciones concretas**
- `ClienteDAOImpl` → Implementación de `ClienteDAO` para **MongoDB**.
- `ProductoDAOImpl` → Implementación de `ProductoDAO` para **MongoDB**.

#### **Modelos de datos**
- `Cliente` → Modelo que representa los datos de un **cliente**.
- `Producto` → Modelo que representa los datos de un **producto**.

#### **Controladores**
- `cliente_routes` → Maneja las rutas y peticiones **HTTP** relacionadas con **clientes**.
- `producto_routes` → Maneja las rutas y peticiones **HTTP** relacionadas con **productos**.

## Implementación del Patrón DAO

### Fundamentos Teóricos Aplicados

El patrón DAO (Data Access Object) es un patrón de diseño estructural que permite separar la lógica de acceso a datos de la lógica de negocio. En esta implementación:

1. **Abstracción de la Fuente de Datos**: El código de la aplicación no interactúa directamente con MongoDB, sino a través de las interfaces DAO.

2. **Uso de Interfaces**: Se definen interfaces abstractas (`ClienteDAO`, `ProductoDAO`) que establecen un contrato para las operaciones de datos.

3. **Implementaciones Concretas**: Clases como `ClienteDAOImpl` y `ProductoDAOImpl` que implementan las interfaces y contienen la lógica real de acceso a MongoDB.

4. **Operaciones CRUD Genéricas**: Se define una clase base abstracta (`BaseDAO`) que establece operaciones comunes (Create, Read, Update, Delete), esto para abstraer a un más el acceso, ya que se evita la repetición de estos métodos comunes de CRUD para cada DAO que se vaya implementando.

5. **Métodos Específicos por Entidad**: Por lo anterior, ahora en cada DAO específico solo se añaden métodos propios de su dominio (ej. `buscar_por_email` para clientes).

### Componentes Clave

#### 1. Clase Base Abstracta (`base_dao.py`)

Esta clase define las operaciones CRUD básicas que todas las implementaciones DAO deben proporcionar:

- `listar_todos()`: Obtener todos los registros
- `leer_por_id(id)`: Leer un registro por su ID
- `registrar(entidad)`: Crear un nuevo registro
- `actualizar(id, entidad)`: Actualizar un registro existente
- `eliminar(id)`: Eliminar un registro

#### 2. Interfaces Específicas

Cada entidad tiene su propia interfaz que extiende de `BaseDAO` y añade métodos específicos:

- `ClienteDAO`: Añade `buscar_por_email()` y `clientes_activos()`
- `ProductoDAO`: Añade `buscar_por_nombre()`, `productos_disponibles()` y `actualizar_stock()`

#### 3. Implementaciones Concretas

Las clases que implementan las interfaces y contienen la lógica real de acceso a MongoDB:

- `ClienteDAOImpl`: Implementa `ClienteDAO` para la colección "clientes" en MongoDB
- `ProductoDAOImpl`: Implementa `ProductoDAO` para la colección "productos" en MongoDB

#### 4. Modelos

Clases que representan entidades del dominio con métodos para convertir entre objetos Python y documentos MongoDB:

- `Cliente`: Representa un cliente con atributos como nombre, email, teléfono
- `Producto`: Representa un producto con atributos como nombre, descripción, precio, stock

#### 5. Rutas y Controladores

Manejan las solicitudes HTTP, utilizan los DAO para acceder a los datos y renderizan las plantillas:

- `cliente_routes.py`: Contiene las rutas para operaciones CRUD de clientes
- `producto_routes.py`: Contiene las rutas para operaciones CRUD de productos

