from django.shortcuts import render
from .models import BotModel, BotManager, AdModel, SubmittedJobApplications

import random
# Create your views here.


def strToArray(string):
    if (string == '[]' or string == 'None' or string.strip() == ''):
        return []
    str_array = string
    str_array = str_array.replace('[', '')
    str_array = str_array.replace(']', '')
    str_array = str_array.strip()
    num_str_list = str_array.split(',')
    num_int_list = []
    for i in num_str_list:
        num_int_list.append(int(i))
    return num_int_list


def SaveNewBot(bot_name, botManager):
    newBot = BotModel(botName=bot_name,
                      botManagerName=botManager,  adsIds="[]")
    newBot.save()
    return


def SaveNewBotManager(name, bot_name):
    crrBot = BotModel.objects.filter(botName=bot_name)
    crrManager = BotManager.objects.filter(name=name)
    bot_id = crrBot[0].id
    if crrManager:
        mID = crrManager[0].id
        crrBotIds = strToArray(crrManager[0].botsIds)
        crrBotIds.append(bot_id)
        updatedBotIds = str(crrBotIds)
        newManager = BotManager(
            id=mID, name=name, subcriptionPlan=2, activeBots=1, botsIds=updatedBotIds)
        newManager.save()
    else:
        newManager = BotManager(
            name=name, subcriptionPlan=2, activeBots=1, botsIds=f'[{bot_id}]')
        newManager.save()
    return


def BotManagerHandler(request, name):

    crrManager = BotManager.objects.filter(name=name)
    all_bots = crrManager[0].botsIds
    subPlan = crrManager[0].subcriptionPlan
    crrUserBotsIds = strToArray(all_bots)
    crrUserBots = []
    activeAds = len(strToArray(crrManager[0].ManagerAdsIds))

    for botid in crrUserBotsIds:
        this_bot = BotModel.objects.filter(id=botid)
        crrUserBots.append(this_bot[0])

    if subPlan == 1:
        subPlan = 'One Time'
    elif subPlan == 2:
        subPlan = 'Monthly'
    elif subPlan == 3:
        subPlan = 'Anually'
    else:
        subPlan = 'An Error !'

    context = {
        'name': name,
        'subscription': subPlan,
        'bots': crrUserBots,
        'activeAds': activeAds
    }

    return render(request, 'botmanager.html', context)


def JobAdHandler(request, botmanager, adId):

    crrManager = BotManager.objects.filter(name=botmanager)
    crrManagerID = crrManager[0].id
    crrManagerName = crrManager[0].name
    context = {}
    crrAdId = None
    if request.method == "POST":
        if request.POST.get('submit') == 'Apply':
            contact = request.POST.get('email_or_phone')
            try:
                JA = SubmittedJobApplications(
                    job_id=adId,
                    job_title=request.POST.get('job_title'),
                    applicient_email_or_phone=contact,
                    job_manager=crrManagerName,
                )
                JA.save()
            except:
                return render(request, 'job_ad_success.html',
                              {'address': contact, 'msg': "you have already applied to this job"})
            return render(request, 'job_ad_success.html', {'address': contact})

        crrAd = AdModel.objects.filter(job_id=adId)

        if (crrAd):
            crrAdId = crrAd[0].id
            context = request.POST
            newAd = AdModel(
                job_id=adId,
                job_manager=crrManagerName,
                job_title=request.POST.get('job_title'),
                job_location=request.POST.get('job_location'),
                working_hours=request.POST.get('working_hours'),
                job_description=request.POST.get('job_description'),
                job_vacancy=request.POST.get('job_vacancy'),
                job_type=request.POST.get('job_type'),
                job_industry=request.POST.get('job_industry'),
                max_salary=request.POST.get('salaryMax'),
                min_salary=request.POST.get('salaryMin'),
                job_pay_rate_type=request.POST.get('job_pay_rate_type'),
                required_job_experince=request.POST.get(
                    'required_job_experince'),
                require_job_skill=request.POST.get('require_job_skill')
            )
            newAd.save()
        else:
            newAd = AdModel(
                id=crrAdId,
                job_id=adId,
                job_manager=crrManagerName,
                job_title=request.POST.get('job_title'),
                job_location=request.POST.get('job_location'),
                working_hours=request.POST.get('working_hours'),
                job_description=request.POST.get('job_description'),
                job_vacancy=request.POST.get('job_vacancy'),
                job_type=request.POST.get('job_type'),
                job_industry=request.POST.get('job_industry'),
                max_salary=request.POST.get('salaryMax'),
                min_salary=request.POST.get('salaryMin'),
                job_pay_rate_type=request.POST.get('job_pay_rate_type'),
                required_job_experince=request.POST.get(
                    'required_job_experince'),
                require_job_skill=request.POST.get('require_job_skill')
            )
            newAd.save()

        ads = crrManager[0].ManagerAdsIds
        print(ads)
        adsArray = strToArray(ads)
        if (adId in ads):
            print('This ad exist')
        else:
            adsArray.append(int(adId))
        print(adsArray)
        updateManager = BotManager(id=crrManagerID, name=crrManagerName,
                                   subcriptionPlan=crrManager[0].subcriptionPlan, botsIds=crrManager[0].botsIds,  ManagerAdsIds=str(adsArray))
        updateManager.save()

    context = {
        'job_id': '',
        'job_manager': crrManagerName,
        'job_title': '',
        'job_location': '',
        'working_hours': '',
        'job_description': '',
        'job_vacancy': '',
        'job_type': '',
        'job_industry': '',
        'max_salary': '',
        'min_salary': '',
        'job_pay_rate_type': '',
        'required_job_experince': '',
        'require_job_skill': ''
    }

    if adId == "new":
        adId = int(random.random()*100000)
        context['job_id'] = adId
        context['showSave'] = True
    else:
        print("Search Database for ad data")
        crrAd = AdModel.objects.filter(job_id=adId)
        context = {
            'job_id': crrAd[0].job_id,
            'job_manager': crrAd[0].job_manager,
            'job_title': crrAd[0].job_title,
            'job_location': crrAd[0].job_location,
            'working_hours': crrAd[0].working_hours,
            'job_description': crrAd[0].job_description,
            'job_vacancy': crrAd[0].job_vacancy,
            'job_type': crrAd[0].job_type,
            'job_industry': crrAd[0].job_industry,
            'max_salary': crrAd[0].max_salary,
            'min_salary': crrAd[0].min_salary,
            'job_pay_rate_type': crrAd[0].job_pay_rate_type,
            'required_job_experince': crrAd[0].required_job_experince,
            'require_job_skill': crrAd[0].require_job_skill,
            'showApply': True
        }

    return render(request, 'job_ad.html', context)
