# -*- coding: utf-8 -*-
{
    'name': "bug管理",

    'summary': """
        用于软件开发过程中bug的管理""",

    'description': """
        用于软件开发过程中bug的管理
    """,

    'author': "冼俊泓",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bugs.xml',
        'views/follower.xml',
        'views/bugs_template.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
