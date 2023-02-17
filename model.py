# Fit KMeans model
kmeans = KMeans(n_clusters=5)
kmeans.fit(df[['amount', 'date', 'source_A', 'destination_B']])

# Get cluster labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Add cluster labels to dataframe
df['cluster'] = labels
