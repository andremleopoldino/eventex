from datetime import datetime

from django.test import TestCase

from eventex.subscriptions.models import Subscriptions


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscriptions(
        name='André Moreira Leopoldino',
        cpf=12345678901,
        email='andrem01310@gmail.com',
        phone='11983539575'
        )
        self.obj.save()
    
    def test_create(self):
        
        self.assertTrue(Subscriptions.objects.exists())
    

    def get_created_at(self):
        """Subscription mut have auto created attr"""
        self.assertIsInstance(self.obj.created_at, datetime)


    def test_str(self):
        self.assertEqual('André Moreira Leopoldino', str(self.obj))