from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import Item

@csrf_exempt
def get_all_items(request):
    if request.method == "GET":
        items = list(Item.objects.values())
        return JsonResponse(items, safe=False)

@csrf_exempt
def filter_items(request):
    if request.method == "GET":
        search = request.GET.get("search", "")
        items = list(Item.objects.filter(name__icontains=search).values())
        return JsonResponse(items, safe=False)

@csrf_exempt
def add_item(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            item = Item.objects.create(name=data["name"], description=data.get("description", ""))
            return JsonResponse({"message": "Item added successfully", "item_id": item.id}, status=201)
        except KeyError:
            return JsonResponse({"error": "Invalid data"}, status=400)

@csrf_exempt
def get_item(request, item_id):
    if request.method == "GET":
        item = get_object_or_404(Item, id=item_id)
        return JsonResponse({"id": item.id, "name": item.name, "description": item.description})

@csrf_exempt
def update_item(request, item_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            item = get_object_or_404(Item, id=item_id)
            item.name = data.get("name", item.name)
            item.description = data.get("description", item.description)
            item.save()
            return JsonResponse({"message": "Item updated successfully"})
        except KeyError:
            return JsonResponse({"error": "Invalid data"}, status=400)

@csrf_exempt
def delete_item(request, item_id):
    if request.method == "DELETE":
        item = get_object_or_404(Item, id=item_id)
        item.delete()
        return JsonResponse({"message": "Item deleted successfully"})
