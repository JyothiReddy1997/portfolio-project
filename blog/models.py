from django.db import models

# Create a blog model
#title
#pu_date
#body
#image
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

#add blog app to settings

#create migration           cmd

#migrate                cmd

# add to admin
