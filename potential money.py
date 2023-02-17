# Calculate proportion of transactions involving each source and destination in each cluster
sources = [c for c in df.columns if c.startswith('source_')]
destinations = [c for c in df.columns if c.startswith('destination_')]
source_proportions = df.groupby('cluster')[sources].mean()
destination_proportions = df.groupby('cluster')[destinations].mean()

# Identify clusters with high proportion of transactions involving suspicious sources or destinations
suspicious_sources = list(source_proportions[source_proportions['source_C'] > 0.5].index)
suspicious_destinations = list(destination_proportions[destination_proportions['destination_D'] > 0.5].index)
