{
    'name': 'Hospital',
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for hospital automation:'
               ' keeping records of doctors and patients.',
    'license': 'LGPL-3',
    'author': 'Oleksandr Yevpak',
    'website': '',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/disease_category_data.xml',
        'data/disease_data.xml',
        'views/hospital_menus.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/doctor_schedule_views.xml',
        'views/disease_views.xml',
        'views/disease_category_views.xml',
        'views/visit_views.xml',
        'views/diagnosis_views.xml',
        'views/personal_doctor_history_views.xml',
        'views/disease_history_views.xml',
        'views/analysis_views.xml',
        'wizard/personal_doctor_change_views.xml',
        'wizard/disease_report_wizard_views.xml',
        'wizard/disease_report_count_wizard_views.xml',
        'wizard/filling_doctor_chart_wizard_views.xml',
    ],
    'demo': [
        'data/doctor_demo.xml',
        'data/patient_demo.xml'
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
