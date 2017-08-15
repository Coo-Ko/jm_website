#-*- coding:utf-8 -*-
from openerp import api, fields, models

class jm_official_web_news_one(models.Model):
    _name = 'jm.official.web.news.one'
    _rec_name = 'title'

    title = fields.Char(u'标题')
    author = fields.Char(u'作者')
    date = fields.Date(u'创建时间')
    source = fields.Char(u'来源')
    content = fields.Text(u'内容')
    intro = fields.Text(u'简介')
    image = fields.Binary(u'显示图片', attachment=True)


class jm_official_web_news_two(models.Model):
    _name = 'jm.official.web.news.two'
    _rec_name = 'title'

    title = fields.Char(u'标题')
    author = fields.Char(u'作者')
    date = fields.Date(u'创建时间')
    source = fields.Char(u'来源')
    intro = fields.Text(u'简介')
    content = fields.Text(u'内容')
    image = fields.Binary(u'显示图片', attachment=True)

class jm_official_web_news_three(models.Model):
    _name = 'jm.official.web.news.three'
    _rec_name = 'title'

    title = fields.Char(u'标题')
    author = fields.Char(u'作者')
    date = fields.Date(u'创建时间')
    source = fields.Char(u'来源')
    intro = fields.Text(u'简介')
    content = fields.Text(u'内容')
    image = fields.Binary(u'显示图片', attachment=True)