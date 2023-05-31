from django.forms import ModelForm, CharField, TextInput, DateField, DateInput, ModelChoiceField, Select, ModelMultipleChoiceField, SelectMultiple
from .models import Quote, Author, Tag

class QuoteForm(ModelForm):
    quote = CharField(min_length=5, required=True, widget=TextInput())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all(), required=True, widget=SelectMultiple())
    author = ModelChoiceField(queryset=Author.objects.all(), required=True, widget=Select())
    
    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput())
    date_born = DateField(input_formats=['%B %d, %Y'],required=True, widget=DateInput(format='%B %d, %Y'),
                          error_messages={'invalid': 'Please enter a valid date in the format "Month DD, YYYY".'})
    location_born = CharField(max_length=150, widget=TextInput())
    bio = CharField(widget=TextInput())
    
    class Meta:
        model = Author
        fields = ['fullname', 'date_born', 'location_born', 'bio']


class TagForm(ModelForm):
    name = CharField(max_length=30, widget=TextInput())
  
    class Meta:
        model = Tag
        fields = ['name']



  