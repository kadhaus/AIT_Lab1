import math
from django.http import HttpResponse
import matplotlib
matplotlib.use('Agg')
import pylab

import io

def func(x, typef, coefficient):
    if typef == "sin":
        return math.sin(x*coefficient)
    if typef == "cos":
        return math.cos(x*coefficient)
    if typef == "tan":
        return math.tan(x*coefficient)
    if typef == "tanh":
        return math.tanh(x*coefficient)


def graphic(function, coefficient, xmin, xmax, ymin, ymax):
    dx = 0.01
    xlist = matplotlib.mlab.frange(xmin, xmax, dx)
    ylist = [func(x, function, coefficient) for x in xlist]
    pylab.plot(xlist, ylist)
    pylab.ylim(ymin, ymax)
    buf = io.BytesIO()
    pylab.axhline(0, color='black')
    pylab.axvline(0, color='black')
    pylab.grid(True)
    pylab.savefig(buf, format='png')
    pylab.close()
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response

def reverseText(text):
    res = text[::-1]
    return res


def equationSolve(a,b,c):
    if a == 0:
        if b == 0 and c == 0:
            res = ["Любое значение х является решением"]
        elif c != 0 and b == 0:
            res = ['Решений нет']
        else:
            res = [-c/b]
    else:
        discr = b*b - 4 * a * c
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            res = ['x1: ' + str(x1), 'x2: ' + str(x2)]
        elif discr == 0:
            x = -b / (2 * a)
            res = ['x: ' + str(x)]
        else:
            res = ["Действительных корней нет"]
    return res


