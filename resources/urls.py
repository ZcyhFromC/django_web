'''resources应用的url'''

from django.urls import path

from . import views

app_name = 'resources'

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    
    # 节点相关
    path('nodes/<int:user_id>', views.nodes, name='nodes'),
    path('node/<int:node_id>', views.node, name='node'),
    path('new_node/', views.new_node, name='new_node'),
    
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
