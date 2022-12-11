from django.shortcuts import render
from zk import ZK, const
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View




@login_required(login_url='login/')
def Home(request):
    return render(request, "home/index.html")

class Dashboard(LoginRequiredMixin,View):
    template_name = 'home/index.html'
    login_url ='/login/'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        numberofGust =int(request.POST.get('numberofGust', 0))
        for x in range(1,numberofGust+1):
            name=request.POST.get('text'+str(x), None)
            checked=  request.POST.get('check'+str(x), None)
            print(name,checked)
        return render(request, self.template_name,{'form': ""})




def index(request):
    conn = None
    zk = ZK('172.20.0.71', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
    # layer = get_channel_layer()
    try:
        conn = zk.connect()
        print("Connected")
        for attendance in conn.live_capture():
            if attendance is None:
                pass
            else:
                # async_to_sync(layer.group_send)('chat_test_channel', {"type": "chat_message", "message": attendance.name})
                print(dir(attendance))
                print ('+ UID #{}'.format(attendance.uid))
                print ('+ user_id #{}'.format(attendance.user_id))
    
    except Exception as e:
        print ("Process terminate : {}".format(e))
    finally:
        if conn:
            conn.disconnect()
    return HttpResponse("ALLAH IS ONE")

def test(request):
    return HttpResponse("ALLAH IS ONE")