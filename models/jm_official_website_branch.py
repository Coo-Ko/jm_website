#-*- coding: utf-8 -*-
from openerp.exceptions import UserError, ValidationError
from openerp import api, fields, models


class JM_official_website_school(models.Model):

    _name = 'jm.official.website.school'

    name = fields.Char(u'院校名称')
    webadd = fields.Char(u'网址')
    area_con = fields.Char(u'所属地区')


class JM_official_website_area(models.Model):

    _name = 'jm.official.website.area'

    name = fields.Char(u'地区名称')
    image = fields.Binary(u"图片")
    school = fields.One2many('jm.official.website.school','area_con',string=u"直属院校")