{
    'name': 'Library Extensions',
    'version': '1.0.0',
    'category': 'Library',
    'summary': 'Extensions for the Library Management System',
    'description': """
        This module extends the library management system with:
        - Author field for books
        - Book categories
        - Enhanced views
    """,
    'author': 'Patrick Odev',
    'website': 'https://www.odevsolutions.com',
    'depends': ['library'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_category_views.xml',
        'views/library_book_views.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}