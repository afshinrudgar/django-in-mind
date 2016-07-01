from django.db import models

# Custom Fields

class RateField(models.IntegerField):

  def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
    self.min_value, self.max_value = min_value, max_value
    models.IntegerField.__init__(self, verbose_name, name, **kwargs)

  def formfield(self, **kwargs):
      defaults = {'min_value': self.min_value, 'max_value':self.max_value}
      defaults.update(kwargs)
      return super(RateField, self).formfield(**defaults)


# Create your models here.
# simply all

class User(models.Model):
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=100)
  name = models.CharField(max_length=50)
  bio = models.CharField(max_length=200, null=True)

  def __str__(self):
    return '@' + self.username


class Place(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=20)
  location = models.CharField(max_length=50)
  city = models.CharField(max_length=30)
  uri = models.CharField(max_length=130, unique=True) # combination of city + name for show

  def __str__(self):
    return '%s-%s' %(self.city, self.name)

  def unique_uri(self):
    uri = '%s-%s' %(self.city, self.name)
    if not Place.objects.filter(uri=uri):
      return uri
    idx = 2
    while True:
      temp = uri + '-' + str(idx)
      if not Place.objects.filter(uri=temp):
        return temp
      idx += 1

  def save(self, *args, **kwargs):
    if not self.uri:
      self.uri = self.unique_uri()
    super(Place, self).save(*args, **kwargs)


class Review(models.Model):
  by = models.ForeignKey(User)
  about = models.ForeignKey(Place)
  text = models.CharField(max_length=1000)
  image = models.CharField(max_length=50, null=True)
  date = models.DateTimeField('date published', auto_now=True)
  rate = RateField(min_value=1, max_value=10)

  def __str__(self):
    return '%s: %s (%d)' %(self.by, self.about, self.rate)