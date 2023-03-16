import unittest
from flaskr import create_app

class TestAuth(unittest.TestCase):
    def setUp(self):
        # Create the application and a test client for testing
        self.app = create_app()
        self.client = self.app.test_client()

    def test_login_page_loads(self):
        # Test if the login page is accessible and returns a 200 status code
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    # Run the tests when this script is executed
    unittest.main()