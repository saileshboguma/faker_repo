import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fakerproject.settings')
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        list = ['Project Manager','Team Lead','Software Engineer','Database specialist','Devops Engineer','Senior software engineer']
        ftitle=fake.random_element(list)
        list1=['B.tech','M.tech','MCA','PHD']
        feligilibity=fake.random_element(list1)
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        #Below code is resposible to get or create date in databases
        hydjobs_record=Hydjob.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligilibity,address=faddress,email=femail,phonenumber=fphonenumber)
populate(20)
