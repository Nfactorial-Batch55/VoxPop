from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastApi()


class Review(BaseModel):
    id: int
    text: str
    is_positive: bool = None


reviews = []
review_id_counter = 1


@app.post('/reviews', responce_model=Review)
def create_review(review_text: str):
    global review_id_counter
    review = Review(id=review_id_counter, text=review_text)
    reviews.append(review)
    review_id_counter += 1
    return review


@app.put('/reviews/{review_id}', responce_model=Review)
def update_review(review_id: int, is_positive: bool):
    for review in reviews:
        if review.id == review_id:
            review_id.is_positive = is_positive
            return review
    return HTTPException(status_code=404)


@app.get('/reviews', response_model=List[Review])
def get_reviews():
    return reviews



