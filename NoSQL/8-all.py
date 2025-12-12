#!/usr/bin/env python3
"""
Module to list all documents in a MongoDB collection using PyMongo
"""


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection
    
    Args:
        mongo_collection (pymongo.collection.Collection):
            The PyMongo collection object from which to retrieve documents.
            
    Returns:
        list: A list of documents (dict) in the collection.
        returns an empty list if the collection has no documents.
    """
    new_collection = list(mongo_collection.find())
    return new_collection
