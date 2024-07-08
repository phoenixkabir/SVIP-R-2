import pandas as pd

def mitigate_bias(recommendations):
    # Example algorithm to mitigate bias
    mean_rating = recommendations['rating'].mean()
    recommendations['rating'] = recommendations['rating'].apply(lambda x: x if x > mean_rating else mean_rating)
    return recommendations

if __name__ == "__main__":
    recommendations = pd.read_csv('recommendations.csv')
    unbiased_recommendations = mitigate_bias(recommendations)
    unbiased_recommendations.to_csv('unbiased_recommendations.csv', index=False)
