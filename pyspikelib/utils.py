import numpy as np
import pandas as pd


def distribution_features_tsfresh_dict():
    ratios_beyond_r_sigma_rvalues = [1, 1.5, 2, 2.5, 3, 5, 6, 7, 10]

    feature_dict = {
        'symmetry_looking': [{'r': value} for value in np.arange(0.05, 1.0, 0.05)],
        'standard_deviation': None,
        'kurtosis': None,
        'variance_larger_than_standard_deviation': None,
        'ratio_beyond_r_sigma': [
            {'r': value} for value in ratios_beyond_r_sigma_rvalues
        ],
        'count_below_mean': None,
        'maximum': None,
        'variance': None,
        'abs_energy': None,
        'mean': None,
        'skewness': None,
        'length': None,
        'large_standard_deviation': [
            {'r': value} for value in np.arange(0.05, 1.0, 0.05)
        ],
        'count_above_mean': None,
        'minimum': None,
        'sum_values': None,
        'quantile': [{'q': value} for value in np.arange(0.1, 1.0, 0.1)],
        'ratio_value_number_to_time_series_length': None,
        'median': None,
    }

    return feature_dict


def tsfresh_dataframe_stats(df):
    unique_values = []

    for key in df.columns.values:
        unique_values.append(
            pd.Series(df[key].values.astype(np.float32)).value_counts().values.shape[0]
        )

    unique_values = np.array(unique_values)

    max_values = 30
    features = {}
    features['nan'] = df.columns.values[np.where(unique_values == 0)[0]]
    features['binary'] = df.columns.values[np.where(unique_values == 2)[0]]
    features['categorial'] = df.columns.values[
        np.where((unique_values > 2) & (unique_values < max_values))[0]
    ]

    return features


def train_test_common_features(train_df, test_df):
    train_feature_set = set(train_df.columns.values)
    test_feature_set = set(test_df.columns.values)
    train_df = train_df.loc[:, train_feature_set.intersection(test_feature_set)]
    test_df = test_df.loc[:, train_feature_set.intersection(test_feature_set)]
    return train_df, test_df
