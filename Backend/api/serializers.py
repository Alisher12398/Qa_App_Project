from rest_framework import serializers
from api.models import Group, Qa
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
#
class GroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    image_name = serializers.CharField()
    price = serializers.IntegerField()

    class Meta:
        model = Group
        fields = '__all__'

class QaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    id_group = GroupSerializer(read_only=True)
    question = serializers.CharField()
    answer_1 = serializers.CharField()
    answer_2 = serializers.CharField()
    answer_3 = serializers.CharField()
    answer_4 = serializers.CharField()
    answer_right = serializers.IntegerField()

    class Meta:
        model = Qa
        fields = '__all__'


# class QaModelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Qa
#         fields = ['id_group', 'question', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'answer_right']
#
# class DataSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     id_user = UserSerializer(read_only=True)
#     id_group = GroupSerializer(read_only=True)
#     points = serializers.IntegerField(required=True)
#
#     def create(self, validated_data):
#         data = Data(**validated_data)
#         data.save()
#         return data
#
#     def update(self, instance, validated_data):
#         instance.points = validated_data.get('points', instance.points)
#         instance.save()
#
# class GroupsPurchasesSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     id_user = UserSerializer(read_only=True)
#     id_group = GroupSerializer(read_only=True)
#
#     def create(self, validated_data):
#         groups_purchase = Company(**validated_data)
#         groups_purchase.save()
#         return groups_purchase
#
#     def update(self, instance, validated_data):
#         instance.save()
#
# class CompanySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True)
#
#     def create(self, validated_data):
#         company = Company(**validated_data)
#         company.save()
#         return company
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#
# class CompanyModelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Company
#         fields = ['id', 'name']
#
#
# class OffersSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     id_company = CompanySerializer(read_only=True)
#     title = serializers.CharField(required=True)
#
#     def create(self, validated_data):
#         offer = Offers(**validated_data)
#         offer.save()
#         return offer
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.save()
#
# class OffersPurchasesSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     owner = UserSerializer(read_only=True)
#     id_offer = OffersSerializer(read_only=True)
#     promocode = serializers.CharField()
#     purchase_day = serializers.DateTimeField(required=True)
#
#     def create(self, validated_data):
#         offer = Offers(**validated_data)
#         offer.save()
#         return offer
#
#     def update(self, instance, validated_data):
#         instance.promocode = validated_data.get('promocode', instance.promocode)
#         instance.purchase_day = validated_data.get('purchase_day', instance.purchase_day)
#         instance.save()
#
# class OffersPurchasesModelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = OffersPurchases
#         fields = ['id_offer']
#
#
# class UserInfoSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(required=True)
#     user_points = serializers.IntegerField(required=True)
#     avatar = serializers.CharField(required=True)
#     id_offers = OffersSerializer(read_only=True)
#
#     def create(self, validated_data):
#         user = UserInfo(**validated_data)
#         user.save()
#         return user
#
#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.save()
#
