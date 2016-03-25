from django.shortcuts import render, HttpResponse, loader
from models import Building, Bathroom, Comment
import json

def defaultencode(o):
    if isinstance(o, Decimal):
        # Subclass float with custom repr?
        return fakefloat(o)
    raise TypeError(repr(o) + " is not JSON serializable")

def index(request):
    latest_question_list = "yoooo"
    context = {'latest_question_list': latest_question_list}

    buildings = Building.objects.all()

    context = {'buildings': buildings}
    return render(request, 'app/index.html', context)

def building_detail(request, building_url):

    building = Building.objects.get(url = building_url)
    bathrooms = Bathroom.objects.filter(in_building = building)
    context = {'building': building, 'bathrooms': bathrooms}
    return render(request, 'app/building_detail.html', context)

def bathroom_detail(request, bathroom_url):

    bathroom = Bathroom.objects.get(url = bathroom_url)
    comments = Comment.objects.all().filter(for_bathroom = bathroom).order_by('-date')
    context = {'bathroom': bathroom, 'comments': comments}
    return render(request, 'app/bathroom_detail.html', context)

def get_comments(request, bathroom_url):

    bathroom = Bathroom.objects.get(url = bathroom_url)
    comments = Comment.objects.filter(for_bathroom = bathroom)
    comment_texts = []
    for i in comments:
        comment_texts.append(i.comment_text)

    results = {"comment_texts": comment_texts}
    return HttpResponse(json.dumps(results, default=defaultencode), content_type="application/json")

def add_comment(request):

    if request.method == 'POST':
        data = request.POST.get("data")
    elif request.method == 'GET':
        data = request.GET.get("data")

    data = json.loads(data)

    bathroom_url = data['bathroom']
    bathroom = Bathroom.objects.get(url = bathroom_url)

    comment_in = data['comment']
    votes_test = 1

    new_comment = Comment(for_bathroom = bathroom, comment_text = comment_in, votes = votes_test)
    new_comment.save()

    return HttpResponse("")
