import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def content_based_filtering(train_file):
    data = pd.read_csv(train_file)
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = tfidf.fit_transform(data['content'])
    
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(data.index, index=data['title']).drop_duplicates()
    
    return cosine_sim, indices

def get_recommendations(title, cosine_sim, indices, data):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    
    item_indices = [i[0] for i in sim_scores]
    return data['title'].iloc[item_indices]

if __name__ == "__main__":
    cosine_sim, indices = content_based_filtering('train_data.csv')
    data = pd.read_csv('train_data.csv')
    print(get_recommendations('Interesting documentary', cosine_sim, indices, data))
