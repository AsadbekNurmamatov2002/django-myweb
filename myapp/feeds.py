import markdown
from django.utils.feedgenerator import Atom1Feed
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post

class LatestPostsFeed(Feed):
   title = 'Yangiliklar'
   link = reverse_lazy('myapp:home')
   description = 'Yangiliklar site'
   def items(self):
      return Post.objects.all().order_by("-id")[:50]
   def item_title(self, item):
      return item.title
   def item_description(self, item):
      return truncatewords_html(markdown.markdown(item.body), 30)
   def item_pubdate(self, item):
      return item.publish
   
class MyFeed(Feed):
     feed_type = Atom1Feed