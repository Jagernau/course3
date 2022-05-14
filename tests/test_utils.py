import pytest
from sys import path
path.append("../")
from utils import ToGet

posts = ToGet("../data/posts.json")
coments = ToGet("../data/comments.json")
keys_expect = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


#тесты корректности файла
def test_type():
    """проверяет введёный арумент str"""
    with pytest.raises(TypeError):
        ToGet(67)


def test_path():
    """проверяет верность пути"""
    assert ToGet("../dta/poss.json").get_posts_all() is None


def test_json_file():
    """если json написан с ошибками"""
    assert ToGet("../data/testing.json").get_posts_all() is None


def test_json_types():
    """проверяет верный возврат типов файлов"""
    assert (
        isinstance(ToGet("../data/posts.json").get_posts_all(), list)
    ), "Загруженный json должн быть листом"
    assert isinstance(posts.get_posts_all()[
                      0], dict), "Посты должны быть словарём"


def test_keys():
    """проверяет есть ли такие ключи"""
    post_keys = posts.get_posts_all()[0]
    first_post_keys = set(post_keys.keys())
    assert first_post_keys == keys_expect, "Полученные ключи не совпадают"


#тесты по запросам

#pk
def test_one_post_type_pk():
    """проверяет тип одного поста по pk"""
    post_pk = posts.get_post_by_pk(1)
    assert type(post_pk) == dict, "тип поста должен быть словарём"


def test_one_post_keys_pk():
    """проверка количества ключей"""
    post_pk_keys = posts.get_post_by_pk(1)
    assert set(post_pk_keys) == keys_expect, "полученные ключи не совпадают"


params = [1,2,3,4,5,6,7,8]
@pytest.mark.parametrize("pk", params)
def test_one_post_by_params_pk(pk):
    """верно ли количество постов по pk"""
    post = posts.get_post_by_pk(pk)
    assert post["pk"] == pk, "номера постов не совпадают"

#user_name
def test_one_post_type_user_name():
    """проверяет тип одного поста по user_name"""
    post_user_name = posts.get_posts_by_user("leo")
    assert type(post_user_name) == list, "тип выдачи постов должен быть list"


post_params_by_users = [("leo",{1,5}), ("larry", {4,8}),("hank", {3,7})]
@pytest.mark.parametrize("name, correct_pk", post_params_by_users)
def test_one_post_by_params_user_name(name, correct_pk):
    """проверяет номера постов с именами запостивших"""
    postes = posts.get_posts_by_user(name)
    post_pks = set()
    for i in postes:
        post_pks.add(i["pk"])
    assert post_pks == correct_pk, "pk не сходятся с именами запостивших"



