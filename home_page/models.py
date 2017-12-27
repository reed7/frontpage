from django.db import models


class MyProfile(models.Model):
    greeting = models.CharField(max_length=256)
    about = models.TextField(max_length=1024)


class ContactMethod(models.Model):
    CONTACT_TYPES = [
        ('tt', 'Twitter'),
        ('fb', 'Facebook'),
        ('em', 'Email'),
        ('wc', 'WeChat'),
        ('ma', 'Mailing'),
        ('gh', 'Github'),
        ('cp', 'Codepen'),
        ('lk', 'Linkedin'),
        ('ce', 'Cellphone'),
        ('ot', 'Other'),
    ]

    profile = models.ForeignKey(MyProfile, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=256)
    contact_type = models.CharField(max_length=2, unique=True, choices=CONTACT_TYPES)

    def __str__(self):
        for type in self.CONTACT_TYPES:
            if self.contact_type == type[0]:
                return type[1]

        return 'Other'


class QuestionAnswer(models.Model):
    profile = models.ForeignKey(MyProfile, on_delete=models.CASCADE)
    question = models.CharField(max_length=256)
    answer = models.TextField(max_length=1024)
    display = models.BooleanField(default=True)
    display_order = models.IntegerField(unique=True, default=0)
