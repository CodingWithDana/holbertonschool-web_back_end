#!/usr/bin/env python3
"""
Module to insert a new document in a collection based on kwargs
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The MongoDB collection object where the document will be inserted.
        **kwargs:
            Arbitrary keyword arguments representing the document's fields
            and values.

    Returns:
        ObjectId: The `_id` of the inserted document.
    """
    inserted = mongo_collection.insert_one(kwargs)
    return inserted.inserted_id
