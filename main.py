import re

def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    """
    Parse cookie string and return dict with key-value pairs
    Params:
        query (str): string to parse
    Return:
        dict: dictionary with key-value pairs
    """

    # Check type of query
    if type(query) != str:
        raise TypeError('Query must be a string')

    if ',' in query or ' ' in query:
        return {}

    # Check if query has an empty string
    if query == '':
        return {}

    # Check if query has a semicolon
    if '=' in query:

        # Check if query has a semicolon at the end
        if query[-1] == ';':
            # Remove semicolon at the end
            query = query[:-1]

        query = re.sub(r'=+', '=', query)
        query = re.sub(r';+', ';', query)

        # Split query by semicolon
        query = query.split(';')

        # Create a dictionary
        result_dict = {}

        # Iterate over query
        for item in query:

            # Split item by equal sign
            item = item.split('=', 1)

            if item[0] == '' or len(item) == 1:
                continue

            # Add key-value pair to dictionary
            result_dict[item[0]] = item[1]
        return result_dict

    return {}


if __name__ == '__main__':
    print(parse_cookie('name=Dima'))
    print(parse_cookie('name=Dima;age=28;'))
    print(parse_cookie('name=Dima=User;age=28;'))
    print(parse_cookie('name=Dima=User;age==28;'))
    print(parse_cookie(''))
    print(parse_cookie('=Dima;age=28;'))
    print(parse_cookie('name=Dima;age=;'))
    print(parse_cookie('name=Dima,age=28;'))
    print(parse_cookie('name=Dima age=28;'))
    print(parse_cookie('name=Dima;age=;28;'))
