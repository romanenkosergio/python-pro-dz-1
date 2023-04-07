import re


def parse(query: str) -> dict:
    f"""
    This function parses a query string like 'name=ferret&color=purple'
    and returns a dictionary with the parsed query parameters.
    Parameters:
        query (str): a query string to parse
    Returns:
        dict: a dictionary with parsed query parameters  
    """

    # Check if query is a string
    if type(query) != str:
        raise TypeError('Query must be a string')

    # Check if query has a question mark
    if '?' in query:
        substring_query = query[query.find('?') + 1:]
        substring_query = re.sub(r'\?+', '', substring_query)
        substring_query = re.sub(r'=+', '=', substring_query)
        substring_query = re.sub(r'&+', '&', substring_query)

        # Check if query has something after question mark
        if substring_query == '':
            return {}

        # Check if query has '&' at the end
        if substring_query[-1] == '&':
            substring_query = substring_query[:-1]

        # Split query by '&' and '='
        split_query = [i.split('=') for i in substring_query.split('&')]

        return {i[0]: i[1] for i in split_query}

    return {}


if __name__ == '__main__':
    print(parse('https://example.com/path/to/page?name=ferret&color=purple'))
    print(parse('https://example.com/path/to/page??name=ferret&color=purple'))
    print(parse('https://example.com/path/to/page?name=ferret&color=purple&'))
    print(parse('https://example.com/path/to/page?name=ferret&color=purple&&'))
    print(parse('https://example.com/path/to/page?name=ferret&color==purple'))
    print(parse('http://example.com/'))
    print(parse('http://example.com/?'))
    print(parse('http://example.com/?name=Dima'))
    print(parse('http://example.com/?name='))
    print(parse(''))


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
