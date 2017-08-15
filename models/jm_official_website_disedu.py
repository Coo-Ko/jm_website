#-*- coding: utf-8 -*-
from openerp.exceptions import UserError, ValidationError
from openerp import api, fields, models

class Jm_official_website_disedu_topimg(models.Model):
    _name = 'jm.official.website.disedu.topimg'

    image = fields.Binary(u"图片", attachment=True)
    url = fields.Char(u'网址')

class Jm_official_website_disedu_shcool(models.Model):
    _name = 'jm.official.website.disedu.school'

    image = fields.Binary(u"图片", attachment=True)
    url = fields.Char(u'网址')

class Jm_official_website_disedu_honor(models.Model):
    _name = 'jm.official.website.disedu.honor'
    _rec_name = 'desc'

    image = fields.Binary(u"图片", attachment=True)
    desc = fields.Char(u'描述')


class Jm_official_website_disedu_excellent_student(models.Model):
    _name = 'jm.official.website.disedu.excellent.student'
    _rec_name = 'desc'

    type = fields.Selection([(1, '独照'), (2, '合照')], string=u'类别')
    image = fields.Binary(u"图片")
    desc = fields.Char(u'描述')
