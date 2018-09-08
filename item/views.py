#from django.shortcuts import render
# Create your views here.

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import \
    ListView, DeleteView, DetailView, UpdateView, CreateView

from .models import Item
from .forms import ItemForm

class ItemListView(ListView):
    model = Item
    paginate_by = 5

class ItemDetailView(DetailView):
    model = Item

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('item_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「｛｝」を作成しました'.format(form.instance))
        return result

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('item_list')

    def form_valid(self, form):
            result = super().form_valid(form)
            messages.success(
                self.request, '「{}」を更新しました'.format(form.instance))
            return result


class ItemDeleteView(DeleteView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('item_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object))
        return result