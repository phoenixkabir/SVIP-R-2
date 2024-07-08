import pandas as pd
from sklearn.metrics import mean_squared_error, accuracy_score

def evaluate_model(predictions_file, test_file):
    predictions = pd.read_csv(predictions_file)
    test = pd.read_csv(test_file)
    
    rmse = mean_squared_error(test['rating'], predictions['rating'], squared=False)
    accuracy = accuracy_score(test['label'], predictions['label'])
    
    print(f'RMSE: {rmse}, Accuracy: {accuracy}')

if __name__ == "__main__":
    evaluate_model('predictions.csv', 'test_data.csv')
