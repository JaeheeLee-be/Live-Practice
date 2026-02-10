from flask import Blueprint, render_template, request, redirect, url_for
from app.services import review_service


bp = Blueprint("review", __name__)


@bp.route("/")
def index():
    reviews = review_service.get_all_reviews()
    avg_rating = review_service.get_average_rating()
    
    return render_template(
        "index.html",
        reviews=reviews,
        avg_rating=avg_rating
    )


@bp.route("/new", methods=["GET", "POST"])
def new_review():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        rating = int(request.form["rating"])
        
        review_service.create_review(title, content, rating)
        return redirect(url_for("review.index"))
    
    return render_template("new.html")


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_review(id):
    review = review_service.get_review_by_id(id)
    
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        rating = int(request.form["rating"])
        
        review_service.update_review(id, title, content, rating)
        return redirect(url_for("review.index"))
    
    return render_template("edit.html", review=review)


@bp.route("/delete/<int:id>")
def delete_review_route(id):
    review_service.delete_review(id)
    return redirect(url_for("review.index"))