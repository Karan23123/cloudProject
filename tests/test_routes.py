import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.client.get('/post/1')  # Adjust based on available posts
        self.assertEqual(response.status_code, 200)

    def test_admin_page(self):
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
