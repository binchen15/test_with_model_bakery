from django.test import TestCase
from model_bakery import baker, seq
from .models import Journal, Article
from .baker_recipes import big4


class TestJournalModel(TestCase):

    def setUp(self):
        """init with one journal, and 10 articles published by this journal"""
        self.journal  = baker.make(Journal, name="Astrophysical Journal")
        self.articles = baker.make(Article, title=seq('great paper #'), 
                                   journal=self.journal, _quantity=10)

    def test_journal_persistence(self):
        self.assertIs(self.journal.id, 1)
    
    def test_journal_str_rep(self):
        self.assertEqual(str(self.journal), self.journal.name)

    def test_journal_article_relationship(self):
        """test one-to-many relationship"""
        self.assertEqual(self.journal.article_set.count(), 10)

    def test_nonpersistence_of_prepare(self):
        """baker.make() vs baker.prepare()"""
        article  = baker.prepare(Article)
        self.assertIs(article.id, None)

    def tearDown(self):
        self.journal.delete()


class TestArticleModel(TestCase):

    def setUp(self):
        self.articles = baker.make_recipe('forum.article_recipe', _quantity=10)

    def test_article_generator_via_recipe(self):
        self.assertEqual(len(self.articles), 10)

    def test_artitle_journal_name_cycle_iterator(self):
        """journal name geneated by cycling big4 array"""
        for article in self.articles:
            self.assertIn(article.journal.name, big4)

    def tearDown(self):
        for article in self.articles:
            article.delete()    
