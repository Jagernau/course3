import pytest
from sys import path
path.append("../")
from utils import ToGet

posts = ToGet("../data/posts.json")
coments = ToGet("../data/comments.json")



