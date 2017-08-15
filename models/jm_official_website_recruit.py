#-*- coding: utf-8 -*-
from openerp.exceptions import UserError, ValidationError
from openerp import api, fields, models

class Jm_official_website_recruit_type(models.Model):
    _name = 'jm.official.website.recruit.type'
    _rec_name = 'name'

    name = fields.Char(u'招聘方式')

class Jm_official_website_recruit(models.Model):
    _name = 'jm.official.website.recruit'
    _rec_name = 'name'

    name = fields.Char(u'岗位')
    type = fields.Many2one('jm.official.website.recruit.type', u'招聘方式')
    details = fields.Text(u'岗位要求')