import unittest
from unittest.main import main
import requests
from run import app, testFunctions


class TestGETStatusCode(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/"
    BOARDS = None
    POSTS = None

    with app.app_context():
        x = testFunctions
        BOARDS = x.listBoard()
        POSTS = x.listPosts()

    def test_index(self):
        r = requests.get(TestGETStatusCode.API_URL)
        self.assertEqual(r.status_code, 200)

    def test_board(self):
        for boardName in TestGETStatusCode.BOARDS:
            r = requests.get(TestGETStatusCode.API_URL + '/b/' + boardName[1])
            self.assertEqual(r.status_code, 200)

    def test_posts(self):
        for post in TestGETStatusCode.POSTS:
            print(post[1])
            r = requests.get(TestGETStatusCode.API_URL +
                             '/b/' + post[1] + '/reply/' + str(post[0]))
            self.assertEqual(r.status_code, 404)

    def test_static_pages(self):
        r = requests.get(TestGETStatusCode.API_URL + '/about')
        self.assertEqual(r.status_code, 200)
        r = requests.get(TestGETStatusCode.API_URL + '/rules')
        self.assertEqual(r.status_code, 200)

class TestPOSTStatusCodes(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/"
    BOARD_OBJ = {
        "board_name": "Web Series",
        "board_description": "posts only related to web series and not tv shows. TV Show discussion in Television board"
    }

    def test_board_creation(self):
        r = requests.post(TestPOSTStatusCodes.API_URL + 'createBoard/', json=TestPOSTStatusCodes.BOARD_OBJ)
        self.assertEqual(r.status_code, 201)

    
BOARDS = None
POSTS = None

with app.app_context():
    x = testFunctions
    BOARDS = x.listBoard()
    POSTS = x.listPosts()
