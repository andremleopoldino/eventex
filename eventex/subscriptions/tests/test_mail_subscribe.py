
from django.core import mail
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='André Leopoldino', cpf='12345678901', email='budapythonico@gmail.com', phone = '11-98353-9575')
        self.response = self.client.post('/inscricao/', data)
        self.mail = mail.outbox[0]


    def test_send_subscribe_email(self):
        self.assertEqual(1,len(mail.outbox))

    def test_subscription_email_subject(self):
        
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.mail.subject)

    def test_subscription_email_from(self):
        
        expect = 'budapythonico@gmail.com'

        self.assertEqual(expect, self.mail.from_email)

    def test_subscription_email_to(self):
        
        expect = ['budapythonico@gmail.com' , 'budapythonico@gmail.com']

        self.assertEqual(expect, self.mail.to)

    
    def test_subscription_message(self):
        email = mail.outbox[0]
        expect = 'Inscrição realizada com sucesso ! Obrigado pelo interesse no Eventex! O maior encontro de hackers do mundo!'

        contents = [
            'André Leopoldino',
            '12345678901', 
            'budapythonico@gmail.com',
            '11-98353-9575'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.mail.body)
      