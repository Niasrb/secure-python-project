import unittest
from src.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        response = self.app.get('/api/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "healthy"})

    def test_get_data(self):
        response = self.app.get('/api/data')
        self.assertEqual(response.status_code, 200)
        self.assertTrue("items" in response.get_json())

if __name__ == '__main__':
    unittest.main()