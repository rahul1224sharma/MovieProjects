from django import forms
from MovieApp.models import Movies

class MoviesForm(forms.ModelForm):
    # class Meta:
    #   model=Movies
    #  fields='__all__'

    #or

    releasedate = forms.DateField()
    moviename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    actor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    actress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # director_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ratings = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Movies
        fields = ('releasedate', 'moviename', 'actor', 'actress', 'ratings');

