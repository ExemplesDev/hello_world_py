import pytest
from message import Message

class TestMessage(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run""" 

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run""" 

    def setUp(self):
        """This method is run once before _each_ test method is executed""" 

    def teardown(self):
        """This method is run once after _each_ test method is executed""" 

    def test_init(self):
        hello = Message()
        assert hello.message == "Hello" 

    def test_exists(self):
        hello = Message()
        assert hello.exists() == True
