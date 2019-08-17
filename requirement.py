#1.What is printed from the middleware when a request hits the Django server?
Ans:'middleware.Testmiddleware3'


#2.Write the following code to generate an array of even squares in a single line of code using list comprehension.
a=[i**2 for i in range(100) if i%2==0]
print(a)


#3.HTTP response code for the following situations:
#If a request is sent on a URL which does not exist on the application.
5xx(500-599)
#If a request is sent on a URL to create an object on the application, and it is successfully created.
2xx(200-299)
#If a request is sent on a URL to get details of an object and the detail is sent successfully.
2xx(200-299)
#If a form is submitted with some invalid input.
4xx(400-499)

    
#4.Movie and actor database:
from django.db import models
class Actor(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    

class Movie(models.Model):
    actor=models.Foriegnkey(Actor,on_delete=models.CASCADE,related_name='movie_of_actor')
    released_date=models.DateField()
    budget=models.FloatField()
