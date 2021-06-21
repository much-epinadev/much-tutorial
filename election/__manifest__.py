# -*- coding: utf-8 -*-
{
    'name': "election",

    'summary': """
        Official US Election App
        """,
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/candidate.xml',
        'views/voter.xml',
        'wizards/data_import.xml',
    ],
}
