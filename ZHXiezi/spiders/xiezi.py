from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import wget
import os


class ZHxiezidownloader(CrawlSpider):

    name = "xiezi"
    allowed_domains = ["v.yupoo.com"]
    start_urls = [
        "http://v.yupoo.com/photos/xy0594xy/collections/"
    ]

    rules = [Rule(SgmlLinkExtractor(restrict_xpaths=('//fieldset\
        //div[@class="Sets"]//a')), callback='parse_item')]

    def parse_item(self, response):

        mainpic = response.xpath("//td[@valign='top']\
        /a/img/@src").extract()[0]  # foto principal

        pics = response.xpath("//li/div/a/img/@src").extract()  # lista de fotos

        folder = response.url.split("/")[6]  # ultima parte de la url

        if not os.path.exists(folder):
            os.makedirs(folder)

        wget.download(mainpic, out=folder)

        for pic in pics:
            wget.download(pic, out=folder)
