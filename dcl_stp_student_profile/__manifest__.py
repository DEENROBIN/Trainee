{
    'name': 'Student Profile',
    'version': '1.0',
    'summary': 'Manage student-related configurations',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/dcl_stp_student_menu.xml',
        'views/dcl_stp_student_class_view.xml',
        'views/dcl_stp_student_section.xml',
        'views/dcl_stp_student_institute.xml',
        # 'views/student_section_view.xml',
        # 'views/student_institute_view.xml',
    ],
    'installable': True,
    'application': True,
}
