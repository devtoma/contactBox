
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
            <html><head>
                  
                    <style>
                        .name-surname {
                            float: left;
                            width: 250px;
                            
                            cursor: pointer;
                            font-size: 22px;
                            font-weight: bold;
                            font-variant: small-caps;
                            color: black;
                            text-decoration: none
                             /*optional*/
                            font-family:arial,sans-serif; /*input has OS specific font-family*/
                              background:none;
                             border:none; 
                             padding:0;
                             text-align: left;
                            
                        }
                        
                        .name-surname:active {
                             color:gray;
                             
                        }
                        
                        .name-surname:hover{
                              background-color: #eee;
                              color: #555;
                              height: 30px;
                              font-size: 23px;
                        }
                        
                        .buttons-div {
                            float: left;
                            height: 35px;
                            padding-left: 5px;
                        }
                        
                        .bottom-buttons {
                            margin-top: 50px;
                            
                        }
                        
                        .position-site {
                            margin-top: 100px;
                            margin-left: 200px;
                            font-size: 20px;
                            font-weight: bold;
                            font-variant: small-caps;
                            padding-top: 20px;
                            display: inline-block;
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
                </head><body>
              <form action="#" method="POST">
                <fieldset class="position-site"><legend>Kontakty</legend>
        """

        __html_end = """
                  <div class=bottom-buttons>
                    <button class="button" type="submit" name="event" value="add">
                      Dodaj kontakt</button>
                    <button class="button" type="submit" name="event" value="groups">
                      Grupy</button>
                  </div>
                </fieldset>
              </form>
            </body></html>
        """

        __html = ''
        if order == 0:
            contact_list = Person.objects.order_by('surname', 'name')
            for i in contact_list:
                __html = __html + f"""        
                    <button class="name-surname" name="cinfo" value="{i.id}">{i.name} {i.surname}</button>
                    <div class="buttons-div">
                        <button class="button" type="submit" name="edit" value="{i.id}">Edycja</button>
                        <button class="button" type="submit" name="delete" value="{i.id}">Usuń</button></div>
                    <div class="clearfix"></div>                  
                """
            return __html_start + __html + __html_end
        elif order == 1: pass
        elif order == 2: pass

    def get(self, request):
        return HttpResponse(ContactList.show_contact_list())


    def post(self, request):
        if self.request.POST.get('edit'):
            return HttpResponse("Edytuję...")
        elif self.request.POST.get('delete'):
            __delete = self.request.POST.get('delete')
            box = f"""
                <form action="" method="post">
                  <div style='margin-top: 100px; margin-left: 200px;'>
                     <h3 style='font-familly: arial, san-serif; font-size: 22px; font-variant: small-caps;'>Na pewno chcesz skasować?</h3>
                    <input type="hidden" id="deleteId" name="deleteId" value="{__delete}">
                    <input style='
                            display: inline-block;                      
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
                            user-select: none;' type="submit" name="confirmation" value="Potwierdź">
                    <button style='
                            display: inline-block;                      
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
                            user-select: none;' onclick="window.history.back();" type="button">Wróć</button>
                </form></body><html>
                </div>
            """
            return HttpResponse(box)
        elif self.request.POST.get('confirmation') == "Potwierdź":
            __delete = self.request.POST.get("deleteId")

            Person.objects.get(pk=__delete).delete()
            __after_delete = self.show_contact_list()
            return HttpResponse(__after_delete)
        elif self.request.POST.get('cinfo'):
            return HttpResponse('Info czeka na przekierowanie...')
        elif self.request.POST.get('event') == 'groups':
            return HttpResponse("Czekam na widok Grup")
        else:
            return HttpResponse("Czekam na Widok Dodawania Rekordu.")
