import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2

        first_post = TimelinePost.get(TimelinePost.id == 1)
        assert first_post.name == 'John Doe'
        assert first_post.email == 'john@example.com'
        assert first_post.content == 'Hello world, I\'m John!'
        assert first_post.created_at is not None

        second_post = TimelinePost.get(TimelinePost.id == 2)
        assert second_post.name == 'Jane Doe'
        assert second_post.email == 'jane@example.com'
        assert second_post.content == 'Hello world, I\'m Jane!'
        assert second_post.created_at is not None

        timeline_posts = TimelinePost.select()
        assert len(timeline_posts) == 2

        first_post.delete_instance()
        timeline_posts = TimelinePost.select()
        assert len(timeline_posts) == 1

        second_post.delete_instance()
        timeline_posts = TimelinePost.select()
        assert len(timeline_posts) == 0
