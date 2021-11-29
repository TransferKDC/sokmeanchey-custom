# -*- coding: utf-8 -*-
{
    'name': "account_move_view",
    'summary': """ Add View Currency on List View""",
    'description': """ Display Curency on View and Inovice for SMC""",
    'author': "A2A Digital",
    'category': 'Account',
    'version': '14.0.1.0.0',
    'depends': ['account','base'],
    'data': [
        'views/account_move_views.xml',
        'reports/report_invoice_khmer.xml',
        'reports/report.xml',
    ],
    'demo': [],
    'installable': True,
    'license': 'LGPL-3', 

}
