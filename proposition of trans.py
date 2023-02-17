# Calculate proportion of large transactions in each cluster
df['is_large'] = df['amount'] > 0.8
proportions = df.groupby('cluster')['is_large'].mean()

# Identify clusters with high proportion of large transactions
suspicious_clusters = list(proportions[proportions > 0.5].index)
