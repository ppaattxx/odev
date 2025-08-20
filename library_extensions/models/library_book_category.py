from odoo import models, fields, api

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Library Book Category'
    _rec_name = 'name'

    name = fields.Char(
        string='Category Name',
        required=True,
        help='Name of the book category'
    )
    
    book_ids = fields.Many2many(
        'library.book',
        string='Books',
        help='Books in this category'
    )

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Category name must be unique!')
    ]