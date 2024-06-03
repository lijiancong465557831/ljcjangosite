from django.shortcuts import render
from sign.models import Event
def events(request):
    events_list=Event.objects.all()
    return render(request, 'events.html',{'events_list':events_list})
# Create your views here.
# def sql_excute():
#     Event.objects.create(name="性能发布会",address="上海",limits=150)
#     event_dict={"name":"性能发布会","address":"上海","limits":150}
#     Event.objects.create(**event_dict)
#     event_list=Event.objects.all()
#     return event_list
def event_detail(request,event_id):
    event_obj=Event.objects.filter(id=event_id[0])
    return render(request,'event_detail.html',{"event":event_obj})
if __name__ == '__main__':
    print(sql_excute())