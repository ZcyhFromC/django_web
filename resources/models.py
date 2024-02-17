from django.db import models
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager

# ~ class Topic(models.Model):
    # ~ '''【用作索引】一系列资源的主题。做到不重不漏，方便资源组的建立。'''
    # ~ text = models.CharField(max_length=200)
    # ~ description = models.TextField(blank=True)
    # ~ date_added = models.DateTimeField(auto_now_add=True)
    
    # ~ def __str__(self):
        # ~ """返回模型的字符串表示"""
        # ~ return self.text

class ResourceNode(MPTTModel):
    '''
    资源节点。
    '''
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='children'
    )
    name = models.CharField(max_length=200)
    tags = TaggableManager(blank=True)
    text = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nodes')
    date_added = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True, null=True)
    
    class MPTTMeta:
        order_insertion_by = ['date_added']
    
    def __str__(self):
        if self.link != None:
            return f'·{self.name}·'
        else:
            return f'[{self.name}]'
   
class ResourceGroup(models.Model):
    name = models.CharField(max_length=200)
    tags = TaggableManager(blank=True)
    text = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    # 资源组
    nodes = models.ManyToManyField(ResourceNode, symmetrical=False)
    
    def __str__(self):
        return self.name
    
# ~ class Comment(models.Model):
    # ~ '''用户评论'''
    # ~ resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    # ~ user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ~ text = models.TextField()
    # ~ date_added = models.DateTimeField(auto_now_add=True)
    
    # ~ def __str__(self):
        # ~ return self.text
