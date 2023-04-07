import unittest
from main import parse


class TestParse(unittest.TestCase):
    def test_normal_case(self):
        """Test normal case"""
        parse_data = parse('https://example.com/path/to/page?name=ferret&color=purple')
        self.assertEqual(parse_data, {'name': 'ferret', 'color': 'purple'})

    def test_double_question_mark(self):
        """Test double question mark"""
        parse_data = parse('https://example.com/path/to/page??name=ferret&color=purple')
        self.assertEqual(parse_data, {'name': 'ferret', 'color': 'purple'})

    def test_question_mark_at_the_end(self):
        """Test question mark at the end"""
        parse_data = parse('https://example.com/path/to/page?name=ferret&color=purple&')
        self.assertEqual(parse_data, {'name': 'ferret', 'color': 'purple'})

    def test_double_and_at_the_end(self):
        """Test double '&' at the end"""
        parse_data = parse('https://example.com/path/to/page?name=ferret&color=purple&&')
        self.assertEqual(parse_data, {'name': 'ferret', 'color': 'purple'})

    def test_double_equal(self):
        """Test double '='"""
        parse_data = parse('https://example.com/path/to/page?name=ferret&color==purple')
        self.assertEqual(parse_data, {'name': 'ferret', 'color': 'purple'})

    def test_empty_string(self):
        """Test empty string"""
        parse_data = parse('')
        self.assertEqual(parse_data, {})

    def test_no_question_mark(self):
        """Test no question mark"""
        parse_data = parse('http://example.com/')
        self.assertEqual(parse_data, {})

    def test_question_mark_only(self):
        """Test question mark only"""
        parse_data = parse('http://example.com/?')
        self.assertEqual(parse_data, {})

    def test_question_mark_and_name(self):
        """Test question mark and name"""
        parse_data = parse('http://example.com/?name=Dima')
        self.assertEqual(parse_data, {'name': 'Dima'})

    def test_question_mark_and_name_and_equal(self):
        """Test question mark and name and equal"""
        parse_data = parse('http://example.com/?name=')
        self.assertEqual(parse_data, {'name': ''})


if __name__ == '__main__':
    unittest.main()
