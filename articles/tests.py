from django.test import TestCase
from .models import Article

class ArticleModelTests(TestCase):
    def test_article_str_returns_title(self):
        article = Article.objects.create(title="Test", content="Test Content")
        self.assertEqual(str(article), "Test")

    def test_search_finds_articles(self):
        Article.objects.create(title="Angeln", content="Köder am Fluss")
        Article.objects.create(title="Köderwahl", content="Beste Methode")
        response = self.client.get('/', {'q': 'köder'})
        self.assertContains(response, "Angeln")
        self.assertContains(response, "Köderwahl")
