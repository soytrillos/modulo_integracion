# -*- coding: utf-8 -*-
{
    'name': "integradora_bex",

    'summary': """
        Modulo de parametrizacion para integrar ERP con WMS BEX""",

    'description': """
        Modulo de Integracion ERP - WMS
    """,

    'author': "SimonT",
    'website': "https://www.bexsoluciones.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/integradora_bex_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
