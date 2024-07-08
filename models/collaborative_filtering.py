import pandas as pd
from surprise import Dataset, Reader, SVD, KNNBaseline
from surprise.model_selection import cross_validate, train_test_split
from surprise.model_selection import GridSearchCV
from surprise import accuracy

def collaborative_filtering(train_file):
    reader = Reader(line_format='user item rating timestamp', sep=',')
    data = Dataset.load_from_file(train_file, reader=reader)
    
    trainset, testset = train_test_split(data, test_size=0.2)

    # Hyperparameter tuning for SVD
    param_grid = {
        'n_factors': [50, 100, 150],
        'n_epochs': [20, 30, 40],
        'lr_all': [0.002, 0.005],
        'reg_all': [0.4, 0.6]  
    }
    gs = GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=3)
    gs.fit(data)

    # Best model
    algo = gs.best_estimator['rmse']
    algo.fit(trainset)

    predictions = algo.test(testset)
    accuracy.rmse(predictions)
    accuracy.mae(predictions)
    
    return algo
    
if __name__ == "__main__":
    collaborative_filtering('train_data.csv')
