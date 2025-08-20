from odoo import models, fields, api

class LibraryBook(models.Model):
    _inherit = 'library.book'
    
    author_id = fields.Many2one(
        'res.partner',
        string='Author',
        required=True,
        help='The author of the book'
    )
    
    category_id = fields.Many2many(
        'library.book.category',
        string='Categories',
        help='Categories this book belongs to'
    )