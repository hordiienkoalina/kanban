import unittest
from flaskr import create_app, db
from flaskr.models import User

class TestAuth(unittest.TestCase):
    def setUp(self):
        # Set up the test app and client
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        
        # Create the test database
        db.create_all(app=self.app)

    def test_existing_email(self):
        # Creating a dummy user for testing
        test_user = User(email="test@example.com", password="test123")
        with self.app.app_context():
            # Add and commit the test user to the database
            db.session.add(test_user)
            db.session.commit()

        # Send a POST request to the '/signup' route with a duplicate email
        response = self.client.post('/signup', data={
            'email': 'test@example.com',
            'password': 'test456'
        })
        # Check if the response contains the expected error message
        self.assertIn(b'Email address already exists', response.data)

if __name__ == '__main__':
    unittest.main()