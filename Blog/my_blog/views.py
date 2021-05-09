from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, \
									PageNotAnInteger
from django.views.generic import ListView
from .models import Post


def post_list(request):
	#posts = Post.objects.filter(status='published') duplicate
	object_list = Post.objects.filter(status='published')
	paginator = Paginator(object_list, 3) #3 posts in each page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		#if page isn not an intager deliver the first page
		posts = paginator.page(1)
	except EmptyPage:
		#if page is out of range deliver last page of results
		posts = paginator.page(paginator.num_pages)

	return render(request,
					'my_blog/post/list.html',
					{'page':page,
					'posts': posts})

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post,
									status='published',
									publish__year=year,
									publish__month=month,
									publish__day=day)
	return render(request,
					'my_blog/post/detail.html',
					{'post': post})

class PostListView(ListView):
	queryset = Post.objects.filter(status='published')
	context_object_name = 'posts'
	paginate_by = 3
	template_name = 'my_blog/post/list.html'

# Create your views here.
