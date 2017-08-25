import sys
import shutil
from airefraction import cli
import pandas as pd


def test_cli(tmpdir, monkeypatch):
    infile = shutil.copy('tests/sample_zernike.xlsx', tmpdir.strpath)
    outfile = tmpdir.join('sample_corrections.xlsx').strpath
    monkeypatch.setattr(sys, 'argv',
                        ['', infile, outfile])
    cli.main()
    df = pd.read_excel(outfile)
    assert tuple(df.columns) == ('s', 'm', 'j0', 'j45')
    eps = 1e-6
    assert abs(df.s[0] - (-0.83123493)) < eps
    assert abs(df.m[0] - (-1.17640030384064)) < eps
    assert abs(df.j0[0] - 0.274268180131912) < eps
    assert abs(df.j45[0] - (-0.141971915960312)) < eps



