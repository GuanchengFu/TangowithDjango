from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length = 128,
		help_text = "Please enter the category name.")
	views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
	likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
	slug = forms.CharField(widget = forms.HiddenInput(), required = False)

	class Meta:
		model = Category
		#fields decide what fields that we want to include in the forms.
		#In this case, the form will only display the name field.
		#field is used to show all the values that will be returned from this form.
		#In this situation, the only value returned by the form is the name fiedl.
		fields = ('name',)


class PageForm(forms.ModelForm):

	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')
		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url

			return cleaned_data
	title = forms.CharField(max_length = 128,
		help_text = "Please enter the title of the page.")
	url = forms.URLField(max_length = 200,
		help_text = "Please enter the URL of the page.")
	views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)

	class Meta:
		model = Page

		exclude = ('category',)
