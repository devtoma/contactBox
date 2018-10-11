
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

    def set_list_taste(self, type=0):

        __html = ""
        contact_list = Person.objects.order_by("surname", "name")  # wyciągam z bazy uporządkowaną listę

        if type == 0:  #lista nazwisk z przyciskami z boku - edycja, usuń
            for i in contact_list:
                __html += f"""
                    <button class="name-surname" name="cinfo" value="{i.id}">{i.name} {i.surname}</button>
                    <div class="buttons-div">
                        <button class="button" type="submit" name="edit" value="{i.id}">Edycja</button>
                        <button class="button" type="submit" name="delete" value="{i.id}">Usuń</button></div>
                    <div class="clearfix"></div>                  
                """
            __html = """<fieldset class="position-site"><legend>Kontakty</legend>""" + __html
        elif type == 1:
            #contact_list = Person.objects.filter(group__member="").order_by('surname', 'name')
            for i in contact_list:
                __html += f"""      
                    <button class="name-surname" name="cinfo" value="{i.id}">{i.name} {i.surname}</button>
                    <div class="buttons-div">
                        <button class="button" type="submit" name="delete" value="{i.id}">Usuń z grupy</button></div>
                    <div class="clearfix"></div>                  
                """
            __html = f"""<fieldset class="position-site" ><legend>{i}</legend>""" + __html
        return __html



    def set_contact_list(self, order=0):
        self.order = order
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
                        
                        .button:hover {
                           
                           color: #ddd;
                           background-color: #555;
                        }
                        
                        .button {
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
              <form action="#" method="POST"><div style="float: left;">       
        """
        __html_end = """
                  <div class=bottom-buttons>
                    <button class="button" type="submit" name="event" value="add">
                      Dodaj kontakt</button>
                    <button class="button" type="submit" name="event" value="groups">
                      Grupy</button>
                  </div>
                </fieldset></div>
              </form>
            </body></html>
        """
        __html = self.set_list_taste(self.order)
        return " ".join((__html_start, __html, __html_end))

    def get(self, request):
        return HttpResponse(self.set_contact_list())


    def post(self, request):
        if self.request.POST.get('edit'):
            return HttpResponse("Edytuję...")
        elif self.request.POST.get('delete'):
            __delete = self.request.POST.get('delete')
            confirm_box = f"""
                
                <form action="" method="post">
                  <div style='margin-top: 100px; margin-left: 200px;'>
                     <h3 style='font-familly: arial, san-serif; font-size: 22px; font-variant: small-caps;'>Na pewno chcesz skasować?</h3>
                    <input type="hidden" id="deleteId" name="deleteId" value="{__delete}">
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
                            user-select: none;' onmouseover="this.style.backgroundColor = '#555'"; 
                            onmouseout="this.style.backgroundColor = '#ddd';" type="submit" name="confirmation" 
                            value="yes">Potwierdź</button>                    
                    
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
                            user-select: none;' onmouseover="this.style.backgroundColor = '#555'"; 
                            onmouseout="this.style.backgroundColor = '#ddd'; this.color = '#555';" onclick="window.history.back();" 
                            type="button">Wróć</button>
 
                </form></body><html>
                </div>
            """
            return HttpResponse(confirm_box)
        elif self.request.POST.get('confirmation') == "yes":
            __delete = self.request.POST.get("deleteId")
            Person.objects.get(pk=__delete).delete()
            return HttpResponse(self.show_contact_list())
        elif self.request.POST.get('cinfo'):
            return HttpResponse('Info czeka na przekierowanie...')
        elif self.request.POST.get('event') == 'groups':
            return HttpResponseRedirect('/Group')
        else:
            return HttpResponse("/edit")


@method_decorator(csrf_exempt, name='dispatch')
class ContactGroupsList(ContactList):

    def get(self, request):
        __html = ''
        for i in range(6):
            __html += self.set_contact_list(1)
        return HttpResponse(__html)

    def post(self, request):
        return HttpResponse("Czekam na Widok")


@method_decorator(csrf_exempt, name='dispatch')
class EditContact(View):
    # made by @TomW
    # dodac placefolder wszystki, placholder zaminic w pola domyslne inputa 2) dodac selekty rozwjane emial i telefon 3) zapis do bazy przyciski
    @staticmethod
    def show_contact_edit(id):
        placeholder = Person.objects.get(pk=id)  # pobieram obiek z tabeli Preson o konkretnym id(cały rzad)

        # print(placeholder.phonenumber_set.get(owner_id=id).number)
        # print(placeholder.address_set.get())

        # w __html dostajemy się do konkretnych komorek okreslonej tabeli

        __html_start = f"""<html><body><form action="#" method="POST">

              <label>
                  Imie:
                  <input type="text" name="user_name" value="{placeholder.name}">
              </label>
              <br>
              <label>
                  Nazwisko:
                  <input type="text" name="user_surname" value="{placeholder.surname}">
              </label>
              <fieldset>
                      <legend>Adres:</legend>
                      <label>
                          Ulica:
                          <input type="text" name="user_address" value="{placeholder.address_set.get(resident__id=id).street}">
                      </label>
                      <label>
                          Nr domu:
                          <input type="text" name="user_house_num" value="{placeholder.address_set.get(resident_id=id).house_number}">
                      </label>
                      <label>
                          Nr mieszkania:
                          <input type="text" name="user_flat_name" value="{placeholder.address_set.get(resident_id=id).flat_number}">
                      </label>
                      <br>
                      <label>
                          Miasto:
                          <input type="text" name="user_city" value="{placeholder.address_set.get(resident_id=id).city}">
                      </label>
              </fieldset>    
              <label>
                  Email:
                  <input type="email" name="user_email" value="{placeholder.emailaddress_set.get(owner_id=id).address}">
              </label>
              <br>
              <label>
                  Nr telefonu:
                  <input type="text" name="user_phone_number" value="{placeholder.phonenumber_set.get(owner_id=id).number}">
                  <select>
                      <option value=""></option>
                      <option value=""></option>
                      <option value="">VW</option>
                      <option value="" selected>Audi</option>
                 </select>
              </label>
               """

        names = ""
        member_list = placeholder.group_set.all()  # wszystkie nazwy grup przypisanych do persony(u mnie presony)

        print(member_list.values()[0]['name'])
        for i in member_list:
            if names == "":
                names += i.name
                print(names)
            else:
                names += f", {i.name}"

        __html_group = f"""

                  <label>
                      Grupa:
                      <input type="text" name="user_group" value="{names}">

                  </label>

                  """
        __html_end = """

                 <div> 
                  <input type="submit" name="action" value="1">
                  <input type="submit" name="action" value="2">
                 </div> 
              </form></body></html>
        """

        return __html_start + __html_group + __html_end

    def get(self, request, id):

        result = self.show_contact_edit(id)
        # print(placeholder.name)

        return HttpResponse(result)

    def post(self, request, id):

        button = self.request.POST.get("action")

        if self.request.POST.get("action") == 1:
            return HttpResponse("Zapisuj goscia")
        else:

            return HttpResponse("Powrot")

# jak lepije zapisac numer tel + id ownera,
