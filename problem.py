import os
import numpy as np
import pandas as pd
import rampwf as rw

from pandas.core.indexes.range import RangeIndex
from rampwf.score_types import MARE

problem_title = 'Energy consumption prediction'
_target_column_name = 'consumption'
DATECOL = 'horodate'
_associated_targets = ['consumption']

# A type (class) which will be used to create wrapper objects for y_pred
Predictions = rw.prediction_types.make_regression()

# An object implementing the workflow
workflow = rw.workflows.Estimator()

# Score used
score_types = [
    MARE(precision=4),
]


def custom_time_series_split(X, n_splits, min_train_size):
    '''Same principle as sklearn TimeSeriesSplit, but with
    possibility of having a minimum train size.

    Arguments:
    X -- pd.DataFrame with sorted column horodate and sorted indexes
    n_splits -- int
    min_train_size -- int : minimum size of the train dataset
    '''
    assert pd.Index(X[DATECOL]).is_monotonic & \
        isinstance(X.index, RangeIndex), "Please provide a sorted DataFrame."
    n_samples = len(X)

    min_index_test = int(min_train_size * n_samples)
    min_index_test += (n_samples - min_index_test) % n_splits

    indices = np.arange(n_samples)
    test_size = (n_samples - min_index_test) // n_splits
    test_starts = range(min_index_test, n_samples, test_size)

    assert len(test_starts) == n_splits

    for test_start in test_starts:
        yield (indices[:test_start],
               indices[test_start:test_start + test_size])


def get_cv(X, y):
    return custom_time_series_split(X, n_splits=3, min_train_size=0.6)


def _read_data(path, f_name):
    data = pd.read_csv(os.path.join(path, 'data', f_name))
    data[DATECOL] = pd.to_datetime(data[DATECOL])
    data = data.sort_values(DATECOL)
    data.reset_index(inplace=True)
    y_array = data[_target_column_name].values
    X_df = data.drop(_associated_targets, axis=1)
    return X_df, y_array


def get_train_data(path='.'):
    f_name = 'data.csv'
    return _read_data(path, f_name)


def get_test_data(path='.'):
    f_name = 'data.csv'
    return _read_data(path, f_name)
