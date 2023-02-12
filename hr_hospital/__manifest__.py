{
    'name': 'Hospital',
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'summary': '',
    'license': 'LGPL-3',
    'author': 'evpak128',
    'website': '',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/disease_data.xml',
        'views/hospital_menus.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/disease_views.xml',
        'views/visit_views.xml',
    ],
    'demo': [
        'data/doctor_demo.xml',
        'data/patient_demo.xml'
    ],
    'support': '',
    'application': False,
    'installable': True,
    'auto_install': False,
}
