from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 128, unique = True)

	views = models.IntegerField(default = 0)

	likes = models.IntegerField(default = 0)
	
	slug = models.SlugField(unique = True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		#Call the save function defined in the models.Model
		super(Category, self).save(*args, **kwargs)

	class Meta:
		#All the data other than data field can be declared here.
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

class Page(models.Model):

	#all the models have a auto-increment integer field called id.

	category = models.ForeignKey(Category, on_delete = models.CASCADE)

	title = models.CharField(max_length = 128)

	url = models.URLField()

	views = models.IntegerField(default = 0)

	def __str__(self):
		return self.title