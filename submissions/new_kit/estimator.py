import numpy as np
import datetime as dt

from sklearn.base import BaseEstimator
from sklearn.compose import make_column_transformer
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer


class Regressor(BaseEstimator):
    def __init__(self, regressor=GradientBoostingRegressor()):
        self.regressor = regressor

    def fit(self, X, y):
        self.regressor.fit(X, y)
        return self

    def predict(self, X):
        y_pred = self.regressor.predict(X)
        return y_pred


class FeatureExtractor(object):

    def transform(self, X):
        """Create numerical features based on horodate."""
        _X = X.copy()
        # _X["horodate"] = pd.to_datetime(X["horodate"], utc=True)
        _X["period_daily_cos"] = X["horodate"].apply(
            lambda x: np.cos(2 * np.pi * self._time_in_day(x)))
        _X["period_daily_sin"] = X["horodate"].apply(
            lambda x: np.sin(2 * np.pi * self._time_in_day(x)))
        _X["period_weekly_cos"] = X["horodate"].apply(
            lambda x: np.cos(2 * np.pi * self._time_in_week(x)))
        _X["period_weekly_sin"] = X["horodate"].apply(
            lambda x: np.sin(2 * np.pi * self._time_in_week(x)))
        _X["period_yearly_cos"] = X["horodate"].apply(
            lambda x: np.cos(2 * np.pi * self._time_in_year(x)))
        _X["period_yearly_sin"] = X["horodate"].apply(
            lambda x: np.sin(2 * np.pi * self._time_in_year(x)))
        _X.drop(columns="horodate", inplace=True)
        return _X.to_numpy()

    # Utility functions that help converting horodate into meaningful features.
    def _time_in_day(self, x):
        return (x.hour + x.minute / 60) / 24

    def _time_in_week(self, x):
        return (x.weekday() + (x.hour + x.minute / 60) / 24) / 7

    def _time_in_year(self, x):
        scds_since_beginning_year = x - dt.datetime(x.year, 1, 1,
                                                    tzinfo=x.tzinfo)
        total_scds_year = dt.datetime(x.year, 12, 31, 23, 30,
                                      tzinfo=x.tzinfo) - \
            dt.datetime(x.year, 1, 1, tzinfo=x.tzinfo)
        return scds_since_beginning_year / total_scds_year


def get_estimator():
    # transformer
    date_transformer = FunctionTransformer(FeatureExtractor().transform)
    date_cols = ['horodate']

    # preprocessor
    preprocessor = make_column_transformer(
        (date_transformer, date_cols),
        remainder='passthrough',
    )

    # estimator
    regressor = Regressor()

    return make_pipeline(preprocessor, regressor)
