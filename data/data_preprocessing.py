import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    
    # Handling missing values
    data.fillna(method='ffill', inplace=True)
    
    # Label encoding for categorical features
    le = LabelEncoder()
    data['user'] = le.fit_transform(data['user'])
    data['item'] = le.fit_transform(data['item'])
    
    # Feature scaling
    scaler = StandardScaler()
    numerical_features = ['rating', 'timestamp', 'engagement']
    data[numerical_features] = scaler.fit_transform(data[numerical_features])
    
    # Split data
    train, test = train_test_split(data, test_size=0.2)
    train.to_csv('train_data.csv', index=False)
    test.to_csv('test_data.csv', index=False)

if __name__ == "__main__":
    load_and_preprocess_data('sample_data.csv')
