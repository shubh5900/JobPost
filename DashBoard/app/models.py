from django.db import models

# Create your models here.
class Manager(models.Model):
    Name=models.CharField(max_length=40)
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.Name} {self.Email}"


class JobList(models.Model):
    JobTitle=models.CharField(max_length=20)
    city=models.CharField(max_length=13)
    country=models.CharField(max_length=15)
    details=models.TextField(max_length=1500)
    LastDate=models.DateField()

    def __str__(self):
        return f"{self.JobTitle} {self.LastDate}"


class Candidates(models.Model):
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        )
    FirstName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)
    Gender = models.CharField(max_length = 1,choices = GENDER_CHOICES,)
    BOD=models.DateField()
    Email=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=20)
    Skill=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.Email} {self.Mobile} {self.Skill}"


class ApplyCondidate(models.Model):
    jobId=models.CharField(max_length=20)
    CandidatesEmail=models.CharField(max_length=100)
    CandidatesMobile=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.jobId} {self.CandidatesEmail} {self.CandidatesMobile}"



    

