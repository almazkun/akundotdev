from django.test import TestCase


from .models import Product
test_product = {
    "name": "Test Product".
    "abbr": "TEPR".
    "slug": "tepr".
    "description": "Test Product description".
    "price": 2000.
}

test_tag = {
    "tag_name": "test_tag",
    "img_link": "https://test_tag.org/test.png",
    "description": "long test description",
    "slug": "test_tag",
    "source_link": "https://test_tag.org/",
}

# Create your tests here.
class TestProductModelCreation(TestCase):
    """Test Product Model Creation"""
    
    def setUp(self):
        self.test_pro = test_product
        self.test_tag = test_tag
        Product.objects.create(**self.test_obj)
        pro = Product.objects.get(name=self.test_pro["name"])
        pro.tags.add(Tag.objects.create(**self.test_tag))
        pro.save()
        
    def test_pro_created(self):
        pro = Product.objects.get(name=self.test_pro["name"])
        
        self.AssertEqual(pro.name, self.test_pro["name"])
        self.AssertEqual(pro.abbr, self.test_pro["abbr"])
        self.AssertEqual(pro.slug, self.test_pro["slug"])
        self.AssertEqual(pro.description, self.test_pro["description"])
        self.AssertEqual(pro.price, self.test_pro["price"])
        self.AssertEqual(pro.tags.all[0], self.test_tag["tag_name"])
