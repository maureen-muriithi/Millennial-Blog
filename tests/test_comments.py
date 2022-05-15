
from app.models import Comment, User
from app import db
def setUp(self):
        self.user_Moh = User(username = 'James',password = 'potato', email = 'james@ms.com')
        # self.new_comment = Comment(movie_id=12345,movie_title='Review for movies',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='This movie is the best thing since sliced bread',user = self.user_James )

