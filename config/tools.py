import json

_config = {
    "url": f'https://store.steampowered.com/specials',
    "container":
        {
            "name": "store sale divs",
            "selector": 'div[class*="UlvFkP8Oew4a6VTHCvLNH _34o914Rd3YiwTjnvyTgVbb Focusable"]',
            "match": "all",
            "type": "node"
        }
    ,
    "item": [
        {

            "name": "title",
            "selector": 'div[class*="StoreSaleWidgetTitle"]',
            "match": "first",
            "type": "text"
        },
        {

            "name": "thumbnail",
            "selector": 'div[class*= "CapsuleImageCtn"] img',
            "match": "first",
            "type": "node"
        },

        {
            "name": "tags",
            "selector": 'div[class="_3OSJsO_BdhSFujrHvCGLqV"] > a',
            "match": "all",
            "type": "text"
        },

        {
            "name": "release_date",
            "selector": 'div[class="_3eOdkTDYdWyo_U5-JPeer1"]',
            "match": "first",
            "type": "text"
        },
        {
            "name": "sale price",
            "selector": 'div[class*=" StoreSalePriceWidgetContainer"]  div[class="Wh0L8EnwsPV_8VAu8TOYr"]',
            "match": "text",
            "type": "first"
        },
        {
            "name": "discount",
            "selector": 'div[class*=" StoreSalePriceWidgetContainer"] > div[class="_2fpFvkG2gjtlAHB3ZxS-_7"]',
            "match": "text",
            "type": "first"
        },
        {
            "name": "original price",
            "selector": 'div[class*=" StoreSalePriceWidgetContainer"]  div[class="_1EKGZBnKFWOr3RqVdnLMRN"]',
            "match": "text",
            "type": "first"
        },
{
            "name": "currency",
            "selector": 'div[class*=" StoreSalePriceWidgetContainer"]  div[class="_1EKGZBnKFWOr3RqVdnLMRN"]',
            "match": "text",
            "type": "first"
        },
        {
            "name": "description",
            "selector": 'div[class*=" StoreSaleWidgetShortDesc"]',
            "match": "first",
            "type": "text"
        },
        {
            "name": "review_sentiment",
            "selector": 'a[class*=" ReviewScore"] > div:nth-of-type(1) > div',
            "match": "first",
            "type": "text"
        },
        {
            "name": "number_of_review",
            "selector": 'a[class*=" ReviewScore"] > div:nth-of-type(1) > div:nth-of-type(2)',
            "match": "first",
            "type": "text"
        }


     ]
}


#Other - attributes.get('src')


def get_config(load_from_file=False):
    if load_from_file:
        with open("config.json", 'r') as f:
            return json.load(f)
    return _config
def generate_config():
    with open('config.json','w') as f:
        json.dump(_config, f, indent=4)

if __name__ =='__main__':
    generate_config()



