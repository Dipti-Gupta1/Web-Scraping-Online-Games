from selectolax.parser import Node, HTMLParser
from typing import Union


def parse_raw_attributes(node: Union[Node,str] , selectors: list[dict]):
    if not issubclass(Node, type(node)):
        node = HTMLParser(node)


    parsed = {}
    matched = None

    for s in selectors:
        match = s.get('match')
        type_ = s.get('type')
        selector = s.get('selector')
        name = s.get('name')

        if match == 'all':
            matched = node.css(selector)

            if type_ == 'text':
                parsed[name] = [node.text() for node in matched]
            elif type_ == 'node':
                parsed[name] = matched

        elif match == 'first':
            matched = node.css_first(selector)

            if type_ == 'text':
                parsed[name] = matched.text() if matched else None
            elif type_ == 'node':
                parsed[name] = matched

        elif name in ["discount","original price", "sale price","currency"]:
            price_container = node.css_first('.StoreSalePriceWidgetContainer')
            if price_container:
                price_element = price_container.css_first(selector)
                parsed[name] = price_element.text() if price_element else None

        # elif name in ["discount"]:
        #     # Find the elements containing discount, MRP, and original price
        #     price_container = node.css_first('.StoreSalePriceWidgetContainer')
        #     if price_container:
        #         price_element = price_container.css_first(selector)
        #         parsed[name] = price_element.text().replace('-','').replace('%','') if price_element else None
        #
        # elif name in ["currency"]:
        #     price_container = node.css_first('.StoreSalePriceWidgetContainer')
        #     if price_container:
        #         price_curr = price_container.css_first(selector)
        #         if price_curr:
        #             text = price_curr.text().strip()
        #             match_ = re.search(r"([^\d\.]+?)(\d+(?:,\d{3})*(?:\.\d+)?)", text)
        #             if match_:
        #                 currency_symbol, price_value = match_.groups()
        #                 parsed[name] = currency_symbol
        #             else:
        #                 None

    return parsed


