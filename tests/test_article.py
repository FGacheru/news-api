import unittest
from app.models import Articles

class TestArticle(unittest.TestCase):

    def setUp(self):
        self.new_articles = Articles("title","https://image.tmdb.org/t/ptfukyy","article",'2020','news','date')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Articles.all_articles = []

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_articles.title,'title')
        self.assertEquals(self.new_articles.image,"2020")
        self.assertEquals(self.new_articles.description,'article')
        self.assertEquals(self.new_articles.date,'date')
        self.assertEquals(self.new_articles.articles,'news')


    def test_save_articles(self):
        '''
        test_save_article test case to test if the article object is saved into
         the article list
        '''
        self.new_articles.save_articles() # saving the new article
        self.assertEqual(len(Articles.all_articles),1)