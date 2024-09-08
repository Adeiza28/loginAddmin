from django.db import models

# Create your models here.
# To make our project dynamic using simple class 
# class Feature:
#     id : int
#     name : str
#     details : str
#     is_true : bool

# To make our project dynamic using simple class to link it with database 
class Feature(models.Model): 
    # it will have id my default so we dont need to include id and we dont need to inclusse the datatype again
    Name = models.CharField(max_length=100)
    Details = models.CharField(max_length=500)
    
# before we can send our data to db we need register our app to project settind
