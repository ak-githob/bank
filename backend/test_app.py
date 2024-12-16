import unittest
from app import app  


class TestOpenAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True
    
    def test_open_account_success(self):
        response = self.app.post('/open_account', json={
            'email': 'test@example.com',
            'balance': 1000,
            'document': 'document.pdf'
        })
        self.assertEqual(response.status_code, 200)
        # Check the response data
        data = response.get_json()
        self.assertIn('account_id', data)
    
    def test_invalid_balance(self):
        response = self.app.post('/open_account', json={
            'email': 'test@example.com',
            'balance': -100,  # Invalid balance
            'document': 'document.pdf'
        })
        self.assertEqual(response.status_code, 400)  # Check for bad request

    def test_invalid_document_format(self):
        response = self.app.post('/open_account', json={
            'email': 'test@example.com',
            'balance': 500,
            'document': 'invalid_format.txt'  # Invalid format
        })
        self.assertEqual(response.status_code, 400)

    def test_invalid_email(self):
        response = self.app.post('/open_account', json={
            'email': 'invalid_email',  # Invalid email format
            'balance': 500,
            'document': 'document.pdf'
        })
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
