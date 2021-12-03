from flask import Flask, request, redirect, Response, jsonify
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app
import unittest
import requests

class TestBase(TestCase):
    def create_app(self):
        return app

    def test_colour(self):
        response = self.client.get(url_for('colour'))
        result = response
        if result == "red":
            self.assertIn(b"red", response.data)
        if result == "blue":
            self.assertIn(b"blue", response.data)
        if result == "green":
            self.assertIn(b"green", response.data)
