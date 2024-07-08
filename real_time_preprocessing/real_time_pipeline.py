from kafka import KafkaConsumer, KafkaProducer
import json
import pandas as pd
from tensorflow import load_model
from sklearn.preprocessing import StandardScaler

model = load_model('deep_learning_model.h5')
scaler = StandardScaler()

def consume_and_process():
    consumer = KafkaConsumer('input_topic', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    
    for message in consumer:
        data = json.loads(message.value.decode('utf-8'))
        processed_data = data_processing_logic(data)
        prediction = model.predict(scaler.transform([processed_data]))[0][0]
        producer.send('output_topic', json.dumps({'prediction': prediction}).encode('utf-8'))

def data_processing_logic(data):
    # Process incoming data
    data_df = pd.DataFrame([data])
    data_df = data_df.drop(['label'], axis=1)
    return data_df.values[0]

if __name__ == "__main__":
    consume_and_process()
