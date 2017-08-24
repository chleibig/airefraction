import numpy as np
from airefraction import data


def test_HEADER():
    assert len(set(data.HEADER)) == 37


def test_load():
    X = data.load('tests/sample_zernike.xlsx')
    assert X.shape == (1, 37)
    assert (abs(X[0, :4] - np.array([4, -0.1740173722,
                                     0.38206546, 1.09698597])) < 1e-8).all()
