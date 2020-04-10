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
    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:100]

    #def pub_date_pretty(self):              #IF U DONT WANT exact time
    #    return self.pub_date.strftime('%b %e $Y')
