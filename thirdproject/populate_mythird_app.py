import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'thirdproject.settings'

import django
django.setup()
import random
from thirdapp.models import Users
from faker import Faker

fakegen =Faker()


def populate(N=6):
    for enter in range(N):

        fake_name =fakegen.name().split()
        fname =fake_name[0]
        lname=fake_name[1]
        ename=fakegen.email()

        users =Users.objects.get_or_create(first_name=fname,last_name=lname, email =ename)


if __name__=="__main__":
    print("populating script")
    populate(20)
    print("populating completed!!!!")
