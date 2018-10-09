
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from addressBook.models import Person, PhoneNumber, Address, EmailAddress, Group

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class ContactList(View):

    @staticmethod
    def show_contact_list(order=0):
        __html_start = """
            <html>
                <head>
                  
                    <style>
                        .name-surname {
                            float: left;
                            width: 250px;
                            height: 40px;
                            
                            font-size: 22px;
                            font-weight: bold;
                            font-variant: small-caps;
                        }
                        
                        .buttons-div {
                            float: left;
                        }
                        
                        .bottom-buttons {
                            margin-top: 50px;
                            
                        }
                        
                        .position-site {
                            margin-top: 100px;
                            margin-left: 200px;
                           
                        }
                        .clearfix {
                            clear: both;
                        }
                        
                       
                        
                        .button{
                            display: inline-block;
                            *display: inline;
                            zoom: 1;
                            padding: 6px 20px;
                            margin: 0;
                            cursor: pointer;
                            border: 1px solid #bbb;
                            overflow: visible;
                            font: bold 13px arial, helvetica, sans-serif;
                            text-decoration: none;
                            white-space: nowrap;
                            color: #555;
                            
                            background-color: #ddd;
                            background-image: -webkit-gradient(linear, left top, left bottom, from(rgba(255,255,255,1)), to(rgba(255,255,255,0)));
                            background-image: -webkit-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
                            background-image: -moz-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
                            background-image: -ms-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
                            background-image: -o-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
                            background-image: linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
                            
                            -webkit-transition: background-color .2s ease-out;
                            -moz-transition: background-color .2s ease-out;
                            -ms-transition: background-color .2s ease-out;
                            -o-transition: background-color .2s ease-out;
                            transition: background-color .2s ease-out;
                            background-clip: padding-box; /* Fix bleeding */
                            -moz-border-radius: 3px;
                            -webkit-border-radius: 3px;
                            border-radius: 3px;
                            -moz-box-shadow: 0 1px 0 rgba(0, 0, 0, .3), 0 2px 2px -1px rgba(0, 0, 0, .5), 0 1px 0 rgba(255, 255, 255, .3) inset;
                            -webkit-box-shadow: 0 1px 0 rgba(0, 0, 0, .3), 0 2px 2px -1px rgba(0, 0, 0, .5), 0 1px 0 rgba(255, 255, 255, .3) inset;
                            box-shadow: 0 1px 0 rgba(0, 0, 0, .3), 0 2px 2px -1px rgba(0, 0, 0, .5), 0 1px 0 rgba(255, 255, 255, .3) inset;
                            text-shadow: 0 1px 0 rgba(255,255,255, .9);
                            
                            -webkit-touch-callout: none;
                            -webkit-user-select: none;
                            -khtml-user-select: none;
                            -moz-user-select: none;
                            -ms-user-select: none;
                            user-select: none;
}
                    
                    </style>
                </head><body><div class="position-site">
        """

        __html_end = """

            <div class=bottom-buttons>
                <button class="button" type="submit">Dodaj kontakt</button>
            </div>
        </div></body></html>
        
        """

        __html = ''
        if order == 0:
            contact_list = Person.objects.order_by('surname', 'name')
            for i in contact_list:
                __html = __html + f"""
                    
                    <div class="name-surname">{i.name} {i.surname}</div>
                    <div class="buttons-div">
                        <button class="button" type="submit">Edycja</button>
                        <button class="button" type="submit">Usuń</button></div>
                    <div class="clearfix"></div>                  
                """
            return __html_start + __html + __html_end
        elif order == 1: pass
        elif order == 2: pass

    def get(self, request):

        self.result = ContactList.show_contact_list()

        return HttpResponse(self.result)


    def post(self, request):
        # <other view logic>
        # self.key = request.POST.get('key')
        # self.value = request.POST.get('value')
        # request.session[self.key] = self.value
        return HttpResponseRedirect("nic takiego łosiu")
