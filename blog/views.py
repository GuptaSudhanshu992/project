from django.views import View
from django.shortcuts import render
from .models import BlogPost, BlogSection, Category
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.http import JsonResponse
from django.http import Http404

class BlogView(View):
    def get(self, request):
        categories = Category.objects.all()
        selected_category = request.GET.get('category_id', None)

        if selected_category and Category.objects.filter(id=selected_category).count()>0:
            live_posts = BlogPost.objects.filter(status_live=True, categories=selected_category).only('title', 'post_url', 'cover_image', 'cover_image_alt', 'categories' )
        else:
            live_posts = BlogPost.objects.filter(status_live=True).only('title', 'post_url', 'cover_image', 'cover_image_alt', 'categories' )

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            posts_data = [
                {
                    "title": post.title,
                    "post_url": post.post_url,
                    "image": post.cover_image.url if post.cover_image else "",
                    "alt": post.cover_image_alt,
                    "reading_time": post.reading_time,
                    "snippet": post.snippet,
                    "updated_at": post.updated_at,
                    "categories": [
                        {"id": cat.id, "name": cat.name} for cat in post.categories.all()
                    ],
                }
                for post in live_posts
            ]
            return JsonResponse({"live_posts": posts_data})

        return render(request, 'blog.html', {'live_posts': live_posts, 'categories': categories, 'selected_category': selected_category})

class BlogPostView(DetailView):
    model = BlogPost
    template_name = 'blogpost.html'
    context_object_name = 'post'

    def get_object(self):
        post_url = self.kwargs.get('post_url')
        post = get_object_or_404(BlogPost, post_url=post_url, status_live=True)
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sections'] = BlogSection.objects.filter(blog_post=self.object)
        return context
