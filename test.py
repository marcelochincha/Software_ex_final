import unittest
from main import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        response = self.app.get('/resource/1')
        self.assertEqual(response.status_code, 200)

    def test_home_data(self):
        response = self.app.get('/resource/1')
        self.assertEqual(response.json, {"id": 1, "name": "Resource Name"})

    def test_404_error(self):
        response = self.app.get('/resource/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Resource not found', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()

