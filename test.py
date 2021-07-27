try:
    import pytest
    import unittest
    from app import app

except Exception as e:
    print("Some modules are missing {}".format(e))


class FlaskTest(unittest.TestCase):

    # check for the response 200
    def test_route(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # test for content type
    def test_contest(self):
        tester = app.test_client(self)
        response = tester.get('/')
        print(response.content_type, 'text/html; charset=utf-8')
    

if __name__ == "__main__":
    unittest.main()