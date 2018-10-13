from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from addressBook.models import Person, PhoneNumber, Address, EmailAddress, Group, CATEGORIES

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class ContactList(View):
    button_save = """
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
                            onmouseout="this.style.backgroundColor = '#ddd'; this.color = '#555';"
                             onclick="window.history.back();" 
                            type="button">Wróć</button>
                """
    def set_list_taste(self, group_view=1, type_view=0):
        __html = ""
        if type_view == 0:  #lista nazwisk z przyciskami z boku - edycja, usuń
            contact_list = Person.objects.order_by("surname", "name")  # wyciągam z bazy uporządkowaną listę
            for i in contact_list:
                __html += f"""
                    <button class="name-surname" name="cinfo" value="{i.id}">{i.name} {i.surname}</button>
                    <div class="buttons-div">
                        <button class="button" type="submit" name="edit" value="{i.id}">Edycja</button>
                        <button class="button" type="submit" name="delete" value="{i.id}">Usuń</button></div>
                    <div class="clearfix"></div>                  
                """
            __html = f"""<fieldset class="position-site"><legend>Kontakty</legend>{__html}           
                <div class=bottom-buttons>
                <button class="button" type="submit" name="event" value="add">
                    Dodaj kontakt</button>
                <button class="button" type="submit" name="event" value="groups">
                    Grupy</button>
                </div>"""
        elif type_view == 1:
            __group = Group.objects.get(pk=group_view)  # wyciągam z bazy  listę wszystkie wpisy dla danej grupy
            group_list = __group.member.all()  # tworzę listę osób przypisanych do grupy

            for i in group_list:
                __html += f"""      
                    <button class="name-surname" name="cinfo" value="{i.id}">{i.name} {i.surname}</button>
                    <div class="buttons-div">
                        <button class="button" type="submit" name="delete" value="{i.id}">Usuń z grupy</button></div>
                    <div class="clearfix"></div>                  
                """
            __html = f"""<fieldset class="position-site" ><legend>{Group.objects.get(pk=group_view).name}</legend>""" \
                     + __html
        return __html

    def set_contact_list(self, group=1, type_view=0):
        self.type_view = type_view
        self.group_view = group
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
                </fieldset></div>
              </form>
            </body></html>
        """
        __html = self.set_list_taste(self.group_view, self.type_view)
        return " ".join((__html_start, __html, __html_end))

    def get(self, request):
        return HttpResponse(self.set_contact_list())

    def post(self, request):
        __id = self.request.POST.get('edit')
        if self.request.POST.get('edit'):
            return HttpResponseRedirect('/Edit/' + __id + '/')
        elif self.request.POST.get('delete'):
            __delete = self.request.POST.get('delete')
            confirm_box = f"""       
                <html><body><form action="" method="post">
                  <div style='margin-top: 100px; margin-left: 200px;'>
                     <h3 style='font-familly: arial, san-serif; font-size: 22px; font-variant: small-caps;'>Na pewno chcesz skasować?</h3>
                    <input type="hidden" id="deleteId" name="deleteId" value="{__delete}">
                    {ContactList.button_save}
                  </div>
                </form></body><html>          
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
            return HttpResponse("wywaliło!")


@method_decorator(csrf_exempt, name='dispatch')
class ContactGroupsList(ContactList):

    def get(self, request):
        __html = ''
        __group_list = Group.objects.all().order_by('name')
        for i in __group_list:
            __html += self.set_contact_list(i.id, 1)
        return HttpResponse(__html)

    def post(self, request):
        return HttpResponse("Czekam na Widok")


