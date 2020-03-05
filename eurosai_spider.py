# This is a spider for scrapy in Python
# We crawl through the 230 pages of audits published on the EuroSAI website
# We extract for each report : title, link to the report, subjects, year of publishing, countries

import scrapy
 
class EurosaiSpider(scrapy.Spider):
    name = "eurosai"
 
    def start_requests(self):
        url_root = "https://www.eurosai.org/en/databases/audits/index.html?page="
        urls = [url_root + str(i) for i in range(1,231)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        
        for row in response.xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/div[1]/table/tbody//tr"):
            yield {'title' : row.xpath('td[1]//text()').extract_first(),
                   'link' : row.xpath('td[1]//a/@href').extract(),
                   'subject' : row.xpath('td[2]//p//text()').extract(),
                   'year': row.xpath('td[3]//text()').extract_first(),
                   'country' : row.xpath('td[4]//p//text()').extract()
            }