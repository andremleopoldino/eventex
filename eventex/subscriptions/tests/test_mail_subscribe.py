
from django.core import mail
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscriptions


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='André Leopoldino', cpf='12345678901', email='andrem01310@gmail.com', phone = '11-98353-9575')
        self.response = self.client.post('/inscricao/', data)
        self.mail = mail.outbox[0]


    def test_send_subscribe_email(self):
        self.assertEqual(1,len(mail.outbox))


    def test_save_subscription(self):
        self.assertTrue(Subscriptions.objects.exists())

    def test_subscription_email_subject(self):
        
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.mail.subject)

    def test_subscription_email_from(self):
        
        expect = 'andrem01310@gmail.com'

        self.assertEqual(expect, self.mail.from_email)

    def test_subscription_email_to(self):
        
        expect = ['andrem01310@gmail.com' , 'andrem01310@gmail.com']

        self.assertEqual(expect, self.mail.to)

    
    def test_subscription_message(self):
        email = mail.outbox[0]
        expect = 'Inscrição realizada com sucesso ! Obrigado pelo interesse no Eventex! O maior encontro de hackers do mundo!'


        contents = [
            'André Leopoldino',
            '12345678901', 
            'andrem01310@gmail.com',
            '11-98353-9575'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.mail.body)
      