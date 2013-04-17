from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=20)
	email = forms.EmailField(required=False, label='Your e-mail address')
	message = forms.CharField(widget=forms.Textarea)

	
	# Django form system automatically looks for any method whose name starts with 
	# clean_ and ends with the name of a field. If any such method exists, 
	# it is called during validation.
	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Not enough words!")
		return message

class CommodityForm(forms.Form):
	description = forms.CharField(max_length=255)
	price = forms.CharField(required=False)
	
	
	#name = forms.CharField(max_length=100)
	#unit = forms.ForeignKey(Unit)
	#balance = forms.IntegerField()
	#currency = forms.ForeignKey(Currency)
	#price = forms.DecimalField(max_digits=20, decimal_places=2)
	#stock_record_num = forms.CharField(max_length=6)
	#optimum_level = forms.DecimalField(max_digits=10)
	#created = forms.DateTimeField(auto_now=False)
	#updated = forms.DateTimeField(auto_now=True)