from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from pollapp.models import Poll, Variant
from pollapp.poll_collection import PollCollection

# Create your views here.
def index(request):
    polls = Poll.objects.all()
    return render(request, 'pollapp/index.html', {'polls': polls})


def poll_detail(request, poll_id):
    collection = PollCollection(request)
    print(collection.collection)
    if poll_id in collection.collection:
        show_buttons = False
    else:
        show_buttons = True
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'pollapp/poll_detail.html', {'poll': poll, 'show_buttons': show_buttons})

def addvote(request, variant_id):
    if request.method == 'POST':
        collection = PollCollection(request)
        total_votes = 0
        var = get_object_or_404(Variant, id=variant_id)
        poll = get_object_or_404(Poll, id=var.poll.id)
        var.votes = var.votes + 1
        var.save()
        for vot in var.poll.variants.all():
            total_votes += vot.votes
        poll.total_votes = total_votes
        poll.save()
        collection.add_to_collection(poll.id)
        url = reverse('poll_detail', args=(var.poll.id,))
        return redirect(url)