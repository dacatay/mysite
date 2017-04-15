from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views.generic import ListView
from taggit.models import Tag

from .models import Post, Comment
from .forms import EmailPostForm, CommentForm


def post_list(request, tag_slug=None):
    """
    function based view for all blogposts as a list
    :return: rendered list.html with namespace page (paginator), post and tag
    """
    object_list = Post.objects.all().filter(status='published').order_by('-publish')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if Page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/list.html', {'page': page,
                                              'paginator': paginator,
                                              'posts': posts,
                                              'tag': tag})


class PostListView(ListView):
    """
    show a class-based view for all published blog entries ordered by publishing date
    """
    queryset = Post.objects.all().filter(status='published').order_by('-publish')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/list.html'


def post_detail(request, year, month, day, post):
    """"
    display a single blog post in detail
    """
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # list the active comments for a specific post
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            # modify object before saving > commit=False
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post,
                                                'comments': comments,
                                                'comment_form': comment_form})


def post_share(request, post_id):
    """
    share a post via email  
    """
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        # form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_url(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['comment'])
            send_mail(subject, message, 'daniel.acatay@googlemail.com', [cd['to']])
            sent = True
        else:
            form = EmailPostForm()
        return (render, 'blog/share.html', {'post': post,
                                            'form': form,
                                            'sent': sent})


