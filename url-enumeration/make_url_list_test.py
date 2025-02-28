import unittest
import makeUrlList


class MyTestCase(unittest.TestCase):
    def test_given_one_sign_when_add_urls_should_create_urls(self):
        words = ["w1", "w2"]
        url_list = []
        makeUrlList.add_urls("HTTPS://{$}", words, url_list)
        self.assertEqual("HTTPS://w1", url_list[0])
        self.assertEqual("HTTPS://w2", url_list[1])


if __name__ == '__main__':
    unittest.main()
