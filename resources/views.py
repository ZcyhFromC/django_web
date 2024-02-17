from django.shortcuts import render, redirect

# ~ from django.contrib.auth.decorators import login_required
# ~ from django.contrib.auth.models import User

# ~ from .models import Topic, Resource, Comment
# ~ from .forms import TopicForm, ResourceForm, CommentForm, GroupOrResourceForm, GroupForm

def index(request):
    '''主页面'''
    return render(request, 'resources/index.html')

# ~ def topics(request):
    # ~ '''显示所有的主题'''
    # ~ topics = Topic.objects.order_by('date_added')
    # ~ context = {'topics': topics}
    # ~ return render(request, 'resources/topics.html', context)

# ~ def topic(request, topic_id):
    # ~ '''显示单个主题以及其所有的条目,相当于resources'''
    # ~ topic = Topic.objects.get(id=topic_id)
    # ~ resources = topic.Resource_set.order_by('date_added')
    # ~ context = {'topic': topic, 'resources': resources}
    # ~ return render(request, 'resources/topic.html', context)

# ~ @login_required
# ~ def edit_topic(request, topic_id):
    # ~ '''修改topic'''
    # ~ topic = Topic.objects.get(id=topic_id)
    # ~ if request.method != 'POST':
        # ~ form = TopicForm(instance=topic)
    # ~ else:
        # ~ form = TopicForm(instance=topic, data=request.POST)
        # ~ if form.is_valid():
            # ~ form.save()
            # ~ return redirect('resources:topic', topic_id=topic_id)
    # ~ context={'topic': topic, 'form': form}
    # ~ return render(request, 'resources/edit_topic.html', context)

# ~ @login_required
# ~ def new_topic(request):
    # ~ '''添加新主题'''
    # ~ if request.method != 'POST':
        # ~ form = TopicForm()
    # ~ else:
        # ~ form = TopicForm(data=request.POST)
        # ~ if form.is_valid():
            # ~ form.save()
            # ~ return redirect('resources:topics')
    # ~ context = {'form': form}
    # ~ return render(request, 'resources/new_topic.html', context)

# ~ @login_required
# ~ def delete_topic(request, topic_id):
    # ~ '''删除主题'''
    # ~ topic = Topic.objects.get(id=topic_id)
    # ~ context={'topic':topic}
    
    # ~ if request.method !="POST":
        # ~ return render(request, 'resources/delete_topic.html', context)
    # ~ else:
        # ~ topic.delete()
        # ~ return redirect('resources:topics')

# ~ def resource(request, ri_id):
    # ~ '''显示单个资源项以及其所有的条目'''
    # ~ resource = Resource.objects.get(id=ri_id)
    # ~ topic = resource.topic
    # ~ context = {'ri': resource}
    # ~ return render(request, 'resources/resource.html', context)

# ~ @login_required
# ~ def new_resource(request, topic_id):
    # ~ '''在特定主题中添加新资源项'''
    # ~ topic = Topic.objects.get(id=topic_id)
    
    # ~ if request.method == 'GET':
        # ~ form = GroupOrResourceForm()
    # ~ if request.method == 'POST':
        # ~ if not request.POST.get('only_for_jdugement') is None:
            # ~ if request.POST.get('is_group'):
                # ~ # 返回一个Resource的group类型的表单
                # ~ form = GroupForm(initial={'is_group': 'True'})
            # ~ else:
                # ~ # 返回一个Resource的resource类型的表单
                # ~ form = ResourceForm(initial={'is_group': 'False'})
        # ~ else:
            # ~ # 接收数据。
            # ~ form = ResourceForm(data=request.POST)
            # ~ if form.is_valid:
                # ~ ri = form.save(commit=False)
                # ~ ri.user = request.user
                # ~ ri.save()
                # ~ return redirect('resources:topic', topic_id=topic_id)

    # ~ context = {'topic': topic, 'form': form}
    # ~ return render(request, 'resources/new_resource.html', context)
        
    
    if request.method != 'POST':
        form = ResourceForm()
    else:
        form = ResourceForm(data=request.POST)
        if form.is_valid():
            new_ri = form.save(commit=False)
            new_ri.topic = topic
            new_ri.user = request.user
            new_ri.save()
            return redirect('resources:topic', topic_id=topic_id)
    # ~ context = {'topic': topic, 'form': form}
    # ~ return render(request, 'resources/new_resource.html', context)

# ~ @login_required
# ~ def edit_resource(request, ri_id):
    # ~ '''修改资源项'''
    # ~ ri = Resource.objects.get(id=ri_id)
    # ~ topic = ri.topic
    
    # ~ if request.method != "POST":
        # ~ form = ResourceForm(instance=ri)
    # ~ else:
        # ~ form = ResourceForm(instance=ri, data=request.POST)
        # ~ if form.is_valid():
            # ~ form.save()
            # ~ return redirect('resources:resource', ri_id=ri_id)
    
    # ~ context = {'ri':ri , 'topic':topic, 'form': form}
    # ~ return render(request, 'resources/edit_resource.html', context)