@method_decorator(csrf_exempt, name='dispatch')
class EditContact(View):
    # made by @TomW
    # dodac placefolder wszystki, placholder zaminic w pola domyslne inputa 2) dodac selekty rozwjane emial i telefon 3) zapis do bazy przyciski
    # def __iter__(self):
    #     return iter((self.name, self.age, self.gender))

    # @staticmethod
    # def validate_records(item, type=0):
    #     if type == 0 and item:
    #        return item
    #     elif type == 0 and item :


    # metoda zwróci tuplę z całe info z jednego wpisu w  addressBook
    def set_contact_info(self, id):
        self.__contact = Person.objects.get(pk=id)
        __contact_set = {}
        if id != 0:
            member_list =  (item for item in self.__contact.group_set.values()[0])
            print(member_list)
            __contact_set = {
            # atrybuty modelu Person:
                'name': self.__contact.name,
                'surname': self.__contact.surname,
                'description': self.__contact.description,
             # atrybuty modelu PhoneNumber (tupla):
                'phone': (self.__contact.phonenumber_set.values()[0]['number'],
                         self.__contact.phonenumber_set.values()[0]['category']),
            # atrybuty modelu EmailAddress:
                'email': (self.__contact.emailaddress_set.values()[0]['address'],
                          self.__contact.emailaddress_set.values()[0]['category']),
            # atrybuty modelu Address:
               'address': (self.__contact.address_set.values()[0]['street'],
                           self.__contact.address_set.values()[0]['house_no'],
                           self.__contact.address_set.values()[0]['flat_no'],
                           self.__contact.address_set.values()[0]['city']),
                'groups': (self.__contact.group_set.values()[0]['name']),

                'taste': "EDIT"
            }
        elif id == 1:  # new record
            __contact_set = {
            # set na potrzeby okna dodawania wpisu do addressBook
                'name': "Wpisz imię",
                'surname': "Wpisz nazwisko",
                'description': "Podaj opis",
                # atrybuty modelu PhoneNumber (tupla):
                'phone': self.__contact.phonenumber_set.values()[0]['name'],
                # atrybuty modelu EmailAddress:
                'email': (self.__contact.emailaddress_set.values()[0]['address'],
                          self.__contact.emailaddress_set.values()[0]['category']),
                # atrybuty modelu Address:
                'address': (self.__contact.address_set.values()[0]['street'],
                            self.__contact.address_set.values()[0]['house_no'],
                            self.__contact.address_set.values()[0]['flat_no'],
                            self.__contact.address_set.values()[0]['city']),
                'taste': "NEW"
            }
        elif id == 2: # tryb info
            __contact_set['taste'] = 'INFO'
        return __contact_set

    def set_contact_edit(self, id):
        __if_selected = ''
        __contact_info = self.set_contact_info(id)  # pobieram całe info o kontakcie.
        # przygotowuję html od lekkiego ostylowania. w kodzie html 'zaszyję' fragmenty ze stylami inline
        input_style = '<input style="height: 33px;'
        label_style = '<label style="height: 33px; font-size: 22px; font-weight: bold; font-variant: small-caps;'

        __html_start = f"""
            <html><body><form style="margin-top: 100px; margin-left: 200px" action="/Edit/{id}" method="POST">
                <p><label {label_style}">
                  Imię:
                  {input_style} width: 130px" type="text" name="user_name" value="{__contact_info['name']}">
                  Nazwisko:
                  {input_style} width: 250px" type="text" name="user_surname" value="{__contact_info['surname']}">
                </label></p>   
            
                <p><label {label_style}">
                  Opis:
                  {input_style} width: 487px" type="text" name="description" value="{__contact_info['description']}">   
                </label></p>          
                <p><label {label_style}">Telefon:
                  {input_style} width: 295px;" type="tel" name="phone_number" value="{__contact_info['phone'][0]}" 
                  pattern="(\+(\d{1})*\d{1})*\s*\d{2,3}\s*\d{2,3}\s*\d{2,3}\s*\d{2,3}">
                </label>
                <select style='width: 150px; padding: 6px 20px; margin: 0; border: 1px solid #bbb;
                    overflow: visible; font: 13px arial, helvetica, sans-serif;
                    text-decoration: none; white-space: nowrap; color: #555;'>
                  <option value='private' {__if_selected}>{CATEGORIES[0][1]}</option>
                  <option value='home' {__if_selected}>{CATEGORIES[1][1]}</option>
                  <option value='work' {__if_selected}>{CATEGORIES[2][1]}</option>
                  <option value='secret' {__if_selected}>{CATEGORIES[3][1]}</option>
                </select></p>         
                <p><label {label_style}">E-mail:
                  {input_style} width: 310px;" type="email" name="user_email" value="{__contact_info['email'][0]}">
                </label>
                <select style='width: 150px; padding: 6px 20px; margin: 0; border: 1px solid #bbb;
                    overflow: visible; font: 13px arial, helvetica, sans-serif;
                    text-decoration: none; white-space: nowrap; color: #555;'>
                  <option value="private" {__if_selected}>{CATEGORIES[0][1]}</option>
                  <option value="home" {__if_selected}>{CATEGORIES[1][1]}</option>
                  <option value="work"{__if_selected}>{CATEGORIES[2][1]}</option>
                  <option value="secret" {__if_selected}>{CATEGORIES[3][1]}</option>
                </select></p>                
                <fieldset style="width: 510px;"><legend style="font-size: 22px; font-weight: bold; font-variant: small-caps;">Adres:</legend>
                     <p><label {label_style}">
                      Ulica:
                      {input_style} width: 267px" type="text" name="street" value="{__contact_info['address'][0]}">
                      Numer:
                      {input_style} width: 38px" type="text" name="house_no" value="{__contact_info['address'][1]}">
                      /
                      {input_style} width: 38px" type="text" name="flat_no" value="{__contact_info['address'][2]}">
                    </label></p>
                    <p><label {label_style}">Kod
                       {input_style} width: 82px;" type="text" name="zip" value="00-000"> 
                    Miasto:
                      {input_style} width: 292px;" type="text" name="city" value="{__contact_info['address'][3]}">     
                </fieldset>                        
         """

        __html_group = f"""
          <p><label {label_style}">
              Grupy:
              {input_style} width: 465px;" type="text" name="user_group" value=", ".join(me)>
          </label> </p>       
        """

        __html_end = f"""<p>{ContactList.button_save}</p></form></body></html>
        """


        return __html_start + __html_group + __html_end

    def get(self, request, id):
        #print(self.set_contact(id))
        return HttpResponse(self.set_contact_edit(id))

    def post(self, request):

        button = self.request.POST.get("action")

        if self.request.POST.get("action") == 1:
            return HttpResponse("Zapisuj goscia")
        else:

            return HttpResponse("Powrot")

# jak lepije zapisac numer tel + id ownera,
