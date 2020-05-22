from django.shortcuts import render
from itertools import chain
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from cartoons.models import Cartoon
from films.models import Film
from series.models import Serie
from premiers.models import Premier

class ESearchView(View):
    template_name = 'search/search.html'


    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question:
            query_sets = []  # Общий QuerySet

            # Ищем по всем моделям
            query_sets.append(Cartoon.objects.filter(Q(title__istartswith=question) | Q(title__icontains=question)))
            query_sets.append(Film.objects.filter(Q(title__istartswith=question) | Q(title__icontains=question)))
            query_sets.append(Serie.objects.filter(Q(title__istartswith=question) | Q(title__icontains=question)))
            query_sets.append(Premier.objects.filter(Q(title__istartswith=question) | Q(title__icontains=question)))

            # и объединяем выдачу
            final_set = list(chain(*query_sets))
            final_set.sort(key=lambda x: x.pub_date, reverse=True)  # Выполняем сортировку

            context['last_question'] = '?q=%s' % query_sets

            current_page = Paginator(final_set, 10)

            page = request.GET.get('page')
            try:
                context['search_list'] = current_page.page(page)
            except PageNotAnInteger:
                context['search_list'] = current_page.page(1)
            except EmptyPage:
                context['search_list'] = current_page.page(current_page.num_pages)

        return render(request=request, template_name=self.template_name, context=context)