# ~ @login_required
# ~ def delete_resource(request, ri_id):
    # ~ '''删除资源项'''
    # ~ ri = Resource.objects.get(id=ri_id)
    # ~ topic = ri.topic
    # ~ context={'ri_id':ri_id}
    
    # ~ if request.method !="POST":
        # ~ return render(request, 'resources/delete_resource.html', context)
    # ~ else:
        # ~ ri.delete()
        # ~ return redirect('resources:topic', topic_id=topic.id)

# ~ @login_required
# ~ def new_comment(request, ri_id):
    # ~ '''新建评论'''
    # ~ ri = Resource.objects.get(id=ri_id)
    
    # ~ if request.method != "POST":
        # ~ form = CommentForm()
    # ~ else:
        # ~ form = CommentForm(data=request.POST)
        # ~ if form.is_valid:
            # ~ comment = form.save(commit=False)
            # ~ comment.user = request.user
            # ~ comment.resource = ri
            # ~ comment.save()
            # ~ return redirect('resources:resource', ri_id=ri_id)
            
    # ~ context = {'form':form, 'ri_id':ri_id}
    # ~ return render(request, 'resources/new_comment.html', context)

# ~ @login_required
# ~ def edit_comment(request, comment_id):
    # ~ '''修改一个评论'''
    # ~ comment = Comment.objects.get(id=comment_id)
    # ~ ri = comment.resource
    
    # ~ if request.method != "POST":
        # ~ form = CommentForm(instance=comment)
    # ~ else:
        # ~ form = CommentForm(instance=comment, data=request.POST)
        # ~ if form.is_valid():
            # ~ form.save()
            # ~ return redirect('resources:resource', ri_id=ri.id)
    # ~ context = {'comment': comment, 'form': form}
    # ~ return render(request, 'resources/edit_comment.html', context)

# ~ @login_required
# ~ def delete_comment(request, comment_id):
    # ~ '''删除一个评论'''
    # ~ comment = Comment.objects.get(id=comment_id)
    # ~ ri = comment.resource
    # ~ context = {'comment': comment}
    
    # ~ if request.method != 'POST':
        # ~ return render(request, 'resources/delete_comment.html', context)
    # ~ else:
        # ~ comment.delete()
        # ~ return redirect('resources:resource', ri_id=ri.id)
        
# ~ def groups(request, user_id):
    # ~ '''展示某个用户的所有groups'''
    # ~ if user_id == 0:
        # ~ groups = Group.objects.all()
        # ~ c_user = False
    # ~ else:
        # ~ c_user = User.objects.get(id=user_id)
        # ~ groups = c_user.group_set.all()
    # ~ context = {'groups':groups, 'c_user':c_user}# c:current,so to avoid name contradiction.
    # ~ return render(request, 'resources/groups.html', context)

# ~ def group(request, group_id):
    # ~ '''展示特定group的详细信息'''
    # ~ group = Group.objects.get(id=group_id)
    # ~ ris = group.ris.all()
    # ~ context = {'group': group, 'ris': ris}
    # ~ return render(request, 'resources/group.html', context)

# ~ @login_required
# ~ def new_group(request):
    # ~ '''新建一个组'''
    # ~ if request.method != 'POST':
        # ~ form = GroupForm()
    # ~ else:
        # ~ form = GroupForm(data=request.POST)
        # ~ group = form.save(commit=False)
        # ~ group.user = request.user
        # ~ group.save()
        # ~ return redirect('resources:index')
    # ~ context = {'form': form}
    # ~ return render(request, 'resources/new_group.html', context)

# ~ @login_required
# ~ def edit_group(request, group_id):
    # ~ '''修改一个资源组'''
    # ~ group = Group.objects.get(id=group_id)

    # ~ if request.method != 'POST':
        # ~ form = GroupForm(instance=group)
    # ~ else:
        # ~ form = GroupForm(instance=group, data=request.POST)
        # ~ if form.is_valid:
            # ~ form.save()
            # ~ return redirect('resources:group', group_id=group_id)
    
    # ~ context = {'group': group, 'form': form}
    # ~ return render(request, 'resources/edit_group.html', context)

# ~ @login_required
# ~ def delete_group(request, group_id):
    # ~ '''删除一个资源组'''
    # ~ group = Group.objects.get(id=group_id)
    # ~ context = {'group': group}
    
    # ~ if request.method != 'POST':
        # ~ return render(request, 'resources/delete_group.html', context)
    # ~ else:
        # ~ group.delete()
        # ~ return redirect('resources:groups', group_id=0)
