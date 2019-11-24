from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from blog.models import BlogIndexPage



class HomePage(Page):
    body = RichTextField(blank=True)
    max_count = 1
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogindexpages = self.get_children().live()
        context['blogindexpages'] = blogindexpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
