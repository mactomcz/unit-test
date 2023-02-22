import unittest
import poc_def
import test_data


class TestMain(unittest.TestCase):

    def test_download_table(self):
        func = poc_def.download_table('a')
        self.assertIsInstance(func, dict)

    def test_create_rates_list(self):
        func = poc_def.create_rates_list(test_data.data)
        result = test_data.result
        self.assertListEqual(func, result)

    def test_get_headers(self):
        func = poc_def.get_headers()
        result = test_data.headers
        self.assertListEqual(func, result)


if __name__ == '__main__':
    unittest.main()

