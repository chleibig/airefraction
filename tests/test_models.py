from airefraction import models, data


def test_predict():
    X = data.load('tests/sample_zernike.xlsx')
    assert models.predict(X, tag='0a2c89f', target='s') == -0.83123493
    assert models.predict(X, tag='0a2c89f', target='m') == -1.17640030384064
    assert models.predict(X, tag='0a2c89f', target='j0') == 0.274268180131912
    assert models.predict(X, tag='0a2c89f', target='j45') == -0.141971915960312
