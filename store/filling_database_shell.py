from .models import Product
from PIL import Image
import os
import random


"""querry = Product.objects.filter(name__icontains="capri")
pk_list=[]
for x in querry:
    pk_list.append(x["pk"])
"""


class AutomatedDatabaseFilling:
    def __init__(self, name):
        self.pk_list = []

    def retriveing_previous_pk(self):
        querry = Product.objects.filter(name__icontains="capri",category__name="Women's Fashion").values("pk")
        for x in querry:
            self.pk_list.append(x["pk"])

    def updating_database(self):
        for i in self.pk_list:
            obj = Product.objects.get(pk=i)
            obj.image = "womens_fashion/women_suit.jfif"
            postfix = str(random.randrange(1, 50))
            obj.name = "Salwar Suit" + " - " + postfix
            obj.save()
        return True

