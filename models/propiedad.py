from odoo import models, fields

class Propiedad(models.Model):
    _name = 'agencia.propiedad'  # Nombre técnico del modelo
    _description = 'Modelo de Propiedades Inmobiliarias'

    name = fields.Char(string='Nombre de la Propiedad', required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio')
    direccion = fields.Char(string='Dirección')
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('vendido', 'Vendido'),
        ('alquilado', 'Alquilado'),
    ], string='Estado', default='disponible')
