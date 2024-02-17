from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import ResourceNode, ResourceGroup
from .forms import ResourceNodeForm

def index(request):
    '''主页面'''
    if request.user.is_authenticated:
        user_id = request.user.id
    else:
        user_id = 1# 临时处理一下，如果没登陆，默认去zcyh的nodes页面
    context = {'user_id': user_id}
    return render(request, 'resources/index.html', context)

def nodes(request, user_id):
    '''展示某人创造出的节点'''
    user = User.objects.get(id=user_id)
    nodes = user.nodes.all()
    
    context = {'user': user, 'nodes': nodes}
    return render(request, 'resources/nodes.html', context)
    # 这个界面应该有更灵活以及更强大的功能。
    # 依照各种条件或者条件的组合。依据标签找node、依据···找node···

def node(request, node_id):
    '''展示某个节点'''
    node = ResourceNode.objects.get(id=node_id)
    parent = node.parent
    children = node.children.all()
    
    context = {'node': node, 'parent': parent, 'children': children}
    return render(request, 'resources/node.html', context)

def new_node(request):
    # 能不能将这个添加的过程可视化？？
    if request.method != 'POST':
        form = ResourceNodeForm()
    else:
        form = ResourceNodeForm(data=request.POST)
        if form.is_valid:
            node = form.save(commit=False)
            node.user = request.user
            node.save()# 表单modelform尚未了解清楚。
            return redirect('resources:nodes', user_id=1)# 临时处理一下，统一去zcyh的nodes页面
            # 实际上应该跳转到你刚刚来的地址。
    context = {'form': form}
    return render(request, 'resources/new_node.html', context)
    
        
