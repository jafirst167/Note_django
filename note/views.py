from django.shortcuts import render, redirect
from django.contrib import messages

# import Note form and models

from .forms import NoteForm
from .models import Note

def index(request):

	item_list = Note.objects.order_by("-date")
	if request.method == "POST":
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('note')
	form = NoteForm()

	page = {
		"forms": form,
		"list": item_list,
		"title": "NOTE LIST",
	}
	return render(request, 'note/index.html', page)


def remove(request, item_id):
	item = Note.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('note')