from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def getQroups(request):
    if request.method == 'GET':
        groups = Group.objects.all()
        json_groups = [t.get_groups() for t in groups]
        return JsonResponse(json_groups, safe=False)
    # elif request.method == 'POST':
    #     body = json.loads(request.body)
    #     if 'name' in body:
    #         taskList = TaskList(name = body['name'])
    #         taskList.save()
    #         return JsonResponse(taskList.to_json())
    return JsonResponse({'error': 'bad request'})

def getQa(request, pk):
    if request.method == 'GET':
        try:
            question = Qa.objects.get(id = pk)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        json_task = question.get_questions()
        return JsonResponse(json_task)

def getQaG(request, pk):
    if request.method == 'GET':
        try:
            groups = Group.objects.get(id = pk)
        except Group.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        qa = groups.qa_set.all()
        json_qa = [tk.get_questions() for tk in qa]
        return JsonResponse(json_qa, safe = False)

def getUser(request, nameTemp):
    if request.method == 'GET':
        try:
            user = User.objects.get(name = nameTemp)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        json_user = user.get_user()
        return JsonResponse(json_user, safe= False)
    # elif request.method == 'POST':
    #     obj = User.objects.get(name=nameTemp)
    #     obj.points = points
    #     obj.save()
        # body = json.loads(request.body)
        # if 'name' in body:
        #     taskList = TaskList(name = body['name'])
        #     taskList.save()
        #     return JsonResponse(taskList.to_json())
@csrf_exempt
def setUserPoints(request, nameTemp, points):
    if request.method == 'POST':
        obj = User.objects.get(name=nameTemp)
        obj.points = points
        obj.save()
        return JsonResponse(obj.get_user(), safe= False)


def getUserPoints(request, idUser, idGroup):
    if request.method == 'GET':
        try:
            data = Data.objects.get(id_user=idUser, id_group=idGroup)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        points = data.get_user_points()
        return JsonResponse(points, safe= False)

def getUserGroupPoints(request, idTemp):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=idTemp)
            group = Data.objects.filter(id_user=user)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        sum = {'points': 0}
        for data in group:
            sum['points'] += data.points
        return JsonResponse(sum, safe= False)

def checkPassword(request, nameTemp, passwordTemp):
    if request.method == 'GET':
        try:
            user = User.objects.get(name = nameTemp)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        is_equal = {'is_equal':False}
        password = user.get_password()
        if password['password'] == passwordTemp:
            is_equal['is_equal'] = True
        return JsonResponse(is_equal, safe= False)

def isHaveUser(request, name, password):
    user = User.objects.filter(name = name)
    if user.count() == 0:
        return False
    return True

def register(request, name, passwordTemp):

    if isHaveUser(request, name, passwordTemp):
        try:
            user = User.objects.get(name = name)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        is_equal = {'is_equal':False}
        password = user.get_password()
        if password['password'] == passwordTemp:
            is_equal['is_equal'] = True
        return JsonResponse(is_equal, safe= False)

    if not isHaveUser(request, name, passwordTemp):
        obj = User.objects.create(name = name, points=0, password=passwordTemp)
        for group in Group.objects.all():
            data = Data.objects.create(id_user=obj, id_group=group, points=0)
        is_equal = {'is_equal':True}
        return JsonResponse(is_equal, safe= False)

def getUserPointsAll(request, id):
    if request.method == 'GET':
        try:
            user = User.objects.get(id = id)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        is_equal = {'is_equal':False}
        password = user.get_password()
        if password['password'] == password:
            is_equal['is_equal'] = True
        return JsonResponse(is_equal, safe= False)


@csrf_exempt
def setEarnedPoints(request, id_user, id_group, points):
    if request.method == 'POST':
        #obj2 = Data.objects.get(id_group = id_group, id_user=id_user)
        user = User.objects.get(id=id_user)
        group = Group.objects.get(id=id_group)
        obj = Data.objects.filter(id_user=user, id_group=group).update(points=points)
        return JsonResponse(user.get_user(), safe= False)

def getPoints(request, id_user):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=id_user)
            data = Data.objects.all().filter(id_user=user)
        except Group.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        json_qa = [tk.get_group_points() for tk in data]
        return JsonResponse(json_qa, safe = False)

def getIsGroupPurchased(request, id_user, id_group):
    if request.method == 'GET':
        try:
            group = Group.objects.get(id=id_group)
            data = GroupsPurchases.objects.filter(id_user=id_user, id_group=id_group)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        is_purchased = {'is_purchased':False}
        if (data.count() != 0):
            is_purchased['is_purchased']=True
        return JsonResponse(is_purchased, safe= False)

@csrf_exempt
def addGroupPurchase(request, id_user, id_group):
    if request.method == 'POST':
        #obj2 = Data.objects.get(id_group = id_group, id_user=id_user)
        user = User.objects.get(id=id_user)
        group = Group.objects.get(id=id_group)
        obj = GroupsPurchases.objects.create(id_user=user, id_group=group)
        return JsonResponse(user.get_user(), safe= False)

def getIsOfferPurchased(request, id_user, id_offer):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=id_user)
            offer = Offers.objects.get(id=id_offer)
            data = OffersPurchases.objects.filter(id_user=user, id_offer=offer)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        is_purchased = {'is_purchased':False}
        if (data.count() != 0):
            is_purchased['is_purchased']=True
        return JsonResponse(is_purchased, safe= False)

@csrf_exempt
def addOfferPurchase(request, id_user, id_offer, promocode):
    if request.method == 'POST':
        user = User.objects.get(id=id_user)
        offer = Offers.objects.get(id=id_group)
        obj = OffersPurchases.objects.create(id_user=user, id_group=offer, promocode=promocode)
        return JsonResponse(user.get_user(), safe= False)


def getCompanies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        json_groups = [t.get_companies() for t in companies]
        return JsonResponse(json_groups, safe=False)
    return JsonResponse({'error': 'bad request'})

def getOffers(request):
    if request.method == 'GET':
        offers = Offers.objects.all()
        json_groups = [t.get_offers() for t in offers]
        return JsonResponse(json_groups, safe=False)
    return JsonResponse({'error': 'bad request'})
