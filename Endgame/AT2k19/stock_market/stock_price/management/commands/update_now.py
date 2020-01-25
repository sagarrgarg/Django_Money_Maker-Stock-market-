from django.core.management.base import BaseCommand
from stock_price.models import Company


class Command(BaseCommand):
    help = 'Updates Database'

    def handle(self, *args, **kwargs):

        with open("C:/Users/Sagar R Garg/Documents/Stockmarket/new/Endgame2/values.txt") as f:
            data = []
            for i in f.readlines():
                a = i.split()

                if len(a)>3:
                    a[0] = a[0]+" "+a[1]
                    del a[1]

                # item = Company(name = a[0], current_price = float(a[1]), percentage_change = float(a[2]))
                # item.save()

                data+=[a]

            ct = 0
            data = [x for x in data if x != []]
            print(data)
            for i in Company.objects.all():
                item = i
                item.current_price = data[ct][1]
                item.percentage_change = data[ct][2]
                ct+=1
                item.save()
