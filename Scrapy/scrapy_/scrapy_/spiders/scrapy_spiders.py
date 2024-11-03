from typing import Any
import scrapy
from scrapy.http import Response
from ..items import ScrapyItem


class _scrapySpiders(scrapy.Spider):
    name = "coke"
    start_urls = [
        "https://www.thecocktaildb.com/browse/letter/a"
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        items = ScrapyItem()
        image_url = response.css('div img::attr(src)').extract()
        title = response.css('div a::text').extract()


        items["image_url"] = image_url
        items["title"] = title

        l=[]
        ll=[]
        for ele in items["title"]:
            if len(ele)>8:
                l.append(ele)
        items.update({"title": l})

        for ele in items["image_url"]:
            if "https" in ele:
                ll.append(ele)

        items.update({"image_url": ll})
        lll=[]
        for ele in zip(items["image_url"],items["title"]):
            lll.append({ele[0]:ele[1]})
        print(lll)

        yield items