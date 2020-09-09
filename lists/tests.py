from django.test import TestCase
from lists.models import Item


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        item_text = 'A new list item'
        response = self.client.post('/', data={'item_text': item_text})
        self.assertIn(item_text, response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item_text = 'The first (ever) list item'
        second_item_text = 'Item the second'
        first_item = Item(text=first_item_text)
        first_item.save()

        second_item = Item(text=second_item_text)
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item, second_saved_item = saved_items
        self.assertEqual(first_saved_item.text, first_item_text)
        self.assertEqual(second_saved_item.text, second_item_text)
