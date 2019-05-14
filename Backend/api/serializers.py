from rest_framework import serializers
from api.models import *
from auth_.serializers import UserSerializer

# class ContactSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True)
#     phone = serializers.CharField(required=True)
#     owner = UserSerializer(read_only=True)
#
#     def create(self, validated_data):
#         contact = Contact(**validated_data)
#         contact.save()
#         return contact
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.phone = validated_data.get('phone',instance.phone)
#         instance.save()
#         return instance

class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    id_prerequisite = serializers.IntegerField(required=True)
    background_color = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)

    def create(self, validated_data):
        group = Group(**validated_data)
        group.save()
        return group

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.id_prerequisite = validated_data.get('id_prerequisite', instance.id_prerequisite)
        instance.background_color = validated_data.get('background_color', instance.background_color)
        instance.price = validated_data.get('price', instance.price)
        instance.save()

class QaSerizlizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    id_group = GroupSerializer(read_only=True)
    question = serializers.CharField(required=True)
    answer_1 = serializers.CharField(required=True)
    answer_2 = serializers.CharField(required=True)
    answer_3 = serializers.CharField(required=True)
    answer_4 = serializers.CharField(required=True)
    answer_right = serializers.IntegerField(required=True)

    def create(self, validated_data):
        qa = Qa(**validated_data)
        qa.save()
        return qa

    def update(self, instance, validated_data):
        instance.question = validated_data.get('question', instance.question)
        instance.answer_1 = validated_data.get('answer_1', instance.answer_1)
        instance.answer_2 = validated_data.get('answer_3', instance.answer_2)
        instance.answer_3 = validated_data.get('answer_3', instance.answer_3)
        instance.answer_4 = validated_data.get('answer_4', instance.answer_4)
        instance.answer_right = validated_data.get('answer_right', instance.answer_right)
        instance.save()

class UserInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True)
    user_points = serializers.IntegerField(required=True)
    avatar = serializers.CharField(required=True)
    id_offers = OffersSerializer(read_only=True)

    def create(self, validated_data):
        user = UserInfo(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        intance.username = validated_data.get('username', instance.username)
        instance.save()    


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        company = Company(**validated_data)
        company.save()
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

class OffersSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    id_company = CompanySerializer(read_only=True)
    title = serializers.CharField(required=True)

    def create(self, validated_data):
        offer = Offers(**validated_data)
        offer.save()
        return offer

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()

class OffersPurchasesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = UserSerializer(read_only=True)
    id_offer = OffersSerializer(read_only=True)
    promocode = serializers.CharField()
    purchase_day = serializers.DateTimeField(required=True)

    def create(self, validated_data):
        offer = Offers(**validated_data)
        offer.save()
        return offer

    def update(self, instance, validated_data):
        instance.promocode = validated_data.get('promocode', instance.promocode)
        instance.purchase_day = validated_data.get('purchase_day', instance.purchase_day)
        instance.save()
