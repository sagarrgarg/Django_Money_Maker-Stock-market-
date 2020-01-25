from django.shortcuts import render, redirect
from .models import Company
from users.models import Profile
from .forms import BuyForm, SellForm
from django.core.exceptions import ValidationError


#views.home
def home(request):
    context = {
    'details': Company.objects.all()  #Sending data so that the html template can use it.
    }
    #This particular file structure is required in django, although it may seem weird.
    return render(request,'stock_price/home.html',context)#go to stock_price/templates/stock_price/home.html.


def graph(request):
    context = {
    'detail' : Company.objects.all()
    }
    return render(request,'stock_price/graph.html',context)


def about(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    return render(request,'stock_price/about.html')



def buy(request):
    form = BuyForm(request.POST or None)

    if request.method == "POST":
        #form = BuyForm(request.POST)

        username = None
        if request.user.is_authenticated:
            username = request.user.username

        if form.is_valid():
            name = form.cleaned_data['name']
            amount = form.cleaned_data['amount']
            ct = 0

            for i in Company.objects.all():
                l = i
                if name ==l.name:
                    ct+=1
                    k = i
            b = Profile.objects.get(user__username=username)
            if ct==0:
                raise ValidationError('Invalid Name')

            elif k.current_price*amount > Profile.objects.get(user__username=username).money_possesed:
                raise ValidationError('Not enough money')



            else:
                if name == "StarkIndustries":
                    b.Tesla_stock += amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "WayneEnterprises":
                    b.TataMotors_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "DailyPlanet":
                    b.Nissan_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "BigBellyBurger":
                    b.JPMorgan_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "LexCorpIndustries":
                    b.SunPharma_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "ParkerIndustries":
                    b.GSKPfizer_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "QueenConsolidated":
                    b.Nestle_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "Oscorp":
                    b.BHEL_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "S.H.I.E.L.D":
                    b.Credit_stock +=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "RamonIndustries":
                    b.Heralded_stock += amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "XavierFunds":
                    b.Crystal_stock +=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "BannerChemicalIndustry":
                    b.Soteria_stock +=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "WakandaCorporation":
                    b.APInfovault_stock +=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "NonsenseCompany":
                    b.Bayer_stock +=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "StrangeCompany":
                    b.Exxon_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "MurdockFunds":
                    b.Uncash_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "CogitareSolutions":
                    b.Cogitare_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()



            return redirect('stockhome')


    return render(request,'stock_price/buy.html',{'form':form})


def sell(request):

    form = SellForm(request.POST or None)

    if request.method == "POST":

        username = None
        if request.user.is_authenticated:
            username = request.user.username

        if form.is_valid():
            name = form.cleaned_data['name']
            amount = form.cleaned_data['amount']
            ct = 0

            for i in Company.objects.all():
                l = i
                if name ==l.name:
                    ct+=1
                    k = i
            b = Profile.objects.get(user__username=username)

            if ct==0:
                raise ValidationError(('Invalid Name'))



            elif name == "StarkIndustries":
                if b.Tesla_stock< amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.Tesla_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()


            elif name == "WayneEnterprises":
                if b.TataMotors_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.TataMotors_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()


            elif name == "DailyPlanet":
                if b.Nissan_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.Nissan_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()



            elif name == "BigBellyBurger":
                if b.JPMorgan_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.JPMorgan_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()


            elif name == "LexCorpIndustries":
                if b.SunPharma_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.SunPharma_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "ParkerIndustries":
                if b.GSKPfizer_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.GSKPfizer_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "QueenConsolidated":
                if b.Nestle_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.Nestle_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "Oscorp":
                if b.BHEL_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.BHEL_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "S.H.I.E.L.D":
                if b.Credit_stock < amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.Credit_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "RamonIndustries":
                if b.Heralded_stock < amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.Heralded_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "XavierFunds":
                if b.Crystal_stock < amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.Crystal_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "BannerChemicalIndustry":
                if b.Soteria_stock < amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.Soteria_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "WakandaCorporation":
                if b.APInfovault_stock <amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.APInfovault_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "NonsenseCompany":
                if b.Bayer_stock <amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.Bayer_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "StrangeCompany":
                if b.Exxon_stock <amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.Exxon_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "MurdockFunds":
                if b.Uncash_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.Uncash_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()


            return redirect('stockhome')

    return render(request,'stock_price/sell.html',{'form':form})
