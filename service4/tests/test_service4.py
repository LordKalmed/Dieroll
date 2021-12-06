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

    def test_game(self):
        response = self.client.get(url_for('/score'))
        self.assertEqual(response.status_code, 200)