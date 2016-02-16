from unittest import TestCase

import dataserviceclient

class TestJoke(TestCase):
    def test_is_string(self):
        s = dataserviceclient.file()
        self.assertTrue(isinstance(s, str))

