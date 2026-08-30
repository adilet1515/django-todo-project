from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from .models import TodoItem
from .forms import TodoForm
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, "todo/index.html")


class CreateTodoItemView(LoginRequiredMixin,CreateView ):
    raise_exception = True
    model = TodoItem
    form_class = TodoForm
    permission_denied_message = "You cannot create todo items!"

    template_name = "todo/create_form.html"

    success_url = reverse_lazy("todo:list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ViewTodoItems(LoginRequiredMixin,ListView):
    model = TodoItem
    raise_exception = True

    def get_queryset(self):
        return TodoItem.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TodoForm()
        return context

    def post(self,request, *args, **kwargs):
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect("todo:list")

        return render(request,
                  "todo/todoitem_list.html",
                      {
                          "object_list": self.get_queryset(),
                          "form": form,
                      })



class TodoItemDetailView(DetailView):
    def get_queryset(self):
        return TodoItem.objects.filter(author=self.request.user)

    raise_exception = True
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.author == request.user:
            raise PermissionDenied("You cannot change state!")
        self.object.done = "done" in request.POST
        self.object.save()
        return redirect("todo:detail", pk=self.object.pk)


class TodoItemDeleteView(DeleteView):
    model = TodoItem
    success_url = reverse_lazy("todo:list")

    def get_queryset(self):
        return TodoItem.objects.filter(author=self.request.user)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.author != request.user:
            raise PermissionDenied("You cannot delete this todo item!")

        return super().dispatch(request, *args, **kwargs)






