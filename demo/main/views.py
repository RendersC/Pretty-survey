from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def home(request):
    return render(request,'main/main.html')

def about(request):
    return HttpResponse("<p align='center'>Site for questions</p>")

def saving(request):
    if request.method == "POST":
        answer1 = request.POST.get("q1")
        answer2 = request.POST.get("q2")
        answer3 = request.POST.get("q3")
        answer4 = request.POST.get("q4")
        answer5 = request.POST.get("q5")
        print(answer1,answer2,answer3,answer4,answer5)
        file_path = os.path.join(os.path.dirname(__file__), "text.txt")
        with open(file_path,'a',encoding="utf-8") as f:
            row = f"A1:{answer1}  A2:{answer2}  A3:{answer3} A4:{answer4} A5:{answer5}\n"
            f.write(row)
            print("AFTER")
        return HttpResponse("Спасибо за опрос!")
    return HttpResponse("Отправьте форму пожалуйста :)")