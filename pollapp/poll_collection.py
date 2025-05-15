class PollCollection:
    def __init__(self, request):
        self.request = request
        collection = request.session.get('collection')
        if collection:
            self.collection = collection
        else:
            request.session['collection'] = []
            self.collection = request.session.get('collection')

    def add_to_collection(self, poll_id):
        self.collection.append(poll_id)
        self.save()

    def save(self):
        self.request.session.modified = True