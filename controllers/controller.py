# -*- conding:utf-8  -*-
from openerp import http
import json
import jinja2,sys,os
from openerp.http import request

class Jm_official_website_controllers(http.Controller):

    def load_env(self):
        if hasattr(sys, 'frozen'):
            # When running on compiled windows binary, we don't have access to package loader.
            path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'views'))
            loader = jinja2.FileSystemLoader(path)
        else:
            loader = jinja2.PackageLoader('openerp.addons.jm_official_website', "views/jinjahtml")
        env = jinja2.Environment(loader=loader, autoescape=True)
        return env

    @http.route('/homepage/', type='http', auth='public', csrf=False)
    def render_homepage(self):
        news_one = request.env['jm.official.web.news.one'].search([], order='id desc', limit=6)
        news_two = request.env['jm.official.web.news.two'].search([], order='id desc', limit=6)
        news_three = request.env['jm.official.web.news.three'].search([], order='id desc', limit=6)
        advanced_team = request.env['jm.official.website.advanced.team'].search([], order='id desc', limit=6)
        advanced_person = request.env['jm.official.website.advanced.person'].search([], order='id desc', limit=6)
        our_school = request.env['jm.official.website.area'].search([], order='id')
        our_culture = request.env['jm.official.website.culture'].search([], order='id', limit=4)
        bigimgs = request.env['jm.official.website.bigimg'].search([], order='id desc', limit=5)


        env = self.load_env()
        return env.get_template('index.html').render({
            'news_one':news_one,
            'news_two':news_two,
            'news_three':news_three,
            'advanced_team':advanced_team,
            'advanced_person':advanced_person,
            'our_school':our_school,
            'our_culture':our_culture,
            'bigimgs':bigimgs,
        })

    @http.route('/contact/', type='http', auth='public', csrf=False)
    def render_contact(self):
        env = self.load_env()
        return env.get_template('contact.html').render({})

    @http.route('/recruit/', type='http', auth='public', csrf=False)
    def render_recruit(self):
        env = self.load_env()
        return env.get_template('recruit.html').render({})

    @http.route('/news/<string:which>/<int:index>', type='http', auth='public', csrf=False)
    def render_news_details(self, index, which):
        env = 'jm.official.web.news.' + which
        templates_obj = request.env[env]
        news_one = templates_obj.browse(int(index))

        next_obj = templates_obj.search([('id', '<', int(index))], order='id desc', limit=1)
        pre_obj = templates_obj.search([('id', '>', int(index))], order='id',limit=1)

        env = self.load_env()
        return env.get_template('news.html').render({
            'obj':news_one,
            'next_obj':next_obj,
            'pre_obj':pre_obj,
        })

    @http.route(['/newsList/<string:which>/<int:page>', '/newsList/<string:which>/'], type='http', auth='public', csrf=False)
    def render_newsList(self, page=1, search='', which='one', **post):
        ppg = 10
        env = 'jm.official.web.news.' + which
        if search:
            domain = ['|', ('title','ilike',search),('content','ilike',search)]
            news_one_count = request.env[env].search_count(domain)
            news_one = request.env[env].search(domain)

        else:
            news_one_count = request.env[env].search_count([])
            news_one = request.env[env].search([], order='id desc')

        all_page = news_one_count/ppg if news_one_count % page == 0 else news_one_count/ppg + 1
        if page == 1:
            pre_page = '#'
        else:
            pre_page = '/newsList/%s/%s' %(which, page - 1)
        if news_one_count > (page-1)*ppg and news_one_count <= page*ppg:
            news_show = [news_one[i] for i in range((page-1)*ppg, news_one_count)]
            next_page = '#'
        if news_one_count > page*ppg:
            news_show = [news_one[i] for i in range((page - 1)*ppg, page*ppg)]
            next_page = '/newsList/%s/%s' %(which, page+1)

        #print news_show

        env = self.load_env()
        return env.get_template('news_list.html').render({
            'news_show':news_show,
            'pre_page':pre_page,
            'page':page,
            'next_page':next_page,
            'all_page':all_page + 1,
            'all_news':news_one_count,
            'which':which,
        })

    @http.route('/disedu/', type='http', auth='public', csrf=False)
    def render_disedu(self):
        schools = request.env['jm.official.website.disedu.school'].search([], order='id')
        schools_length = request.env['jm.official.website.disedu.school'].search_count([])
        honor = request.env['jm.official.website.disedu.honor'].search([], order='id')
        topimg = request.env['jm.official.website.disedu.topimg'].search([], order='id')
        honor_length = request.env['jm.official.website.disedu.honor'].search_count([])
        excellent_stu = request.env['jm.official.website.disedu.excellent.student'].search([('type', '=', 1)], order='id desc', limit=6)
        excellent_stu_group = request.env['jm.official.website.disedu.excellent.student'].search([('type', '=', 2)], order='id desc', limit=6)
        env = self.load_env()
        return env.get_template('disedu.html').render({
            'schools':schools,
            'schools_length':schools_length,
            'schools_page':int(schools_length/4 +1) if schools_length % 4 != 0 else int(schools_length/4),
            'honor':honor,
            'honor_length':honor_length,
            'honor_page':int(honor_length/2 +1) if honor_length % 2 != 0 else int(honor_length/2),
            'excellent_stu':excellent_stu,
            'excellent_stu_group':excellent_stu_group,
            'topimg':topimg,
        })

    @http.route('/recruit/type/', type='http', auth='public', csrf=False)
    def render_recruit_type(self, **post):
        types = request.env['jm.official.website.recruit.type'].search([], order='id')
        data = {'subject':[]}
        for type in types:
            data['subject'].append({
                'name':type.name,
                'value':type.id,
            })

        data = json.dumps(data)
        if post.get('callback'):
            data = post.get('callback') + "(" + data + ")"
            return data
        else:
            return data

    @http.route('/recruit/details/<int:tid>', type='http', auth='public', csrf=False)
    def render_recruit_details(self, tid,**post):
        positions = request.env['jm.official.website.recruit'].search([('type', '=', tid)], order='id')
        data = {'subject': []}
        for position in positions:
            data['subject'].append({
                'name':position.name,
                'details':position.details,
            })

        data = json.dumps(data)
        if post.get('callback'):
            data = post.get('callback') + "(" + data + ")"
            return data
        else:
            return data

    @http.route('/cop/type/', type='http', auth='public', csrf=False)
    def render_cop_type(self, **post):
        types = request.env['jm.official.website.cop.type'].search([], order='id')
        data = {'subject': []}
        for type in types:
            data['subject'].append({
                'name': type.name,
                'value': type.id,
            })

        data = json.dumps(data)
        if post.get('callback'):
            data = post.get('callback') + "(" + data + ")"
            return data
        else:
            return data

    @http.route('/copschool/details/<int:tid>', type='http', auth='public', csrf=False)
    def render_copschool_details(self, tid, **post):
        positions = request.env['jm.official.website.copschool'].search([('type', '=', tid)], order='id')

        data = {'subject': []}
        for position in positions:
            img1 = request.env['ir.attachment'].search([
                ('res_model', '=', 'jm.official.website.copschool'),
                ('res_id', '=', position.id),
                ('res_field', '=', 'image1')
            ])
            img2 = request.env['ir.attachment'].search([
                ('res_model', '=', 'jm.official.website.copschool'),
                ('res_id', '=', position.id),
                ('res_field', '=', 'image2')
            ])
            data['subject'].append({
                'name': position.name,
                'image1':'/web/content/%s' % img1.id,
                'image2':'/web/content/%s' % img2.id,
                'desc': position.desc,
            })

        data = json.dumps(data)
        if post.get('callback'):
            data = post.get('callback') + "(" + data + ")"
            return data
        else:
            return data

    @http.route('/coopschools/', type='http', auth='public', csrf=False)
    def render_coopschools(self,):

        env = self.load_env()
        return env.get_template('coopschool.html').render({

        })

    @http.route(['/culture/get/<int:id>/', '/culture/get/'], type='http', auth='public', csrf=False)
    def render_culture_get(self, id=None, **post):
        data = {}
        if not id:
            clutures = request.env['jm.official.website.culture'].search([], order='id')
            data['subject'] = []
            for cluture in clutures:
                data['subject'].append({
                    'name':cluture.title,
                    'value':cluture.id,
                })
        else:
            cluture = request.env['jm.official.website.culture'].browse(id)
            data['content'] = cluture.content
        data = json.dumps(data)
        if post.get('callback'):
            data = post.get('callback') + "(" + data + ")"
            return data
        else:
            return data

    @http.route(['/culture/get/history/'], type='http', auth='public', csrf=False)
    def render_culture_history(self, **post):
        data = []
        request.env.cr.execute("select distinct(year) from jm_official_website_culture_history")
        years = request.env.cr.fetchall()
        for year in years:
            events = request.env['jm.official.website.culture.history'].search([('year', '=', year)])
            contents = []
            for event in events:
                content = {'month':event.month,'content':event.content,}
                contents.append(content)

            data.append({'year':year[0], 'event':contents})

        data = json.dumps(data)
        if post.get('callback'):
            data = post.get('callback') + "(" + data + ")"
            return data
        else:
            return data

    @http.route('/culture/', type='http', auth='public', csrf=False)
    def render_culture(self,):
        env = self.load_env()
        return env.get_template('culture.html').render({

        })



