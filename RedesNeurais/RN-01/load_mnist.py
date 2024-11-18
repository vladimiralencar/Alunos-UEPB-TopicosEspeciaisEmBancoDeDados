from sklearn.datasets import fetch_openml
from sklearn.utils import check_random_state
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

def fetch_data(test_size=10000, randomize=False, standardize=False):
    X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
    if randomize:
        random_state = check_random_state(0)
        permutation = random_state.permutation(X.shape[0])
        X = X[permutation]
        y = y[permutation]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, shuffle=False)
    if standardize:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
    return X_train.to_numpy(dtype=np.int16), y_train.to_numpy(dtype=np.int16), X_test.to_numpy(dtype=np.int16), y_test.to_numpy(dtype=np.int16)


if __name__ == '__main__':
    train_data, train_labels, test_data, test_labels = fetch_data()
