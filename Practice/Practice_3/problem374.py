import pandas as pd
import sys

df = pd.read_csv(sys.stdin, encoding='unicode_escape', encoding_errors='replace')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

last_date = df.groupby('CustomerID')['InvoiceDate'].max().reset_index()

old = last_date['InvoiceDate'].min()

last_date['score'] = (last_date['InvoiceDate'] - old).dt.days

result = last_date.sort_values('CustomerID')[['CustomerID', 'score']]

print(" CustomerID  score")
for _, row in result.iterrows():
    sys.stdout.write(f"{row['CustomerID']:>11.1f} {int(row['score']):>7}\n")
    
# tham kháº£o: Claue.ai
# CÃ¢u prompt: dá»±a vÃ o Äoáº¡n code vÃ  output sau hÃ£y viáº¿t cÃ¢u lá»nh in ra mÃ n hÃ¬nh giá»ng output

