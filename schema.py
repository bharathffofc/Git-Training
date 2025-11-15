def serialise_one(doc)->dict:
    doc["_id"]=str(doc["_id"])
    return doc

def serialise_many(docs)->list:
    """function to serialise list of documents"""
    return [serialise_one(doc) for doc in docs]