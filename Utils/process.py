from selectolax.parser import Node
from datetime import datetime
import re
import pandas as pd
from xlsxwriter import xmlwriter

def get_attrs_from_node(node: Node, attr: str):
    if Node is None or not issubclass(Node, type(node)):
        raise ValueError('Expects a selectolax Node to be provided')

    return node.attributes.get(attr)


def get_first_n(input_list: list, n: int = 10):
    return input_list[:5]


# 'Dec 10, 2020' %b %d %Y --> %Y-%m-%d
def reformat_date(date_: str, input_format: str = '%b %d, %Y', output_format: str = '%Y-%m-%d'):
    dt_obj = datetime.strptime(date_, input_format)
    return datetime.strftime(dt_obj, output_format)


def regex(input_str: str, pattern: str, do_what: str = "findall", input_attr:dict={}):
    if do_what == 'findall':
        return re.findall(pattern, input_str)
    elif do_what == 'split':
        return re.split(pattern, input_str)
    elif do_what == 'search':
        match1 = re.search(pattern, input_str).group()
        return match1
        if match1:
            if 'currency' in input_attr:
                return match1.group()
            else:
                try:
                    result = match1.group()
                    return result
                except ValueError:
                    return None
    else:
        raise ValueError
    if not input_attr:
        return print('Not a valid attribute')


def format_and_transform(attr: dict):
    transforms = {
        "thumbnail": lambda n: get_attrs_from_node(n, 'src'),
        "tags": lambda input_list: get_first_n(input_list, 5),
        "release_date": lambda date_: reformat_date(date_, '%b %d, %Y', '%Y-%m-%d'),
        "number_of_review": lambda raw: int(''.join(regex(raw, r'\d', "findall"))),
        "discount": lambda raw: regex(raw, r'[0-9,.]+', "search"),
        "currency": lambda raw: regex(raw, r'^\D+', "search"),
        "original price": lambda raw: float(regex(raw, r'[0-9,.]+', 'search').replace(',','')),
        "sale price": lambda raw: float(regex(raw, r'[0-9,.]+','search').replace(',',''))

    }

    for k, v in transforms.items():
        if k in attr:
            attr[k] = v(attr[k])

    attr['discount value'] = attr['original price'] - attr['sale price']

    return attr

def convert_into_csv(data: list[dict]=None, filename="extract"):
    if data is None:
        raise ValueError ("The function expects data to be provided as a list of dict")
    else:
        df = pd.DataFrame(data)
        filename = f"{datetime.now().strftime('%Y_%m_%d')}_{filename}.csv"
        df.to_csv(filename, index=False, encoding='utf-8-sig')
