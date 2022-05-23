# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class integradora_bex(models.Model):
#     _name = 'integradora_bex.integradora_bex'
#     _description = 'integradora_bex.integradora_bex'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api
import os
import platform

class maestra_integradora(models.Model):
    _name = 'integradora_bex.maestra_integradora'
    _description = 'Clase para configurar las integraciones'

    name = fields.Char(string='Nombre compañia', required=True)
    wms_bd_principal = fields.Char(string='Base de datos RPC', required=True)
    wms_endpoint_api = fields.Char(string='Endpoint API', required=True)
    wms_username_rpc = fields.Char(string='Usuario RPC', required=True)
    wms_token_rpc = fields.Char(string='Token RPC', required=True)
    wms_endpoint_rpc = fields.Char(string='Link RPC', required=True)
    wms_tipo_integracion = fields.Selection(string='Tipo de integracion', selection=[('PL', 'Planos'), ('WS', 'Web Services'), ('API', 'API')], default='PL')

    ruta_archivos = fields.Char(string='Repositorio de archivos o ruta', compute='_compute_ruta_archivos')
    importar_plano = fields.Binary(string='Cargar Archivo')
    nombre_archivo = fields.Char(string='Archivo')
    api_endpoint = fields.Char(string='Endpoint')
    api_username = fields.Char(string='Usuario')
    api_token = fields.Char(string='Token')

    ws_endpoint = fields.Char(string='Endpoint')
    ws_proxy_host = fields.Char(string='Proxy Host')
    ws_proxy_port = fields.Char(string='Proxy Port')
    ws_conexion = fields.Char(string='Conexión')
    ws_compania = fields.Char(string='Compañia')
    ws_proveedor = fields.Char(string='Proveedor')
    ws_username = fields.Char(string='Usuario')
    ws_clave = fields.Char(string='Clave')
    ws_consultas_id = fields.Many2many('integradora_bex.consultas_webservices', 'ws_consultas_rel', 'compania_id', 'consulta_id', string='Consultas')

    @api.depends('wms_bd_principal')
    def _compute_ruta_archivos(self):
        for record in self:
            systemOpe = str(platform.platform()).find('Windows')
            if systemOpe == -1:
                path_home = os.environ['HOME']
                path_def = f'{path_home}/integradora_bex_dir/{record.wms_bd_principal}'
                if os.path.exists(path_def):
                    record.ruta_archivos = path_def
                else:
                    os.makedirs(path_def)
                    record.ruta_archivos = path_def
            else:
                path_def = f'C:\\integradora_bex_dir\\{record.wms_bd_principal}'
                if os.path.exists(path_def):
                    record.ruta_archivos = path_def
                else:
                    os.makedirs(path_def)
                    record.ruta_archivos = path_def

    # ws_consultas_id = fields.Many2many(relation='integradora_bex.consultas_webservices', comodel_name='ws_consultas_rel', column1='compania_id', column2='consulta_id', string='Consultas')
    # ws_consulta_id = fields.Many2one("integradora_bex.consultas_webservices", 'compania_id', 'consulta_id', string='Consulta', ondelete='restrict')




class consultas_webservices(models.Model):
    _name = 'integradora_bex.consultas_webservices'
    _description = 'Clase para configurar consultas'

    name = fields.Char(string='Nombre consulta', required=True)
    erp_integracion = fields.Many2one("integradora_bex.maestra_erp", string='ERP Integracion', ondelete='restrict')
    consulta = fields.Text(string='Query')

    # companias_ids = fields.One2many("integradora_bex.maestra_integradora", 'ws_consulta_id', string='Compañia')

class maestra_erp(models.Model):
    _name = 'integradora_bex.maestra_erp'
    _description = 'Clase para crear ERP'

    name = fields.Char(string='Nombre ERP', required=True)
    description = fields.Text(string='Descripcion')


class generacion_transacciones(models.Model):
    _name = 'integradora_bex.generacion_transacciones'
    _description = 'Clase para generar planos de transacciones'

    name = fields.Char('Nombre planos')


