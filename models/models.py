# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Departamento(models.Model):
    _name = 'modulo_demo.departamento'
    _description = 'Define los atributos de un departamento'

    # Atributos
    nombreDpto = fields.Char(string='Nombre departamento', required=True)

    # Relación entre tablas
    empleado_ids = fields.One2many('modulo_demo.empleado', 'departamento_id', string='Empleados')


class Empleado(models.Model):
    _name = 'modulo_demo.empleado'
    _description = 'Define los atributos de un empleado'

    # Atributos
    dniEmpleado = fields.Char(string='DNI', required=True)
    nombreEmpleado = fields.Char(string='Nombre', required=True)
    fechaNacimiento = fields.Date(string='Fecha de nacimiento', required=True, default=fields.Date.today)
    direccionEmpleado = fields.Char(string='Dirección')

    # Relaciones
    departamento_id = fields.Many2one('modulo_demo.departamento', string='Departamento')
    proyecto_ids = fields.Many2many('modulo_demo.proyecto', string='Proyectos')


class Proyecto(models.Model):
    _name = 'modulo_demo.proyecto'
    _description = 'Define los atributos de un proyecto'

    # Atributos
    nombreProyecto = fields.Char(string='Nombre proyecto', required=True)
    tipoProyecto = fields.Selection([
        ('f', 'Front-End'),
        ('b', 'Back-End')
    ], string='Tipo de proyecto', required=True, help='Tipo de proyecto')
    descripcionProyecto = fields.Text(string='Descripción del proyecto')

    # Relaciones
    empleado_ids = fields.Many2many('modulo_demo.empleado', string='Empleados')
