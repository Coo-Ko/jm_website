#-*- coding: utf-8 -*-
{
    'name' : '今明官网',
    'version' : '1.0',
    'category': 'jmweb',
    'sequence': 30,
    'description': "jm-official-website",
    'author': 'CooKo',
    'depends':['base'],
    'data':[
        'views/jm_official_website_news_views.xml',
        'views/jm_official_website_branch_views.xml',
        'views/jm_official_website_disedu_views.xml',
        'views/jm_official_website_advanced_views.xml',
        'views/jm_official_website_culture_views.xml',
        'views/jm_official_website_bigimg_views.xml',
        'views/jm_official_website_copschool_views.xml',
        'views/jm_official_website_recruit_views.xml',
        'views/jm_official_website_menu.xml',
        'security/ir.model.access.csv',
            ],
    'installable': True,
    'application': True,
    'auto_install': False
}