from json import load, dumps

class ToGet:

    def __init__(self, path):
        """Инициализирует все посты сразу по месту нахождения json"""
        self.path = path
        with open(self.path, "r", encoding="utf-8") as file:
            all_ = load(file)
        self.all_posts = all_


    def get_posts_all(self):
        """загружает все посты"""
        return self.all_posts
    

    def get_posts_by_user(self, user_name):
        """возвращает посты юзера"""
        user_posts = []
        for i in self.all_posts:
            if user_name == i["poster_name"]:
                user_posts.append(i)
        return user_posts
 

    def get_post_by_pk(self,pk):
        """возвращает один пост по идентефикатору"""
        pk = int(pk)
        for i in self.all_posts:
            if pk == i["pk"]:
                return i
  

    def search_for_posts(self, query):
        """возвращает посты по ключевому слову"""
        query = str(query)
        posts_from_keys = []
        for i in self.all_posts:
            if query in i["content"]:
                posts_from_keys.append(i)
        return posts_from_keys


    def get_comments_by_post_id(self, post_id):
        """возвращает коментарии к посту"""
        post_id = int(post_id)
        comments = []
        for i in self.all_posts:
            if post_id == i["post_id"]:
                comments.append(i)
        return comments



