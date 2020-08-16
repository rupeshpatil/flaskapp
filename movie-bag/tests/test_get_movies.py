import unittest
import json

from tests.BaseCase import BaseCase

class TestGetMovies(BaseCase):

    def test_empty_response(self):
        response = self.app.get('/api/movies')
        self.assertListEqual(response.json, [])
        self.assertEqual(response.status_code, 200)

