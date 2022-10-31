import matplotlib.pyplot as plt
import numpy
import numpy as np


def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]


def InterpolanteLagrange(X, Y, x, ImprimirProcedimiento="No", ImprimirEvaluados="No", grafica="No", rango=0):
    if rango == 0:
        rango = [min(X), max(X)]
    n = len(X)
    cosoFeo = "\\[L(x)=\\sum_{j=0}^{" + str(
        n) + "}y_jl_j(x)=\\]\n \\[l_j(x)=\\prod_{i=0,i\\not=j}\\frac{x-x_j}{x_j-x_i}\\]\n"
    L = []
    F = []
    for i in range(len(X)):
        denominador = 1
        X1 = []
        F = []
        fraciones = "\\[y_{" + str(i) + "}l_{" + str(i) + "}(x)=" + str(Y[i]) + "\\cdot"
        numerador = ""
        #
        for j in range(len(X)):
            F.append(0)
            if i != j:
                if X[j] < 0:
                    numerador = numerador + "(x+" + str(-X[j]) + ")"
                    fraciones = fraciones + "\\frac{x+" + str(-X[j]) + "}{" + str(X[i]) + "+" + str(-X[j]) + "}"
                else:
                    numerador = numerador + "(x-" + str(X[j]) + ")"
                    fraciones = fraciones + "\\frac{x-" + str(X[j]) + "}{" + str(X[i]) + "-" + str(X[j]) + "}"
                if j == (n - 1):
                    fraciones = fraciones + "="
                else:
                    if i == (n - 1):
                        if j == (n - 2):
                            fraciones = fraciones + "="
                        else:
                            fraciones = fraciones + "\\cdot"
                    else:
                        fraciones = fraciones + "\\cdot"
                denominador = denominador * (X[i] - X[j])
                X1.append(-X[j])
        if Y[i] == 0:
            cosoFeo = cosoFeo + fraciones + "0\\]\n"
        else:
            cosoFeo = cosoFeo + fraciones + numerador + "\\cdot(" + str(Y[i] * denominador) + ")\\]\n"
        cosoFeo = cosoFeo + "\\[y_{" + str(i) + "}l_{" + str(i) + "}(x)="
        P = potencia(X1)
        Li = []
        for j in range(len(X)):
            b = 0
            for h in P:
                a = 1
                if len(h) == j:
                    for k in h:
                        a = a * k
                    b = b + a
            ssd = b * Y[i] / denominador
            cosoFeo = cosoFeo + "(" + str(ssd) + ")"
            if (len(F) - j - 1 == 1):
                cosoFeo = cosoFeo + "x+"
            else:
                if (len(F) - j - 1 == 0):
                    cosoFeo = cosoFeo + "+"
                else:
                    cosoFeo = cosoFeo + "x^{" + str(len(F) - j - 1) + "}+"
            Li.append(ssd)
        cosoFeo = cosoFeo + "\\]\n"
        L.append(Li)
        #
    for i in L:
        for j in range(len(i)):
            F[j] = F[j] + (i[j])
    todo = "\\[L(x)="
    v = False
    for i in range(len(F)):
        coso = "+"
        if F[i] != 0:
            if F[i] < 0 or v == False:
                v = True
                coso = ""
            coso2 = ""
            if (len(F) - i - 1) == 1:
                coso2 = "x"
            elif (len(F) - i - 1) == 0:
                coso2 = ""
            else:
                coso2 = "x^{" + str(len(F) - i - 1) + "}"
            todo = todo + coso + str(F[i]) + coso2
    if ImprimirProcedimiento == "Si":
        print(cosoFeo)
    print(str(todo) + "\\]")
    predicciones = []
    for j in x:
        fx = 0
        for i in range(len(F)):
            fx = fx + F[i] * (j ** (len(F) - i - 1))
        if ImprimirEvaluados == "Si":
            print("\\[L(" + str(j) + ")=" + str(fx) + "\\]")
        predicciones.append(fx)
    X2 = np.linspace(rango[0], rango[1], 1000)
    Y2 = []
    for j in X2:
        fx = 0
        for i in range(len(F)):
            fx = fx + F[i] * (j ** (len(F) - i - 1))
        Y2.append(fx)
    if grafica == "Si":
        plt.plot(x, predicciones, 'o')
        plt.plot(X2, Y2, '-')
        plt.show()
    return [F, predicciones]


# valores en x
X = [-2 * numpy.pi, -numpy.pi, 0, numpy.pi, 2 * numpy.pi]
# valores en Y
Y = [0, 0, 0, 0, 0]
# valores a evaluar
x = [-numpy.pi/2, 2, -2, numpy.pi]

A = InterpolanteLagrange(X, Y, x, ImprimirProcedimiento="Si", ImprimirEvaluados="Si", grafica="Si")
