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
            __group = Group.objects.get(pk=group_view)  # wyciągam z bazy  listę wszystkie wpisy dla danej grupy (group_view 1-6)
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

    def set_contact_list_view(self, group=1, type_view=0):
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
        return HttpResponse(self.set_contact_list_view())

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
            __html += self.set_contact_list_view(i.id, 1)
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

    # metoda zmienia wybrany klucz QuerrySet w listę. Np. nazwy grup wyciąga ze słowników Seta
    # i tworzy listę z przypisanymi nazwami. patrz utworzenie listy groups w set_contact_info
    @staticmethod
    def convert_queryfield_to_list(querry, field):
        __field_list = []
        __result = [entry for entry in querry]
        [__field_list.append(i[field]) for i in __result]
        return __field_list

    # metoda zwróci tuplę z całe info z jednego wpisu w  addressBook
    def set_contact_info(self, id):
        self.__contact = Person.objects.get(pk=id)
        __contact_set = {}

        # tworzę stringa do grup, to do wersji pierwszej. potem wstawię multiselect boxa i nie będzie potrzebne

        user_groups = self.__contact.group_set.values()
        groups = self.convert_queryfield_to_list(user_groups, 'name')


        print(groups)
        if id != 0:  # set of data fo edit view


            __contact_set = {
                # atrybuty modelu Person:
                'name': self.__contact.name,
                'surname': self.__contact.surname,
                'description': self.__contact.description,
                # atrybuty modelu PhoneNumber (tupla):
                'phone': (self.__contact.phonenumber_set.values()[0]['number'],  # dane telefonu w jednej tupli
                          self.__contact.phonenumber_set.values()[0]['category']),
                # atrybuty modelu EmailAddress:
                'email': (self.__contact.emailaddress_set.values()[0]['address'],  # dane e-mail w jednej tupli
                          self.__contact.emailaddress_set.values()[0]['category']),
                # atrybuty modelu Address:
                'address': (self.__contact.address_set.values()[0]['street'],  # adres w jednej tupli
                            self.__contact.address_set.values()[0]['house_no'],
                            self.__contact.address_set.values()[0]['flat_no'],
                            "02-202", self.__contact.address_set.values()[0]['city']),
                            # dodałem kod pocztowy, nieobsługiwany w bazie
                'groups': groups,

                'taste': "EDIT"
                # potrzebuję tej zmiennej, by zarządzać widokami (dodawanie, edycja, wyświetlanie)
                # przy pomocy jednej html-ki. podzielony łańcuch na __html_start, __html__end
                # w set_contact_edit_view pozwoli mi zarządzać także buttonami w zależności od potrzeb
            }

        elif id == 2: # tryb info
            __contact_set['taste'] = 'INFO'  # poza buttonami 'zapisz', 'wróć' widok INFO będzie
            # taki sam jak widoku edit. inputy będą 'readonly'. imho będzie łatwiej i spójniej
            # ux-owo z innymi komponentami aplikacji

        return __contact_set

    def set_contact_edit_view(self, id, type_view=0):  # id - by wyciągnąć konkretny kontakt, type_view pozwoli dobrać zestaw w zalezności od widoku

        """
        najpierw tworzę listę pustych łańcuchów. dzięki nim rozpoznam stany kategorii e-mail oraz telefonu. jeden
        element podmienię na 'selected' - co sprawi że pojawi się kategoria ustalona przez użytkownika w obu menu. kategorii nie ustawiam dla widoku dodawania wpisu.
        """
        __if_selected = ['']*8  # 8 slotów
        __contact_info = self.set_contact_info(id)  # teraz pobieram całe info o kontakcie. trzymam je w dictionary

        __if_selected[int(__contact_info['phone'][1]) - 1] = "selected"
        # lista kategorii telefonu wyświetli się z wybranym widocznym - będzie na 1. miejscu. daję -1,
        # bo indeksy w html-ce startują od zera, a kategorie w bazie oznaczone są od 1-4

        __if_selected[int(__contact_info['email'][1]) + 3] = "selected"
        # dokładnie jak wyżej, ale dla e-mail.. łańcuchy z listy __if_selected trafią do html-ki poniżej.
        # to nie  daję -1, a +3, bo łańcuchy w html-ce mają indeksy 4,5,6,7 (w __if_selected),
        # a kategorie to indeksy (dokładnie tak jak w phone) 1, 2, 3, 4. dlatego trzeba dodać 3 i zająć
        # pozycje od 4 do 7

        groups_string = ', '.join(__contact_info['groups'])
        # tworzę tu stringa, którego na razie wrzucę w formularz Grupy

        input_style = '<input style="height: 33px;'
        label_style = '<label style="height: 33px; font-size: 22px; font-weight: bold; font-variant: small-caps;'
        # przygotowuję html od lekkiego ostylowania. w html-ce 'zaszyję' fragmenty stringa stylami inline
        # to tylko ostylowanie, nie wpłynie na działanie programu. podmieniam jedynie stringi

        # poniżej html-ka z różnymi {}. dzięki atrybutom z metody set_contact_info, podmieniam części łańcuchów, np.
        #  na 'selected' w rozwijalnych listach lub 'readonly' dla inputów w widoku INFO.
        __html_start = f"""
            <html><body><form style="margin-top: 100px; margin-left: 200px" action="/Edit/{id}" method="POST">
                <p><label {label_style}">
                  Imię:
                  {input_style} width: 130px" type="text" name="user_name" value="{__contact_info['name']}" >
                  Nazwisko:
                  {input_style} width: 250px" type="text" name="user_surname" value="{__contact_info['surname']}">
                </label></p>   
            
                <p><label {label_style}">
                  Opis:
                  {input_style} width: 487px" type="text" name="description" value="{__contact_info['description']}">   
                </label></p>          
                <p><label {label_style}">Telefon:
                  {input_style} width: 295px;" type="tel" name="phone_number" value="{__contact_info['phone'][0]}" 
                  pattern='(\+(\d{1})*\d{1})*\s*\d{2,3}\s*\d{2,3}\s*\d{2,3}\s*\d{2,3}'>
                </label>
                <select style='width: 150px; padding: 6px 20px; margin: 0; border: 1px solid #bbb;
                    overflow: visible; font: 13px arial, helvetica, sans-serif;
                    text-decoration: none; white-space: nowrap; color: #555;'>
                  <option value='private' name="phone_cat_1" {__if_selected[0]}>{CATEGORIES[0][1]}</option>
                  <option value='home' name="phone_cat_2" {__if_selected[1]}>{CATEGORIES[1][1]}</option>
                  <option value='work' name="ephone_cat_3" {__if_selected[2]}>{CATEGORIES[2][1]}</option>
                  <option value='secret' name="phone_cat_4" {__if_selected[3]}>{CATEGORIES[3][1]}</option>
                </select></p>         
                <p><label {label_style}">E-mail:
                  {input_style} width: 310px;" type="email" name="user_email" value="{__contact_info['email'][0]}">
                </label>
                <select style='width: 150px; padding: 6px 20px; margin: 0; border: 1px solid #bbb;
                    overflow: visible; font: 13px arial, helvetica, sans-serif;
                    text-decoration: none; white-space: nowrap; color: #555;'>
                  <option value="private" name="email_cat_1" {__if_selected[4]}>{CATEGORIES[0][1]}</option>
                  <option value="home" name="email_cat_2" {__if_selected[5]}>{CATEGORIES[1][1]}</option>
                  <option value="work" name="email_cat_3" {__if_selected[6]}>{CATEGORIES[2][1]}</option>
                  <option value="secret" name="email_cat_4" {__if_selected[7]}>{CATEGORIES[3][1]}</option>
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
              {input_style} width: 465px;" type="text" name="user_group" value="{groups_string}">
          </label> </p>       
        """
        __html_end = f"""<p>{ContactList.button_save}</p></form></body></html>
        """

        return __html_start + __html_group + __html_end  # przekazujemy gotowy html

    def get(self, request, id):

        return HttpResponse(self.set_contact_edit_view(id))

    def post(self, request):

        button = self.request.POST.get("action")

        if self.request.POST.get("action") == 1:
            return HttpResponse("Zapisuj goscia")
        else:

            return HttpResponse("Powrot")

# jak lepije zapisac numer tel + id ownera,


