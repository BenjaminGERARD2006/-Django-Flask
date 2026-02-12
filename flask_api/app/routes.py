
from flask import Blueprint, request, jsonify
from .models import db, Story, Page, Choice
from flask import request, abort
from .config import API_KEY

def require_api_key():
    key = request.headers.get("X-API-KEY")
    if key != API_KEY:
        abort(401)

bp = Blueprint("api", __name__)

@bp.route("/stories")
def get_stories():
    status = request.args.get("status", "published")
    stories = Story.query.filter_by(status=status).all()
    return jsonify([{"id": s.id, "title": s.title, "description": s.description} for s in stories])

@bp.route("/stories/<int:id>")
def get_story(id):
    s = Story.query.get_or_404(id)
    return jsonify({"id": s.id, "title": s.title, "description": s.description, "start_page_id": s.start_page_id})

@bp.route("/stories/<int:id>/start")
def get_start(id):
    s = Story.query.get_or_404(id)
    return jsonify({"start_page_id": s.start_page_id})

@bp.route("/pages/<int:id>")
def get_page(id):
    page = Page.query.get_or_404(id)
    choices = Choice.query.filter_by(page_id=id).all()
    return jsonify({
        "id": page.id,
        "text": page.text,
        "is_ending": page.is_ending,
        "ending_label": page.ending_label,
        "choices": [{"id": c.id, "text": c.text, "next_page_id": c.next_page_id} for c in choices]
    })

@bp.route("/stories", methods=["POST"])
def create_story():
    data = request.json
    story = Story(title=data["title"], description=data.get("description", ""), status="published")
    db.session.add(story)
    db.session.commit()
    return jsonify({"id": story.id})

@bp.route("/stories/<int:id>", methods=["PUT"])
def update_story(id):
    s = Story.query.get_or_404(id)
    data = request.json

    if "title" in data:
        s.title = data["title"]

    if "description" in data:
        s.description = data["description"]

    if "start_page_id" in data:
        s.start_page_id = data["start_page_id"]

    db.session.commit()
    return jsonify({"status": "updated"})


@bp.route("/stories/<int:id>", methods=["DELETE"])
def delete_story(id):
    s = Story.query.get_or_404(id)
    db.session.delete(s)
    db.session.commit()
    return jsonify({"status": "deleted"})

@bp.route("/stories/<int:id>/pages", methods=["POST"])
def add_page(id):
    data = request.json
    page = Page(
        story_id=id,
        text=data["text"],
        is_ending=data.get("is_ending", False),
        ending_label=data.get("ending_label")
    )
    db.session.add(page)
    db.session.commit()
    return jsonify({"page_id": page.id})

@bp.route("/pages/<int:id>/choices", methods=["POST"])
def add_choice(id):
    data = request.json
    choice = Choice(page_id=id, text=data["text"], next_page_id=data["next_page_id"])
    db.session.add(choice)
    db.session.commit()
    return jsonify({"choice_id": choice.id})
