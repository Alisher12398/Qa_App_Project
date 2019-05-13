from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

#colors https://colorscheme.ru/web-safe-colors.html

class GroupManager(models.Manager):
    def for_user(self, user):
        return self.all()

class Group(models.Model):
    title = models.CharField('Title', max_length=40)
    id_prerequisite = models.IntegerField('ID prerequisite', default=0)
    background_color = models.CharField('Background color', max_length=10)
    price = models.IntegerField('Price')

    objects = GroupManager()

    def __str__(self):
        return '{}: {}'.format(self.id, self.title)

    def get_group_id(self):
        return '{}'.format(self.id)

    def get_groups(self):
        return {
            'id': self.id,
            'title': self.title,
            'id_prerequisite': self.id_prerequisite,
            'background_color': self.background_color,
            'price': self.price,
        }

class Qa(models.Model):
    id_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    question = models.CharField('Question', max_length=512)
    answer_1 = models.CharField('Answer 1', max_length=40)
    answer_2 = models.CharField('Answer 2', max_length=40)
    answer_3 = models.CharField('Answer 3', max_length=40)
    answer_4 = models.CharField('Answer 4', max_length=40)
    answer_right = models.IntegerField('Right answer')

    def __str__(self):
        return '{}: {}'.format(self.id, self.id_group)

    def get_questions(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer_1': self.answer_1,
            'answer_2': self.answer_2,
            'answer_3': self.answer_3,
            'answer_4': self.answer_4,
            'answer_right': self.answer_right,
        }

# class User(models.Model):
#     name = models.CharField(max_length=40)
#     firstname= models.CharField(max_length=30, null=True)
#     points = models.IntegerField()
#     password = models.CharField(max_length=40)
#
#     def __str__(self):
#         return '{}: {}'.format(self.id, self.name)
#
#     def get_password(self):
#         return {
#             'password' : self.password,
#         }
#
#     def get_user_points(self):
#         return {
#             'points': self.points,
#         }
#
#     def get_user(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'points': self.points,
#         }
#
#     def get_name(self):
#         return self.name
#
#     def get_id(self):
#         return self.id

class DataManager(models.Manager):
    def for_user(self, user):
        return self.filter(id_user=user)

class Data(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    points = models.IntegerField('Points')

    objects = DataManager()

    def __str__(self):
        return '{}: {}'.format(self.id_user, self.id_group)

    def get_user_points(self):
        return {
            'points': self.points,
        }

    def get_group_points(self):
        return {
            'id': self.id,
            'id_group': self.id_group.get_group_id(),
            'points': self.points,
        }

class GroupsPurchasesManager(models.Manager):
    def for_user(self, user):
        return self.filter(id_user=user)

class GroupsPurchases(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_group = models.ForeignKey(Group, on_delete=models.CASCADE)

    objects = GroupsPurchasesManager()
    def __str__(self):
        return '{}: {}'.format(self.id_user, self.id_group)

    def get_user_group_purchases(self):
        return {
            'id': self.id,
            'id_user': self.id_user,
            'id_group': self.id_group,
        }
    def get_id(self):
        return '{}'.format(self.id)


class Company(models.Model):
    name = models.CharField('Name', max_length=60)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def get_companies(self):
        return {
            'id': self.id,
            'name': self.name,
        }
    def get_company(self):
        return '{}'.format(self.name)

    def get_id(self):
        return '{}'.format(self.id)


class Offers(models.Model):
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=100)

    def __str__(self):
        return '{}:{} {}'.format(self.id, self.id_company, self.title)

    def get_offers(self):
        return {
            'id': self.id,
            'id_company': self.id_company.get_company(),
            'title': self.title,
        }

    def get_id(self):
        return '{}'.format(self.id)

    def get_id_value(self):
        return self.id

    def get_id2(self):
        return self.id


def generate_promocode(offer):
    date = datetime.now()
    day = 100 - int(date.day)
    month = int((str(date.month)[::-1]))
    promocode = str(offer) +'/' + str(day) + str(month)
    return promocode

class OffersPurchasesManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

class OffersPurchases(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    id_offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    promocode = models.CharField('Promocode', max_length=100, null=True)
    purchase_day = models.DateTimeField('Purchase day', default=datetime.now(), blank=True)

    objects = OffersPurchasesManager()

    def __str__(self):
        return '{}: {}'.format(self.owner, self.id_offer)

    def get_promocode(self):
        return generate_promocode(self.id_offer.get_id2())

    def get_user_offers(self):
        return {
            'id': self.id,
            'id_user': self.owner.id,
            'id_offer': self.id_offer.get_id(),
            'purchase_day': self.purchase_day,
            'promocode': self.get_promocode(),
        }