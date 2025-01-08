{
    'name': 'Agencia Inmobiliaria DCR',  # Nombre amigable de tu módulo
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Gestión de propiedades inmobiliarias',  # Breve descripción
    'description': """
    Módulo de Odoo para gestionar una agencia inmobiliaria.
    Permite gestionar propiedades, clientes, ventas y alquileres.
    """,
    'author': 'Daniel Cuenca Rubio',  # Tu nombre
    'website': 'https://www.aidcr.com',
    'depends': ['base'],  # Dependencia base mínima
    'data': [
        'security/ir.model.access.csv',  # Permisos de acceso
        # Aquí irán los archivos XML de vistas y datos más adelante
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
