import unittest
from sdsd import values_map, title_map, swap


class Test_avito(unittest.TestCase):


    def test_valmap(self):
        test_dict = {'values': [{'id': 100, 'value': 50}, {'id': 50, 'value': 'Кириллица'}, {'id': 77, 'value': 'Septim'}]}
        result_actual = values_map(test_dict, val_dict={})
        result_expected = {100: 50, 50: 'Кириллица', 77: 'Septim'}
        self.assertEqual(result_actual, result_expected)


    def test_titlemap(self):
        test_title = {'params': [{'id': 123, 'title': 'Title_1'}, {'id': 45, 'values': [{'id': 56, 'values': [{'id': 67, 'title': 'Title_2', 'values': [{'id': 78, 'title': 'Title_3'}]}]}]}]}
        result_actual = title_map(test_title, title_dict=None)
        result_expected = {123: 'Title_1', 67: 'Title_2', 78: 'Title_3'}
        self.assertEqual(result_actual, result_expected)


    def test_update(self):
        values = {123: 1, 345: 11, 567: 111}
        title = {1: 'Title_1', 11: 'Title_2', 111: 'Title_3'}
        structure = {'params': [{'id': 123, 'title': '', 'value': '', 'values': [{'id': 345, 'title': '', 'value': '', 'params': [{'id': 567, 'value': ''}]}]}]}
        result_expected = {'params': [{'id': 123, 'title': '', 'value': 'Title_1', 'values': [{'id': 345, 'title': '', 'value': 'Title_2', 'params': [{'id': 567, 'value': 'Title_3'}]}]}]}
        result_actual = swap(structure, values, title)
        self.assertEqual(result_actual, result_expected)



unittest.main()