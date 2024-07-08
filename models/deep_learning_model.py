import pandas as pd
import tensorflow as tf
from tensorflow import Sequential
from tensorflow import Dense, Dropout
from sklearn.preprocessing import StandardScaler

def build_and_train_model(train_file):
    data = pd.read_csv(train_file)
    
    # Data preparation
    X = data.drop(['label'], axis=1)
    y = data['label']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Build model
    model = Sequential()
    model.add(Dense(128, input_dim=X_scaled.shape[1], activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation='sigmoid'))
    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    # Train model
    model.fit(X_scaled, y, epochs=50, batch_size=64, validation_split=0.2)
    model.save('deep_learning_model.h5')

if __name__ == "__main__":
    build_and_train_model('train_data.csv')
