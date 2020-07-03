from django.test import TestCase
from django.urls import reverse


from .models import Tag, Article
from apps.users.models import CustomUser
from .views import HomepageListView, ArticleListView, ArticleDetailView


test_tag = {
    "tag_name": "test_tag",
    "img_link": "https://test_tag.org/test.png",
    "description": "long test description",
    "slug": "test_tag",
}

test_article = {
    "title": "test_article",
    "slug": "test_article",
    "description": "long test description",
    "content": "long test context",
    "img_link": "https://test_tag.org/test.png",
    "views": 100,
    "is_published": True,
}

normal_user = {"username": "normal", "email": "normal@user.com", "password": "foo"}

# Create your tests here.
class TestTagModel(TestCase):
    def test_tag_model(self):
        Tag.objects.create(**test_tag)
        obj = Tag.objects.get(tag_name=test_tag["tag_name"])

        self.assertEqual(obj.tag_name, test_tag["tag_name"])
        self.assertEqual(obj.img_link, test_tag["img_link"])
        self.assertEqual(obj.description, test_tag["description"])
        self.assertEqual(obj.slug, test_tag["slug"])


class TestArticleModel(TestCase):
    def test_article_model(self):
        CustomUser.objects.create_user(**normal_user)
        author = CustomUser.objects.get(username=normal_user["username"])
        test_article["author"] = author
        Article.objects.create(**test_article)
        obj = Article.objects.get(title=test_article["title"])

        self.assertEqual(obj.title, test_article["title"])
        self.assertEqual(obj.slug, test_article["slug"])
        self.assertEqual(obj.author, test_article["author"])
        self.assertEqual(obj.description, test_article["description"])
        self.assertEqual(obj.content, test_article["content"])
        self.assertEqual(obj.img_link, test_article["img_link"])
        self.assertEqual(obj.views, test_article["views"])
        self.assertEqual(obj.is_published, test_article["is_published"])


class TestHomepageListView(TestCase):
    def test_home(self):
        response = self.client.get(reverse("home"))

        self.assertTemplateUsed(response, "articles/home.html")
        self.assertEqual(response.status_code, 200)


class TestArticleListView(TestCase):
    def test_articles(self):
        response = self.client.get(reverse("articles"))

        self.assertTemplateUsed(response, "articles/articles.html")
        self.assertEqual(response.status_code, 200)


class TestArticleDetailView(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(**normal_user)
        test_article["author"] = CustomUser.objects.get(
            username=normal_user["username"]
        )
        Article.objects.create(**test_article)

    def test_article_detail(self):
        obj = Article.objects.get(title=test_article["title"])
        response = self.client.get(
            reverse("article_detail", kwargs={"slug": test_article["slug"]})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "articles/article_detail.html")
