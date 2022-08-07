
from django.db import models

# Create your models here.


class JobApplication (models.Model):

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
        (2, "1 years"),
        (3, "1 years"),
        (4, "1 years"),
        (5, "5+ years "),
        (10, "5+ years ")
    )

    job_title = models.CharField(max_length=100, default="job title")
    job_description = models.TextField()
    job_vacancy = models.IntegerField()
    job_location = models.CharField(max_length=100)
    working_days = models.IntegerField(
        choices=working_days_choice, default="Choose an option")
    working_hours = models.IntegerField(
        choices=working_hr_choice, default="Choose an option")
    job_type = models.CharField(
        max_length=50, choices=job_type, default="Choose an option")
    job_industry = models.CharField(
        max_length=50, choices=job_industry, default="Choose an option")
    salary_expectation = models.IntegerField()
    job_pay_rate_type = models.CharField(
        max_length=100, choices=pay_types, default="Choose an option")
    required_job_experince = models.IntegerField(
        choices=experince, default="Choose an option")
    require_job_skill = models.CharField(
        max_length=100, choices=job_skills, default="Choose an option")

    def __str__(self):
        return self.job_title
