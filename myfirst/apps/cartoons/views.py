from django.shortcuts import render
from cartoons.models import Cartoon
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


class EIndexView(View):
    template_name = 'cartoons/list.html'

    def get(self, request):
        context = {}
        # Забираем все опубликованные статье отсортировав их по дате публикации
        all_series = Cartoon.objects.filter(visible=True).order_by('-pub_date')
        # Создаём Paginator, в который передаём статьи и указываем,
        # что их будет 10 штук на одну страницу
        current_page = Paginator(all_series, 6)

        # Pagination в django_bootstrap3 посылает запрос вот в таком виде:
        # "GET /?page=2 HTTP/1.0" 200,
        # Поэтому нужно забрать page и попытаться передать его в Paginator,
        # для нахождения страницы
        page = request.GET.get('page')
        try:
            # Если существует, то выбираем эту страницу
            context['latest_cartoons_list'] = current_page.page(page)
        except PageNotAnInteger:
            # Если None, то выбираем первую страницу
            context['latest_cartoons_list'] = current_page.page(1)
        except EmptyPage:
            # Если вышли за последнюю страницу, то возвращаем последнюю
            context['latest_cartoons_list'] = current_page.page(current_page.num_pages)

        return render(request=request, template_name=self.template_name, context=context)

def detail(request, cartoon_id):
    try:
       a = Cartoon.objects.get( id = cartoon_id )
    except:
       raise Http404("Фильм не найден!")

    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'cartoons/detail.html', {'cartoon': a, 'latest_comments_list': latest_comments_list})

def leave_comment(request, cartoon_id):
    try:
       a = Cartoon.objects.get( id = cartoon_id )
    except:
       raise Http404("Фильм не найден!")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect( reverse('cartoons:detail', args = (a.id,)) )
