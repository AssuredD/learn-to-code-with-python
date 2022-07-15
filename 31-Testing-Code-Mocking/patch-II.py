import urllib.request
import unittest
from unittest.mock import patch


class WebRequest():
    def __init__(self, url):
        self.url = url

    def execute(self):
        response = urllib.request.urlopen(self.url)
        if response.status == 200:
            return "SUCCESS"

        return "FAILURE"


class WebRequestTest(unittest.TestCase):
    @patch("urllib.request.urlopen")
    def test_execute_with_sucess_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 200
        wr = WebRequest("https://www.assureddesign.co.uk")
        self.assertEqual(wr.execute(), "SUCCESS")

    @patch("urllib.request.urlopen")
    def test_execute_with_failure_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 404
        wr = WebRequest("https://www.assureddesign.co.uk")
        self.assertEqual(wr.execute(), "FAILURE")


if __name__ == "__main__":
    unittest.main()
