from keras.models import load_model
import numpy as np
import os
import warnings


def predict(X, tag='0a2c89f', target='s'):
    here = os.path.abspath(os.path.dirname(__file__))
    model_path = os.path.join(here, 'models', tag)

    MEAN = np.load(os.path.join(model_path, 'MEAN.npy'))
    X_preprocessed = X - MEAN
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        # load_model raises:
        #
        # UserWarning: Error in loading the saved optimizer state. As a
        # result, your model is starting with a freshly initialized optimizer.
        #
        # This can be savely ignored because we don't use the optimizer here.
        model = load_model(os.path.join(model_path,
                                        'best_weights_' + target + '.h5'))

    return model.predict(X_preprocessed)
