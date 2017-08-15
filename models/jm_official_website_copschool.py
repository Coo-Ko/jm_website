#-*- coding: utf-8 -*-
from openerp.exceptions import UserError, ValidationError
from openerp import api, fields, models

class Jm_official_website_cop_type(models.Model):
    _name = 'jm.official.website.cop.type'
    _rec_name = 'name'

    name = fields.Char(u'教育类型')

class Jm_official_website_copschool(models.Model):
    _name = 'jm.official.website.copschool'
    _rec_name = 'name'

    name = fields.Char(u'学校名称')
    type = fields.Many2one('jm.official.website.cop.type', u'教育类型')
    image1 = fields.Binary(u'图片1', attachment=True, store=True)
    image2 = fields.Binary(u'图片2', attachment=True, store=True)
    desc = fields.Text(u'学校描述')