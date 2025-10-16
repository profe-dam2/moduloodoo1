# -*- coding: utf-8 -*-

from odoo import models, fields, api


class departamento(models.Model):
    _name = 'modulo_demo.departamento'
    _description = 'Define los atributos de un departamento'

    # Atributos
    nombreDpto = fields.Char(string='Nombre departamento' ,required=True)

class empleado(models.Model):
    _name = 'modulo_demo.empleado'
    _description = 'Define los atributos de un empleado'

    # Atributos
    dniEmpleado = fields.Char(string='DNI' ,required=True)
    nombreEmpleado = fields.Char(string='Nombre' ,required=True)
    fechaNacimiento = fields.Datetime(string='Fecha de nacimiento' ,required=True, default=fields.date.today())
    direccionEmpleado = fields.Char(string='Dirección')

class proyecto(models.Model):
    _name = 'modulo_demo.proyecto'
    _description = 'Define los atributos de un proyecto'

    #Atributos
    nombreProyecto = fields.Char(string='Nombre proyecto' ,required=True)
    tipoProyecto = fields.Char(string='Tipo proyecto', selection=[('f','Front-End'),('b','Back-End')], help='Tipo de proyecto' ,required=True)
    descriptionProyect = fields.Text(string='Descripción del proyecto')