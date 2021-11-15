# -*- coding: utf-8 -*-
{
    'name': "account_move_invoice",
    'summary': """ Add Currency on Invoice""",
    'description': """ Display Curency on View and Inovice for SMC""",
    'author': "A2A Digital",
    'category': 'Account',
    'version': '14.0.1.0.0',
    'depends': ['account'],
    'data': [
        'reports/report.xml',
        'reports/report_invoice_khmer.xml',
        'views/report_invoice.xml',
        'views/account_move_views.xml',
    ],
    'demo': [],
    'installable': True,
    'license': 'LGPL-3', 
}
