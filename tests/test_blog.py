from app.models import Blog, User, Comment
from app import db
def setUp(self):
        self.user_Moh = User(username = 'Moh',password = 'potato', email = 'moh@ms.com')
        self.new_blog = Blog(id=1, title='A blog about busness', post='ctfgvbhjnmk l ,mkj nhbgv jcfhd restfyk ulhnmkoj nhbgv jfchdxsg  edrftgyhu ljmkn bmvncxd hcfjgykuhjnk. bvngcfxd' )
        self.new_comment = Comment(comment = "Nice", post_id = self.new_blog.id, user_id = self.user_Moh.id)

def test_instance(self):
        self.assertTrue(isinstance(self.user_Moh, User))
        self.assertTrue(isinstance(self.new_blog, Blog))
        self.assertTrue(isinstance(self.new_comment, Comment))
