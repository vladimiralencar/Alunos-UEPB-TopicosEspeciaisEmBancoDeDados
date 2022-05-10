
# pip install s3fs
import pandas as pd
url = 's3://teste2022a/VolumedeAcudes.csv'
df = pd.read_csv(url)
df.head()