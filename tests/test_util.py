import urllib

from helga_quip.util import quote_groupdict, quote_group
from unittest import TestCase

class TestUtilMethods(TestCase):

    quoteList1 = ['a']
    groupdict1 = {'a': '12?\/ # 456 ', 'b': '# $ ? 7412 asd'}
    quoteList2 = ['1']
    group1 = ['twas\' /brillig', '12? \/ # 456 ', 'and the slithy toves']
    
    def test_quote_groupdict(self):
        result = quote_groupdict(self.groupdict1, self.quoteList1)
        self.assertEqual(result['a'], urllib.quote(self.groupdict1['a']))
        self.assertEqual(result['b'], self.groupdict1['b'])

    def test_quote_group(self):
        result = quote_group(self.group1, self.quoteList2)
        self.assertEqual(result[1], urllib.quote(self.group1[1]))
        self.assertEqual(self.group1[0], result[0])
        self.assertEqual(self.group1[2], result[2])

    def test_quote_group_empty(self):
        result = quote_group(None, [])
        quip = "foo".format(*result)
        self.assertEqual("foo", quip)
        

if __name__ == '__main__':
    unittest.main()
