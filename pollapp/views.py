from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from pollapp.forms import PollForm, CreatePollFormset
from pollapp.models import Poll, Variant
from pollapp.poll_collection import PollCollection

# Create your views here.
def index(request):
    polls = Poll.objects.all()
    paginator = Paginator(polls, 15)
    try:
        curr_page = request.GET.get('page', 1)
        polls = paginator.page(curr_page)
    except:
        polls = paginator.page(1)
    return render(request, 'pollapp/index.html', {'polls': polls})


def poll_detail(request, poll_id):
    collection = PollCollection(request)
    if poll_id in collection.collection:
        show_buttons = False
    else:
        show_buttons = True
    poll = get_object_or_404(Poll, id=poll_id)
    sorted_variants = poll.variants.order_by('-votes')
    return render(request, 'pollapp/poll_detail.html', {'poll': poll, 'show_buttons': show_buttons, 'sorted_variants': sorted_variants})

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
    
def create_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        formset = CreatePollFormset(request.POST)
        if form.is_valid and formset.is_valid():
            new_poll = form.save()
            new_variants = formset.save(commit=False)
            for el in new_variants:
                el.poll = new_poll
                el.save()
            url = reverse('poll_detail', args=[new_poll.id,])
            return redirect(url)

    form = PollForm()
    formset = CreatePollFormset()
    return render(request, 'pollapp/createpoll.html', {'form': form, 'formset': formset})