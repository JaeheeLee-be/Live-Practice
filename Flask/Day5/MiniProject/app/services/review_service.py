from app.models import db, Review


def get_all_reviews():
    return Review.query.order_by(Review.created_at.desc()).all()


def get_average_rating():
    reviews = Review.query.all()
    if not reviews:
        return 0
    total = sum(r.rating for r in reviews)
    return round(total / len(reviews), 1)


def create_review(title, content, rating):
    review = Review(title=title, content=content, rating=rating)
    db.session.add(review)
    db.session.commit()
    return review


def get_review_by_id(review_id):
    return Review.query.get_or_404(review_id)


def update_review(review_id, title, content, rating):
    review = Review.query.get_or_404(review_id)
    review.title = title
    review.content = content
    review.rating = rating
    db.session.commit()
    return review


def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()