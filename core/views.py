from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
import json




def index(request):

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not message:
            messages.error(request, "Please fill all fields.")
            return redirect(request.path + "#contact")

        email_body = f"""
        New message from portfolio:

        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        try:
            send_mail(
                subject="Portfolio Contact",
                message=email_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["yashawasthi854@gmail.com"],
                fail_silently=False,
            )
            messages.success(request, "Message sent ✔")
        except:
            messages.error(request, "Email failed. Check settings.")

        return redirect(request.path + "#contact")

    context = {
        "name": "Yash",
        "title_badge_html": '<img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="40px"/> Namaste',

        "about_paragraph": """An AI/ML-focused developer who likes building things that actually work.
I work across backend, frontend, and AI tools to create fast, usable, and clean applications.
My workflow is simple: build → break → fix → improve
.I’m currently leveling up my expertise in AI systems,  aiming for a solid career as an AI/ML Engineer who ships real products.""",

        "socials": {
            "linkedin": "https://www.linkedin.com/in/yash-awasthi-a7aa5b334/",
            "github": "https://github.com/Yashdotin",
            "leetcode": "https://leetcode.com/u/yashawasthi25",
            "email": "mailto:yashawasthi854@gmail.com",
        },

        "projects": [
            {
                "title":"Heart risk prediction using ML",
                "desc":"ML model to predict heart disease risk.",
                "link":"https://heartrisk-pred.onrender.com/",
                "cover":"/static/core/images/heart.jpeg"
            }
            {"title": "AI Voice Assistant (Chanakya)", "desc": "Python NLP assistant.",
             "link": "https://www.linkedin.com/posts/yash-awasthi-a7aa5b334_ai-voiceassistant-nvidia-activity-7319263848144801792-2OTd", "cover": "/static/core/images/1.jpg"},
            {"title": "Wanderlust", "desc": "Node.js + MongoDB Airbnb clone.",
             "link": "https://wanderlust-kwz3.onrender.com/listings", "cover": "/static/core/images/2.jpg"},
            {"title": "Arka", "desc": "AI Chatbot.",
             "link": "https://arka-oh4z.onrender.com/", "cover": "/static/core/images/3.jpg"},
            {"title": "MathSuite", "desc": "Math tools suite.",
             "link": "https://mathsuite.onrender.com/", "cover": "/static/core/images/4.jpg"},
            {"title": "Pocket Calculator", "desc": "Fast calculator.",
             "link": "https://pocketcalc-ce6p.onrender.com/", "cover": "/static/core/images/calc.jpg"},
            {"title": "QR Generator", "desc": "Instant QR tool.",
             "link": "https://qr-1fb6.onrender.com/", "cover": "/static/core/images/qr.jpg"},
        ],
    }

    return render(request, "core/index.html", context)


# ---------------- RESUME PAGE ----------------
def resume(request):
    context = {
        "name": "Yash"
    }
    return render(request, "core/resume.html",context)



@csrf_exempt
def chat_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)

    data = json.loads(request.body)
    msg = data.get("message", "").lower().strip()

    if not msg:
        return JsonResponse({"reply": "Say something 😄"})

    # ------------- PREDEFINED INTENTS ------------- #

    responses = {
       
        ("hi", "hello", "hey", "namaste", "yo"): 
            "Hey! I'm YashBot 👋 — how can I help you?",

        
        ("who are you", "about you", "who is yash", "tell me about yash"):
            "I'm YashBot 🤖 — a mini assistant built by Yash. He's an AI/ML developer passionate about coding and building cool projects.",

        
        ("skills", "tech stack", "what can yash do"):
            "Yash works with Python, Java, C, Django, Node.js, MongoDB, FastAPI, Bootstrap, EJS, CSS, HTML, ML basics and more.",

        
        ("projects", "show projects", "yash projects"):
            "Yash has built several projects:\n• AI Voice Assistant (Chanakya)\n• Wanderlust marketplace\n• Arka chatbot\n• MathSuite\n• QR tool & Pocket Calculator",

        
        ("resume", "cv", "download resume"):
            "You can check out Yash’s resume here: /resume/ 😊",

       
        ("contact", "email", "reach", "connect"):
            "You can contact Yash at: yashawasthi854@gmail.com ✉️",
    }

    
    for keywords, reply in responses.items():
        if any(k in msg for k in keywords):
            return JsonResponse({"reply": reply})

    # ------------- FALLBACK REPLY ------------- #
    return JsonResponse({
        "reply": "I'm not fully smart yet 😅, but feel free to ask about Yash, his projects, skills, or resume!"
    })
