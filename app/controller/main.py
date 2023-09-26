def get_all(model):
    all = model.query.all()
    return all


def get_one(model, id):
    one = model.query.get(id)
    return one
