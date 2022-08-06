from django.shortcuts import render
from .models import SingleUser


def SaveUser(name, age=0, carrerIndustry='Not Defined'):
    crr_user = SingleUser(name=name, age=age, carrerIndustry=carrerIndustry)
    crr_user.save()
    return True


def UserHandler(request, name):
    print(name)
    name = name
    age = ''
    carrerIndustry = ''

    if request.method == "POST":
        context = {"Save": "Save Data Successfull"}
        name = name
        age = request.POST.get('age')
        carrerIndustry = request.POST.get('carrerIndustry')
        allUser = SingleUser.objects.all()
        if len(allUser) == 0:
            SaveUser(name, age, carrerIndustry)
            return render(request, 'edituser.html', context)
        else:
            # update user
            crr_user = SingleUser.objects.filter(name=name)
            crr_id = crr_user[0].id
            if crr_user:
                data = SingleUser(id=crr_id, name=name, age=age,
                                  carrerIndustry=carrerIndustry)
                data.save()
            else:
                SaveUser(name, age, carrerIndustry)

            context = {
                'name': name,
                'age': age,
                'carrerIndustry': carrerIndustry
            }

            print(crr_user, crr_id)
            return render(request, 'edituser.html', context)

    allUser = SingleUser.objects.all()
    crr_user = SingleUser.objects.filter(name=name)

    # print(crr_user[0].id)

    context = {
        'name': name,
        'age': crr_user[0].age,
        'carrerIndustry': crr_user[0].carrerIndustry
    }

    return render(request, 'edituser.html', context)
