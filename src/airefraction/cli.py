import argparse


def main():
    """Compute refractive error corrections"""

    from airefraction import data

    description = 'Compute refractive error corrections.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('infile',
                        help='Excel file with pupil diameters and Zernike '
                             'coefficients. Each row describes one eye.'
                             ' The header must be as follows: ' +
                             str(data.HEADER))
    parser.add_argument('outfile', help='For saving the refractive error '
                                        'corrections.')
    args = parser.parse_args()

    from airefraction import models
    from collections import OrderedDict

    X = data.load(args.infile)
    predictions = OrderedDict()
    for target in ['s', 'm', 'j0', 'j45']:
        predictions[target] = models.predict(X, target=target)[:, 0]
        print(target, predictions[target])

    import pandas as pd
    pd.DataFrame(predictions).to_excel(args.outfile, index=False)


if __name__ == "__main__":
    main()
