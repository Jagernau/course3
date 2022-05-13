import pytest
from sys import path
path.append("../")
from utils import ToGet

#posts = ToGet("../data/posts.json")
#coments = ToGet("../data/comments.json")



def test_type():
    with pytest.raises(TypeError):
        ToGet(67)

def test_path():
    assert ToGet("../dta/poss.json").get_posts_all() == None

def test_json_file():
    assert ToGet("../data/testing.json").get_posts_all()== None

