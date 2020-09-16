# -*- coding: utf-8 -*-
{
    'name': "School Management",

    'summary': """
        
        """,

    'description': """
       
    """,

    'author': "E.B.Tech",
    'website': "http://www.ebtechco.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Learning',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/security_rules.xml',
        'security/ir.model.access.csv',
        'views/sequence.xml',
        'views/school_structure.xml',
        'views/administrative_directorate.xml',
        'views/school_assignment.xml',
        'views/main_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}