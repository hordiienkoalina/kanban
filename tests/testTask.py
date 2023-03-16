import unittest
from flaskr import create_app, db
from flaskr.models import User, Task

class TestKanban(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    def test_create_task(self):
        with self.app.app_context():
            # Create a test user
            test_user = User(email="test@example.com", password="test123")
            db.session.add(test_user)
            db.session.commit()

            # Log in as the test user
            self.client.post('/login', data={
                'email': 'test@example.com',
                'password': 'test123'
            })

            # Create a task for the test user
            response = self.client.post('/add_task', data={
                'title': 'Test Task',
                'description': 'This is a test task',
                'status': 'To Do'
            }, follow_redirects=True)

            # Check if the task was successfully added
            self.assertIn(b'Test Task', response.data)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == '__main__':
    unittest.main()
