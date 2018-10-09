
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

        # method returns string with all contact records in specyfic order
        # 0 - sort by surname, 1 - sort by name, 2 - sort by creation date, 3 - most popular
        __html = ''
        if order == 0:
            contact_list = Person.objects.order_by('surname', 'name')

            for i in contact_list:
                __html = __html + f'<p>{i.name} {i.surname}' \
                                  f'<button class="red button" type="submit">Edycja</button>' \
                                  f'<button class="button" type="submit">Usuń</button></p>'
            return __html
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
