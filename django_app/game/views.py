
import requests
from django.shortcuts import render, redirect
from .models import Play, Rating, Comment
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Avg
from django.shortcuts import redirect, get_object_or_404
from .models import Play, Rating, Comment, Report, AuthorStory
from .models import Comment
from django.shortcuts import redirect
from .models import Rating

def add_comment(request, story_id):
    if request.method == "POST":
        story = story_id
        text = request.POST.get("text")

        Comment.objects.create(
            story=story,
            user=request.user,
            text=text
        )

    return redirect("story_list")

def rate_story(request, story_id):
    if request.method == "POST":
        stars = request.POST.get("stars")

        if request.user.is_authenticated and stars:
            Rating.objects.create(
                user=request.user,
                story_id=story_id,
                stars=int(stars)
            )

    return redirect("story_list")

@staff_member_required
def admin_stats(request):
    total_plays = Play.objects.count()

    stats = Play.objects.values("story_id").annotate(count=models.Count("id"))

    return render(request, "game/admin_stats.html", {
        "total_plays": total_plays,
        "stats": stats
    })

def story_list(request):
    response = requests.get(f"{FLASK_API}/stories")
    stories = response.json()

    ratings = Rating.objects.values("story_id").annotate(avg=Avg("stars"))
    comments = Comment.objects.all()

    return render(request, "game/story_list.html", {
        "stories": stories,
        "ratings": ratings,
        "comments": comments
    })

def play_story(request, story_id):
    start = requests.get(f"{FLASK_API}/stories/{story_id}/start").json()

    page_id = start.get("start_page_id") or start.get("id")

    return redirect("page", page_id=page_id)

def page_view(request, page_id):
    page = requests.get(f"{FLASK_API}/pages/{page_id}").json()

    # Save play when reaching an ending
    if page.get("is_ending") and request.user.is_authenticated:
        Play.objects.create(
            story_id=page.get("story_id"),
            ending_page_id=page_id,
            user=request.user
        )

    return render(request, "game/page.html", {"page": page})

from collections import Counter


def stats_view(request):
    plays = Play.objects.all()

    # Plays per story
    story_counts = Counter(play.story_id for play in plays)

    # Ending distribution
    ending_counts = Counter(play.ending_page_id for play in plays)

    context = {
        "story_counts": dict(story_counts),
        "ending_counts": dict(ending_counts),
    }

    return render(request, "game/stats.html", context)

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})

from django.contrib.auth.decorators import login_required


@login_required
def author_dashboard(request):
    if not request.user.groups.filter(name="Author").exists():
        return redirect("story_list")

    return render(request, "game/author_dashboard.html")

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import requests
from .models import AuthorStory

FLASK_API = "http://127.0.0.1:5000"
API_KEY = "supersecret123"


@login_required
def create_story(request):

    # Only authors allowed
    if not request.user.groups.filter(name="Author").exists():
        return redirect("story_list")

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        # Send to Flask
        response = requests.post(
            f"{FLASK_API}/stories",
            json={
                "title": title,
                "description": description
            },
            headers={"X-API-KEY": API_KEY}
        )

        story = response.json()
        story_id = story["id"]

        # Save ownership in Django
        AuthorStory.objects.create(
            story_id=story_id,
            author=request.user
        )

        return redirect("author_dashboard")

    return render(request, "game/create_story.html")

@login_required
def my_stories(request):
    stories = AuthorStory.objects.filter(author=request.user)
    return render(request, "game/my_stories.html", {"stories": stories})

from django.contrib.auth.decorators import login_required
from .models import Play

@login_required
def my_history(request):
    plays = Play.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "game/history.html", {"plays": plays})

@staff_member_required
def suspend_story(request, story_id):
    requests.put(
        f"{FLASK_API}/stories/{story_id}",
        json={"status": "suspended"},
        headers={"X-API-KEY": "supersecret123"}
    )
    return redirect("story_list")

@login_required
def rate_story(request, story_id):
    stars = int(request.POST.get("stars"))

    Rating.objects.update_or_create(
        user=request.user,
        story_id=story_id,
        defaults={"stars": stars}
    )

    return redirect("story_list")

@login_required
def report_story(request, story_id):
    reason = request.POST.get("reason")

    Report.objects.create(
        user=request.user,
        story_id=story_id,
        reason=reason
    )

    return redirect("story_list")
