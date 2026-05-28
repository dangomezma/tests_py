import pytest
import math
from micode import calcular_distancia

def test_distancia_profe():
    p1=[0,0]
    p2=[3,4]
    assert math.isclose(calcular_distancia(p1, p2),5)

def test_distancia_basica():
    p1=[5,500]
    p2=[5,300]
    assert math.isclose(calcular_distancia(p1, p2),200.0)

def test_distancia_negativa():
    p1=[-5,-10]
    p2=[-5,-15]
    assert math.isclose(calcular_distancia(p1, p2),5.0)

def test_distancia_dec():
    p1=[-1,-56]
    p2=[-1.0001,-56]
    assert math.isclose(calcular_distancia(p1, p2),0.0001)