from django.shortcuts import render
from django.views import generic
from store.models import Product, Category
from django_filters.views import FilterView
from store.filters import ProductFilter
from cart.forms import CartForm
from django.db.models import Count

'''
from store.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.

# Create your views here.

@login_required
#@login_required(login_url='login')
def delete_post(request, pk=None):
    if Post.objects.filter(pk=pk).exists:
        post=get_object_or_404(Post, pk=pk)
        post.delete()
    post = Post.objects.all().order_by("-date")
    paginator = Paginator(post, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return HttpResponseRedirect(reverse('blog'))
@login_required
#@login_required(login_url='login')
def post(request, pk):
    post=get_object_or_404(Post, pk=pk)
    id=post.auth_id
    uProfile=userProfile.objects.all()
    userprofile=userProfile.objects.get(user_id=id)
    form=CommentForm()
    if request.method=="POST":
        # form=CommentForm(request.POST,author=request.user, post=post)
        dateTime=datetime.now()
        comment= Comment()
        comment.date=dateTime.strftime(" Vào: %H:%M ngày: %d/%m/%Y ")
        comment.auth=request.user
        comment.body=request.POST["comment"]
        comment.post= post
        if comment is not None:
            comment.save()
            return HttpResponseRedirect(request.path)
    return render(request, "post.html", {"post":post, "form":form, 'userprofile':userprofile,"uProfile":uProfile})

@login_required
#@login_required(login_url='login')
def delete_comment(request, pk=None):
    comment=get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post', comment.post.id)

from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
'''
# Create your views here.



class ProductList(FilterView):
    model = Product
    queryset = Product.objects.all()
    paginate_by = 20
    filterset_class = ProductFilter
    context_object_name = 'products'
    template_name = 'store/product_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if 'category_slug' in self.kwargs:
            qs = qs.filter(category__slug=self.kwargs['category_slug'])
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProdcutDetails(generic.DetailView):
    model = Product
    template_name = 'store/product_details.html'
    context_object_name = 'product'

    def get_queryset(self):
        product = super().get_queryset()
        return product.select_related('category').annotate(
            total_purchases=Count('ordered')) #biến để đếm số lượng khách đã mua hàng (đếm hành động 'ordered')


class CategoriesList(generic.ListView):
    template_name = 'store/categories_list.html'
    context_object_name = 'categories'
    queryset = Category.objects.all().annotate(num_products=Count('products'))
'''
def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "store/post.html", {"post": post, "form": form})'''