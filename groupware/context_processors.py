from functionlist.models import GroupwareFunction
from django.urls import reverse

def get_context(request):
    context = {}

    class Func():
        pass
    func_list = []
    q = GroupwareFunction.objects.all().order_by('order_priority')
    for i in q:
        f = Func()
        f.title = i.title
        f.path = reverse(i.path_index)
        func_list.append(f)
    context['functionlist'] = func_list
    return context
