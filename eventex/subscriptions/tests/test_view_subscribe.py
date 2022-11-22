from django.core import mail
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """GET /inscricao/ must return status code 200"""
        self.assertEqual(200,self.response.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """HTML must contain imput tags"""
        tags = (

            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1)

            )
            
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)
       

    def test_csrf(self):
        """html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)


    def test_form_has_fields(self):
        """form must have 4 fields"""
        form = self.response.context['form']
        self.assertSequenceEqual(['name','cpf','email','phone'], list(form.fields))


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='André Leopoldino', cpf='12345678901', email='andrem01310@gmail.com', phone = '11-98353-9575')
        self.response = self.client.post('/inscricao/', data)
    
    def test_post(self):

        self.assertEqual(302, self.response.status_code)


class SubscribeInvalidPost(TestCase):
        def setUp(self):
            self.response = self.client.post('/inscricao/', {})

        def test_post(self):
            """Invalid post should not redirect"""

            
            self.assertEqual(200, self.response.status_code)


        def test_template(self):
            self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')



class SubscribeInvalidPost(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {})
        
    def test_post(self):
        self.assertEqual(200, self.response.status_code)


    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')
        
    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)


class SubscribeSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name='André Leopoldino', cpf='12345678901', email='andrem01310@gmail.com', phone = '11-98353-9575')

        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')