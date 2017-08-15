#-*- coding: utf-8 -*-
from openerp.exceptions import UserError, ValidationError
from openerp import api, fields, models

class Jm_official_website_culture(models.Model):
    _name = 'jm.official.website.culture'
    _rec_name = 'title'

    title = fields.Char(u'标题')
    desc = fields.Text(u'简介')
    content = fields.Text(u'内容')

class Jm_official_website_culture_history(models.Model):
    _name = 'jm.official.website.culture.history'
    _rec_name = 'month'

    year = fields.Char(u'年份')
    month = fields.Char(u'月份')
    content = fields.Text(u'内容')