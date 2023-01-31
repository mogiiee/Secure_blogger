from . import db, responses


def inserter(post):
    if post == {""}:
        return responses.response(False, "length is wrong")
    else:
        db.collection.insert_one(post)
        return responses.response(True, post)
