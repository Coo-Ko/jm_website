#-*- coding: utf-8 -*-
from openerp.exceptions import UserError, ValidationError
from openerp import api, fields, models

class Jm_official_website_advanced_team(models.Model):
    _name = 'jm.official.website.advanced.team'

    name = fields.Char(u'团队名称')
    desc = fields.Text(u'描述')
    image = fields.Binary(u'照片', attachment=True)



class Jm_official_website_advanced_person(models.Model):
    _name = 'jm.official.website.advanced.person'

    name = fields.Char(u'姓名')
    desc = fields.Text(u'描述')
    image = fields.Binary(u'照片', attachment=True)