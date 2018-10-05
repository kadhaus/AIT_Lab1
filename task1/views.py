from task1.classview import NavView
from task1 import callAPI
from task1.forms import EquationForm, GraphicsForm, InvertForm
import base64

class ViewWithText(NavView):
    template_name = "reverse.html"
    nav_id = 'reverse'

    def get(self, request):
        form = InvertForm()
        self.buildContext({
            'form': form,
        })
        return self.render(request)

    def post(self, request):
        form = InvertForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = form.cleaned_data.get('text')
            self.buildContext({
                'default_text':text,
                'reversed_text': callAPI.reverseText(text),
            })
        self.buildContext({'form': form})
        return self.render(request)


class ViewWithEquation(NavView):
    template_name = "equation.html"
    nav_id = "equation"

    def get(self, request):
        form = EquationForm(request.GET)
        self.buildContext({
            'form': form,
        })
        if form.is_valid():
            data = form.cleaned_data
            res = callAPI.equationSolve(data.get('coefA'), data.get('coefB'), data.get('coefC'))
            self.buildContext({
                'solution': res,
            })
        return self.render(request)


class ViewWithGraphics(NavView):
    template_name = "graphics.html"
    nav_id = "graphics"

    def get(self, request):
        functions = ['sin', 'cos', 'tan', 'tanh']
        form = GraphicsForm()
        self.buildContext({'functions': functions,
                           'form': form
                           })

        return self.render(request)


def drawGraphic(request):
    form = GraphicsForm(request.GET)
    if form.is_valid():
        function = form.cleaned_data.get('function')
        coefficient = form.cleaned_data.get('coefficient')
        xmin = form.cleaned_data.get('xmin')
        xmax = form.cleaned_data.get('xmax')
        ymin = form.cleaned_data.get('ymin')
        ymax = form.cleaned_data.get('ymax')
        response = callAPI.graphic(function, coefficient, xmin, xmax, ymin, ymax)
        return response
