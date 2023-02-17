# Convert date to numerical value
df['date'] = pd.to_datetime(df['date']).astype(int)/10**9

# Scale transaction amount
scaler = MinMaxScaler()
df['amount'] = scaler.fit_transform(df['amount'].values.reshape(-1,1))

# One-hot encode source and destination
df = pd.get_dummies(df, columns=['source', 'destination'])
