import unittest
from main import parse_cookie


class TestParse(unittest.TestCase):

    def test_normal_case(self):
        """Test normal case"""
        parse_data = parse_cookie('name=Dima')
        self.assertEqual(parse_data, {'name': 'Dima'})

    def test_semicolon_in_end(self):
        """Test with semicolon"""
        parse_data = parse_cookie('name=Dima;age=28;')
        self.assertEqual(parse_data, {'name': 'Dima', 'age': '28'})

    def test_double_equal_between_value(self):
        """Test double '=' between value"""
        parse_data = parse_cookie('name=Dima=User;age=28;')
        self.assertEqual(parse_data, {'name': 'Dima=User', 'age': '28'})

    def test_double_equal_between_key_and_value(self):
        """Test double '=' between key and value"""
        parse_data = parse_cookie('name=Dima=User;age==28;')
        self.assertEqual(parse_data, {'name': 'Dima=User', 'age': '28'})

    def test_empty_string(self):
        """Test the empty string"""
        parse_data = parse_cookie('')
        self.assertEqual(parse_data, {})

    def test_no_key(self):
        """Test no key"""
        parse_data = parse_cookie('=Dima;age=28;')
        self.assertEqual(parse_data, {'age': '28'})

    def test_no_value(self):
        """Test no value"""
        parse_data = parse_cookie('name=Dima;age=;')
        self.assertEqual(parse_data, {'name': 'Dima', 'age': ''})

    def test_with_comma(self):
        """Test question mark and name"""
        parse_data = parse_cookie('name=Dima,age=28;')
        self.assertEqual(parse_data, {})

    def test_with_space(self):
        """Test with space"""
        parse_data = parse_cookie('name=Dima age=28;')
        self.assertEqual(parse_data, {})

    def test_with_semicolon_after_equal(self):
        """Test question mark and name and equal"""
        parse_data = parse_cookie('name=Dima;age=;28;')
        self.assertEqual(parse_data, {'name': 'Dima', 'age': ''})


if __name__ == '__main__':
    unittest.main()
