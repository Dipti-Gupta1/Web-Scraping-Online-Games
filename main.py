
from selectolax.parser import HTMLParser
from Utils.Extract import extract_full_body_html
from config.tools import get_config
from Utils.process import format_and_transform, convert_into_csv
from Utils.parse import parse_raw_attributes

url = f'https://store.steampowered.com/specials'
if __name__ == '__main__':
    config = get_config()
    html = extract_full_body_html(
        from_url=config.get('url'),
        wait_for=config.get('container').get('selector')
    )

    nodes = parse_raw_attributes(html,[config.get('container')])
    # tree = HTMLParser(html)
    #
    # divs = tree.css(config.get('container').get('selector'))
    # print(len(divs))

    game_data = []
    for node in nodes.get("store sale divs"):
        attrs = parse_raw_attributes(node, config.get("item"))
        attrs = format_and_transform(attrs)
        game_data.append(attrs)
    print(game_data)

file = convert_into_csv(game_data)




