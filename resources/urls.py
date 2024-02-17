'''resources应用的url'''

from django.urls import path

from . import views

app_name = 'resources'

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    
    
    # ~ # 特定topic的详细页面
    # ~ path('topic/<int:topic_id>', views.topic, name='topic'),# 开始更改
    # ~ # 所有topic
    # ~ path('topics', views.topics, name='topics'),
    # ~ # 新建一个topic
    # ~ path('new_topic/', views.new_topic, name='new_topic'),
    # ~ # 删除一个topic
    # ~ path('delete_topic/<int:topic_id>', views.delete_topic, name='delete_topic'),
    # ~ # 修改一个topic
    # ~ path('edit_topic/<int:topic_id>', views.edit_topic, name='edit_topic'),
    
    
    # ~ # 特定ri的详细信息
    # ~ path('resource/<int:ri_id>', views.resource, name='resource'),
    # ~ # 新建一个ri
    # ~ path('new_resource/<int:topic_id>/', views.new_resource, name='new_resource'),
    # ~ # 修改一个ri
    # ~ path('edit_resource/<int:ri_id>', views.edit_resource, name='edit_resource'),
    # ~ # 删除一个ri
    # ~ path('delete_resource/<int:ri_id>', views.delete_resource, name='delete_resource'),
    
    
    
    # ~ # 新建一个comment
    # ~ path('new_comment/<int:ri_id>', views.new_comment, name='new_comment'),
    # ~ # 修改一个comment
    # ~ path('edit_comment/<int:comment_id>', views.edit_comment, name='edit_comment'),
    # ~ # 删除一个comment
    # ~ path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
    
    
    # ~ # 展示某个用户创建的所有group。若id为零，那么展示所有。
    # ~ path('groups/<int:user_id>', views.groups, name='groups'),
    # ~ # 展示某一个group的详细信息。
    # ~ path('group/<int:group_id>', views.group, name='group'),
    # ~ # new group。
    # ~ path('new_group/', views.new_group, name='new_group'),
    # ~ # 编辑一个group。
    # ~ path('edit_group/<int:group_id>', views.edit_group, name='edit_group'),
    # ~ # 删除一个group。
    # ~ path('delete_group/<int:group_id>', views.delete_group, name='delete_group'),
]
