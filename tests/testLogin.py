import unittest
from flaskr import create_app

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_login_page_loads(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()