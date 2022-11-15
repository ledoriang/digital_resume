from django.shortcuts import render
from django.contrib import messages
from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate
)

from django.views import generic
from .forms import ContactForm

class IndexView(generic.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolios = Portfolio.objects.filter(is_active=True)

        context['blogs'] = blogs
        context['portfolios'] = portfolios
        context['testimonials'] = testimonials
        context['certificates'] = certificates
        return context

class ContactView(generic.FormView):
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url= "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your message has been sent successfully. We will be in touch soon.')
        return super().form_valid(form)

    def get_success_url(self):
        return '/'

class PortfolioView(generic.ListView):
    template_name = 'main/portfolio.html'
    model = Portfolio
    paginate_by: int = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset

class PortfolioDetailView(generic.DetailView):
    template_name = 'main/portfolio_detail.html'
    model = Portfolio

class BlogView(generic.ListView):
    template_name = 'main/blog.html'
    model = Blog
    paginate_by: int = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset

class BlogDetailView(generic.DetailView):
    template_name = 'main/blog_detail.html'
    model = Blog