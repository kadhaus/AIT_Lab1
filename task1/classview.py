from django.views.generic import View,ListView
from django.shortcuts import render
from django.conf import settings

class NavView(View):
    def __init__(self,*args,**kwargs):
        self.base_context={
            'nav_id':self.nav_id,
        }
        super(NavView,self).__init__(**kwargs)

    def buildContext(self,dictionary):
        self.base_context.update(dictionary)

    def render(self,request):
        return render(request,self.template_name,context=self.base_context)