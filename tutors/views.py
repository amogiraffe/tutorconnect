from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import TutorProfile
from django.db.models import Q
from django.core.paginator import Paginator


class TutorListView(ListView):
    model = TutorProfile
    template_name = 'tutors/list.html'
    context_object_name = 'tutors'
    paginate_by = 6  # 6 tutors per page


    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        subject_filter = self.request.GET.get('subject')
        
        if search_query:
            queryset = queryset.filter(
                Q(user__first_name__icontains=search_query) |
                Q(user__last_name__icontains=search_query) |
                Q(subjects__icontains=search_query)
            )
        
        if subject_filter:
            queryset = queryset.filter(subjects__icontains=subject_filter)
            
        return queryset.order_by('-user__date_joined')

class TutorDetailView(DetailView):
    model = TutorProfile
    template_name = 'tutors/detail.html'

