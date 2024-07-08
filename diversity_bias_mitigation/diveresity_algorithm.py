import pandas as pd
import numpy as np

def promote_diversity(recommendations):
    # Example algorithm to promote diversity
    content_types = recommendations['content_type'].unique()
    diverse_recommendations = []
    for content_type in content_types:
        diverse_recommendations.append(recommendations[recommendations['content_type'] == content_type].sample(1))
    return pd.concat(diverse_recommendations)

if __name__ == "__main__":
    recommendations = pd.read_csv('recommendations.csv')
    diverse_recommendations = promote_diversity(recommendations)
    diverse_recommendations.to_csv('diverse_recommendations.csv', index=False)
