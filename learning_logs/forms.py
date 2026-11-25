from django import forms
from .models import Topic , Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''} # The empty string in the labels dictionary 
                                #tells Django not to generate a label for the text field

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text' : ''}
        widgets = {'text' : forms.Textarea(attrs={'cols' : 80})}
        
        """ A widget is an HTML form element, such as a single-line text box, multiline text area, or drop
        down list. By including the widgets attribute, you can override Django default widget choices. 
        Here we are telling Django to use a forms.Textarea element with a width of 80 columns, 
        instead of the default 40 columns.
        """