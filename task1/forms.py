from django import forms

class EquationForm(forms.Form):
    coefA = forms.FloatField(label="A", initial=0)
    coefB = forms.FloatField(label="B", initial=0)
    coefC = forms.FloatField(label="C", initial=0)

    def __init__(self,*args,**kwargs):
        super(EquationForm, self).__init__(*args,**kwargs)

class GraphicsForm(forms.Form):
    function = forms.CharField(widget=forms.HiddenInput)
    coefficient = forms.FloatField(label="x*coefficient", widget=forms.TextInput)
    xmin = forms.IntegerField(label="x min")
    xmax = forms.IntegerField(label="x max")
    ymin = forms.IntegerField(label="y min")
    ymax = forms.IntegerField(label="y max")

    def __init__(self,*args,**kwargs):
        super(GraphicsForm, self).__init__(*args,**kwargs)