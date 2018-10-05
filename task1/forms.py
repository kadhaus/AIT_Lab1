from django import forms


class EquationForm(forms.Form):
    coefA = forms.FloatField(label="A", max_value=10000, min_value=-10000)
    coefB = forms.FloatField(label="B", max_value=10000, min_value=-10000)
    coefC = forms.FloatField(label="C", max_value=10000, min_value=-10000)

    def __init__(self, *args, **kwargs):
        super(EquationForm, self).__init__(*args, **kwargs)


class InvertForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, max_length=20000)

    def __init__(self, *args, **kwargs):
        super(InvertForm, self).__init__(*args, **kwargs)


class GraphicsForm(forms.Form):
    function = forms.CharField(widget=forms.HiddenInput)
    coefficient = forms.FloatField(label="x*coefficient", max_value=1000, min_value=-1000, initial=1)
    xmin = forms.IntegerField(label="x min", max_value=1000, min_value=-1000, initial=-1)
    xmax = forms.IntegerField(label="x max", max_value=1000, min_value=-1000, initial=1)
    ymin = forms.IntegerField(label="y min", max_value=1000, min_value=-1000, initial=-1)
    ymax = forms.IntegerField(label="y max", max_value=1000, min_value=-1000, initial=1)

    def __init__(self, *args, **kwargs):
        super(GraphicsForm, self).__init__(*args, **kwargs)
