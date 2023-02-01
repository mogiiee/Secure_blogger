from . import db, responses


def inserter(post):
    db.collection.insert_one(post)
    return responses.response(True, post)
