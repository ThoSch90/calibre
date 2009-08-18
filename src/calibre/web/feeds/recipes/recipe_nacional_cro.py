#!/usr/bin/env  python

__license__   = 'GPL v3'
__copyright__ = '2009, Darko Miletic <darko.miletic at gmail.com>'

'''
nacional.hr
'''

import re
from calibre.web.feeds.recipes import BasicNewsRecipe
from calibre.ebooks.BeautifulSoup import BeautifulSoup, Tag

class NacionalCro(BasicNewsRecipe):
    title                 = 'Nacional - Hr'
    __author__            = 'Darko Miletic'
    description           = "news from Croatia"
    publisher             = 'Nacional.hr'
    category              = 'news, politics, Croatia'    
    oldest_article        = 2
    max_articles_per_feed = 100
    delay                 = 4
    no_stylesheets        = True
    encoding              = 'utf-8'
    use_embedded_content  = False
    language              = _('Croatian')
    lang                 = 'hr-HR'
    direction            = 'ltr'    

    extra_css = '@font-face {font-family: "serif1";src:url(res:///opt/sony/ebook/FONT/tt0011m_.ttf)} body{font-family: serif1, serif} .article_description{font-family: serif1, serif}'
    
    conversion_options = {
                          'comment'          : description
                        , 'tags'             : category
                        , 'publisher'        : publisher
                        , 'language'         : lang
                        , 'pretty_print'     : True
                        }
        
    preprocess_regexps = [(re.compile(u'\u0110'), lambda match: u'\u00D0')]

    remove_tags = [dict(name=['object','link','embed'])]
    
    feeds = [(u'Najnovije Vijesti', u'http://www.nacional.hr/rss')]

    def preprocess_html(self, soup):
        soup.html['lang'] = self.lang
        soup.html['dir' ] = self.direction
        mlang = Tag(soup,'meta',[("http-equiv","Content-Language"),("content",self.lang)])
        mcharset = Tag(soup,'meta',[("http-equiv","Content-Type"),("content","text/html; charset=UTF-8")])
        soup.head.insert(0,mlang)
        soup.head.insert(1,mcharset)
        for item in soup.findAll(style=True):
            del item['style']
        return soup

    def print_version(self, url):
        rest, sep, disc = url.rpartition('/')
        return rest.replace('/clanak/','/clanak/print/')
        