
from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def teste_get(self):
        
        self.assertEqual(200,self.response.status_code)

    def test_template(self):
        """must use index.html"""

        self.assertTemplateUsed(self.response,'index.html')    


    def test_subscription_link(self):
        self.assertContains(self.response, 'href="/inscricao/"')

