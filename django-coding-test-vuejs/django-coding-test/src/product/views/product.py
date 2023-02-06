from django.core.paginator import Paginator
from django.views import generic

from product.models import Variant,Product

from django.core.paginator import Paginator
from django.shortcuts import render



class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

    
    def listing(request):
        product_list = Product.objects.all()
        paginator = Paginator(product_list, 3) # Show 3 products per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'list.html', {'page_obj': page_obj})
