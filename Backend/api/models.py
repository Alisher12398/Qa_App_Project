from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

#colors https://colorscheme.ru/web-safe-colors.html

class Group(models.Model):
    title = models.CharField(max_length=40)
    image_name = models.CharField(max_length=60)
    price = models.IntegerField()

    def __str__(self):
        return '{}: {}'.format(self.id, self.title)

    # def get_group_id(self):
    #     return '{}'.format(self.id)
    #
    # def get_groups(self):
    #     return {
    #         'id': self.id,
    #         'title': self.title,
    #         'image_name': self.image_name,
    #         'price': self.price,
    #     }
#
class Qa(models.Model):
    id_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    question = models.CharField(max_length=512)
    answer_1 = models.CharField(max_length=40)
    answer_2 = models.CharField(max_length=40)
    answer_3 = models.CharField(max_length=40)
    answer_4 = models.CharField(max_length=40)
    answer_right = models.IntegerField()

    def __str__(self):
        return '{}: {}'.format(self.id, self.id_group)

    # def get_questions(self):
    #     return {
    #         'id': self.id,
    #         'question': self.question,
    #         'answer_1': self.answer_1,
    #         'answer_2': self.answer_2,
    #         'answer_3': self.answer_3,
    #         'answer_4': self.answer_4,
    #         'answer_right': self.answer_right,
    #     }


# # class ProfileManager(models.Manager):
# #     def for_user(self, user):
# #         return self.filter(owner=user)
#
#
#
#
#
#
# # class User(models.Model):
# #     name = models.CharField(max_length=40)
# #     firstname= models.CharField(max_length=30, null=True)
# #     points = models.IntegerField()
# #     password = models.CharField(max_length=40)
# #
# #     def __str__(self):
# #         return '{}: {}'.format(self.id, self.name)
# #
# #     def get_password(self):
# #         return {
# #             'password' : self.password,
# #         }
# #
# #     def get_user_points(self):
# #         return {
# #             'points': self.points,
# #         }
# #
# #     def get_user(self):
# #         return {
# #             'id': self.id,
# #             'name': self.name,
# #             'points': self.points,
# #         }
# #
# #     def get_name(self):
# #         return self.name
# #
# #     def get_id(self):
# #         return self.id
#
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

    # def get_user_points(self):
    #     return {
    #         'points': self.points,
    #     }
    #
    # def get_group_points(self):
    #     return {
    #         'id': self.id,
    #         'id_group': self.id_group.get_group_id(),
    #         'points': self.points,
    #     }

# class GroupsPurchasesManager(models.Manager):
#     def for_user(self, user):
#         return self.filter(id_user=user)
#
# class GroupsPurchases(models.Model):
#     id_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     id_group = models.ForeignKey(Group, on_delete=models.CASCADE)
#
#     objects = GroupsPurchasesManager()
#     def __str__(self):
#         return '{}: {}'.format(self.id_user, self.id_group)
#
#     def get_user_group_purchases(self):
#         return {
#             'id': self.id,
#             'id_user': self.id_user,
#             'id_group': self.id_group,
#         }
#     def get_id(self):
#         return '{}'.format(self.id)
#

class Company(models.Model):
    name = models.CharField('Name', max_length=60)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

class Offers(models.Model):
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=100)
    price = models.IntegerField()
    
    def __str__(self):
        return '{}:{} {}'.format(self.id, self.id_company, self.title)


# def generate_promocode(offer):
#     date = datetime.now()
#     day = 100 - int(date.day)
#     month = int((str(date.month)[::-1]))
#     promocode = str(offer) +'/' + str(day) + str(month)
#     return promocode

# class OffersPurchasesManager(models.Manager):
#     def for_user(self, user):
#         return self.filter(owner=user)

#     def create(self, *args, **kwargs):
#         if 'id_offer' in kwargs and isinstance(kwargs['id_offer'], str):
#             kwargs['id_offer'] = Offers.objects.get(title=kwargs['id_offer'])
#         return super(OffersPurchasesManager, self).create(*args, **kwargs)

class OffersPurchases(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    id_offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    
#     promocode = models.CharField('Promocode', max_length=100, null=True)
#     purchase_day = models.DateTimeField('Purchase day', default=datetime.now(), blank=True)
# class UserInfo(models.Model):
#     id_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     user_points = models.IntegerField(0)
#     avatar = models.CharField(max_length = 255) 
#     id_offers = models.ForeignKey(Offers, on_delete=models.CASCADE)


#     objects = OffersPurchasesManager()

    def __str__(self):
        return '{}: {}'.format(self.owner, self.id_offer)

#     def get_promocode(self):
#         return generate_promocode(self.id_offer.get_id2())

#     def get_user_offers(self):
#         return {
#             'id': self.id,
#             'id_user': self.owner.id,
#             'id_offer': self.id_offer,
#             'purchase_day': self.purchase_day,
#             'promocode': self.get_promocode(),
#         }

# class UserInfo(models.Model):
#     username = models.CharField(max_length = 40)
#     user_points = models.IntegerField(0)
#     avatar = models.CharField(max_length = 255)
#     id_offers = models.ForeignKey(Offers, on_delete=models.CASCADE)
#
#
#     def __str__(self):
#         return '{}: {}'.format(self.id, self.username)
#
#     def get_username(self):
#         return '{}'.format(self.username)
#
#     def get_id(self):
#         return '{}'.format(self.id)
#
#     def get_user_points(self):
#         return 0
#
#     def get_avatar(self):
#         return self.avatar
#
