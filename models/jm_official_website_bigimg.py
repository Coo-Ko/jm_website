#-*- coding: utf-8 -*-
from openerp.exceptions import UserError, ValidationError
from openerp import api, fields, models

class Jm_official_website_bigimg(models.Model):
    _name = 'jm.official.website.bigimg'
    _rec_name = 'image'

    image = fields.Binary(u'照片', attachment=True)