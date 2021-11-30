from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app
import unittest
import requests_mock
from typing import Text


class TestBase(TestCase):
    def create_app(self):
        return app

    def test_number(self):
        response = self.client.get(url_for('number'))
        if response == "1":
            self.assertIn(b"1", response.data)
        #if self.assertIn(b"2", response.data):
            #pass
        #if self.assertIn(b"3", response.data):
            #pass

