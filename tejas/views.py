from django.shortcuts import render
from django.views import generic
from .models import Post,ResearchPaper,Author,Project
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

def resume(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request,'resume.html')

def hobbies(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request,'hobbies.html')

def project_index(request):
    project = Project.objects.all()
    context = {"project": project}
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)

class HomeView(TemplateView):
    """View function for home page of site."""
    template_name = 'home.html'
#urlpatterns = [ url('^about/', views.AboutView.as_view(), name='about'),

def index(request):
    """View function for index page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request,'index.html')


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'

# Create your views here.
def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


class ResearchPaperListView(generic.ListView):
    model = ResearchPaper
    template_name = 'researchpaper_list.html'

class ResearchPaperDetailView(generic.DetailView):
    model = ResearchPaper
    def researchpaper_detail_view(request, primary_key):
        try:
            researchpaper = ResearchPaper.objects.get(pk=primary_key)
        except ResearchPaper.DoesNotExist:
            raise Http404('ResearchPaper does not exist')
        return render(request, 'researchpaper_detail.html', context={'researchpaper': researchpaper})

    def researchpaper_detail_view(request, primary_key):
        researchpaper = get_object_or_404(ResearchPaper, pk=primary_key)
        return render(request, 'researchpaper_detail.html', context={'researchpaper': researchpaper})

from .forms import ContactForm

# new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get( 'contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['saikumarsangeetha@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('tejas:contact')
    return render(request, 'contact.html', {'form': form_class,})
#
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            try:
                send_mail(contact_name, content, contact_email, ['saikumarsangeetha@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('tejas:success')
    return render(request,'email.html', {'form': form})

def successView(request):
    #return HttpResponse('Success! Thank you for your message.')
    return render(request,'success.html')
#% syntax python %}
# views.py
import logging
logger = logging.getLogger(__name__)

def myfunction():
	logger.debug("this is a debug message!")

def myotherfunction():
	logger.error("this is an error message!!")
#{% endsyntax %}
