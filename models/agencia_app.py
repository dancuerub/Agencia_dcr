from odoo import models, fields
class Agencia_Model(models.Model):
    _name = "agencia.model"
    _description = "App que permite gestionar la compra/venta de viviendas"

    # Campos básicos
    name = fields.Char('Nombre', required=True)
    descripcion = fields.Text('Descripción', help='Introduce una descripción de la propiedad')
    cpostal = fields.Char('Código Postal', required=True)
    fecha_disponible = fields.Date('Fecha disponible')
    precio_inicial = fields.Float('Precio inicial', required=True)
    precio_venta = fields.Float('Precio venta', required=True)
    habitaciones = fields.Integer('Nº habitaciones', required=True)
    m_utiles = fields.Integer('Metros útiles', required=True)
    fachadas = fields.Integer('Nº fachadas', required=True)
    garage = fields.Boolean('Garage')
    jardin = fields.Boolean('Jardín')
    m_jardin = fields.Integer('Metros jardín')
    orientacion = fields.Selection(
        string='Orientación',
        selection=[('norte', 'Norte'), ('sur', 'Sur'), ('este', 'Este'), ('oeste', 'Oeste')],
    )
