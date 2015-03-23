__author__ = 'ivan'
from math import sqrt
# todo переопределить IndexError для внутренних методов(только) класса Vector


class Vector(list):
    def __init__(self, *args):
        res = 0.0
        for arg in args:
            res += arg**2
        self.vlen = sqrt(res)   # Длина вектора
        super(Vector, self).__init__([_ for _ in args])

    def __add__(self, other):   #todo -> Vector
        """
        + Покоординатное сложение
        :returns Vector
        """
        return self.__class__(*[self[i]+other[i] for i in range(len(self))])

    def __sub__(self, other):   #todo -> Vector
        """
        - Производит покоординатное вычитание
        :returns Vector
        """
        return self.__class__(*[self[i]-other[i] for i in range(len(self))])

    def __mul__(self, other):
        if type(other) == self.__class__:
            """
            * Скалярное произведение
            :returns float
            """
            if len(self) != len(other):
                raise VectorError('Разное количество координат у векторов')
            res = 0.0
            for i in range(len(self)):
                res += self[i] * other[i]
            return res
        elif type(other) == int or type(other) == float:
            """
            Умножение вектора на число
            :returns Vector
            """
            return self.__class__(*[self[i]*other for i in range(len(self))])
        else:
            raise Exception('Умножение вектора на {} не предусмотрено'.format(other))

    def __truediv__(self, other):
        """ / Деление вектора на скаляр"""
        return self * (1/other)

    def ed(self):
        """Возвращает сонаправленный единичный вектор"""
        return self * (1/self.vlen) # self.__class__(*[self[i]/self.vlen for i in range(len(self))])


class VectorError(Exception):
    def __init__(self, _str):
        super(VectorError, self).__init__(_str)


def scalar(v1, v2):
    """
    Считает скалярное произведение 2-х векторов
    :param v1:
    :param v2:
    :return: :raise DimensionError: возвращает ошибку, если у векторов разное колво координат
    """
    if len(v1) != len(v2):
        raise VectorError
    res = 0.0
    for dim in range(v1):
        res += v1[dim] * v2[dim]
    return res


def vlen(vec):
    """
    Считает длину вектора(через скалярное произведение)
    :param vec:
    """
    res = 0.0
    for cord in vec:
        res += cord**2
    return sqrt(res)


def singlify(vec):
    """
    Возвращает сонаправленный вектор единичной длины
    :param vec:
    """
    resv = []
    _len = vlen(vec)
    for cord in vec:
        resv.append((cord/_len))
    return resv

def multy(i):
    res = []
    for j in range(i):
        res.append()

def ort_gs(*vectors):
    """
    Ортогонализация Грамма-Шмидта - получение из произвольного базиса ортонормированный
    :param vects:
    """
    f = list(vectors)
    #for i in range(len(f)):
    #    f[i] = f[i].ed()
    e = [f[0]]
    for k in range(1, len(vectors)):
        v_sum = Vector(*[0.0 for _ in range(len(f[k]))])
        for i in range(k):
            v_sum = v_sum + (e[i] * (f[k]*e[i]) / (e[i]*e[i]))
        e.append(f[k] - v_sum)
    for i in range(len(f)):
        e[i] = e[i].ed()
    return e