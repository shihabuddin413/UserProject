from django.db import models


# Create your models here


class AdModel (models.Model):
    pay_types = (
        ('Freelancing', 'Freelancing'),
        ('Contactual', 'Contactual'),
        ('Monthly', 'Monthly'),
        ('Weekly', 'Weekly'),
        ('Yearly', 'Yearly'),
    )

    job_type = (
        ('Freelancing', 'Freelancing'),
        ('Contactual', 'Contactual'),
        ('empolyee', 'As an regular empolyee'),
        ('Other', 'Others')
    )

    working_days_choice = ((1, '1'), (2, '2'), (3, '3'),
                           (4, '4'), (5, '5'), (6, '6'))

    working_hr_choice = ((1, '1'), (2, '2'), (3, '3'),
                         (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'))

    job_skills = (
        ('get_ui_designer', 'Ui designer'),
        ('developer', ' Developer'),
        ('site_engineer', 'site engineer')
    )

    job_industry = (
        ("IT", "IT"),
        ("Automobile", "Automobile"),
        ("Corporate", "Corporate"),
        ("Bank", "Bank"),
    )

    experince = (
        (1, "1 years"),
        (2, "2 years"),
        (3, "3 years"),
        (4, "4 years"),
        (5, "5+ years "),
        (10, "10+ years ")
    )

    job_id = models.IntegerField(default=None)
    job_manager = models.CharField(max_length=200, default="None")
    job_title = models.CharField(max_length=100, default="job title")
    job_location = models.CharField(max_length=200)
    working_hours = models.IntegerField(
        choices=working_hr_choice, default="Choose an option")
    job_description = models.TextField()
    job_vacancy = models.IntegerField()
    job_type = models.CharField(
        max_length=50, choices=job_type, default="Choose an option")
    job_industry = models.CharField(
        max_length=50, choices=job_industry, default="Choose an option")
    max_salary = models.IntegerField()
    min_salary = models.IntegerField()
    job_pay_rate_type = models.CharField(
        max_length=100, choices=pay_types, default="Choose an option")
    required_job_experince = models.IntegerField(
        choices=experince, default="Choose an option")
    require_job_skill = models.CharField(
        max_length=100, choices=job_skills, default="Choose an option")

    def __str__(self):
        return self.job_title


class BotModel(models.Model):
    botName = models.CharField(max_length=200)
    botManagerName = models.CharField(max_length=200, default='Unknwon')
    adsIds = models.CharField(max_length=10000)

    def __str__(self):
        return self.botName


class BotManager (models.Model):
    name = models.CharField(max_length=200)
    subcriptionPlan = models.IntegerField()
    botsIds = models.CharField(max_length=10000)
    ManagerAdsIds = models.CharField(max_length=10000)

    def __str__(self):
        return self.name


class SubmittedJobApplications (models.Model):
    job_id = models.IntegerField(default=None)
    job_title = models.CharField(max_length=200)
    applicient_email_or_phone = models.CharField(max_length=100, unique=True)
    job_manager = models.CharField(max_length=200, default="none")

    def __str__(self):
        return self.job_title + '(' + self.applicient_email_or_phone + ')'
