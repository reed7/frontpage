from django.test import TestCase
from .models import ContactMethod


class ContactMethodTest(TestCase):

    def test_str(self):
        cm = ContactMethod()
        cm.contact_type = "tt"

        self.assertEqual(cm.__str__(), "Twitter")

        cm.contact_type = "abc"
        self.assertEqual(cm.__str__(), "Other")

    def test_create(self):
        cm = ContactMethod()
        cm.contact_type = "tt"
        cm.address = "reed7"

        cm.save()

        cm_li = ContactMethod.objects.all()
        self.assertEqual(cm_li[0].__str__(), "Twitter")

    def test_update(self):
        cm = ContactMethod()
        cm.contact_type = "tt"
        cm.address = "reed7"

        cm.save()

        cm_li = ContactMethod.objects.all()
        self.assertEqual(cm_li[0].__str__(), "Twitter")

        new_cm = cm_li[0]
        new_cm.contact_type = "fb"
        new_cm.save()

        cm_li = ContactMethod.objects.all()
        self.assertEqual(cm_li[0].__str__(), "Facebook")
        self.assertEqual(cm_li[0].address, "reed7")