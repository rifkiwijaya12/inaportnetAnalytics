#data preprocessing
import datetime
from datetime import datetime, timedelta

df_join['waktu_permohonan'] = pd.to_datetime(df_join['waktu_permohonan'], format='%Y-%m-%d %H:%M:%S')
df_join['waktu_respon'] = pd.to_datetime(df_join['waktu_respon'], format='%Y-%m-%d %H:%M:%S')

df_join['waktu_permohonan_real'] = df_join['waktu_permohonan']+ pd.to_timedelta(df_join['ZONE_GMT'], unit='h')
df_join['approval_time'] = df_join['waktu_respon']-df_join['waktu_permohonan_real']
df_join['approval_hours'] = df_join['approval_time'].dt.total_seconds() / 3600

df_join['year'] = df_join['waktu_permohonan_real'].dt.year
df_join['quarter'] = df_join['waktu_permohonan_real'].dt.to_period('Q')
df_join['month'] = df_join['waktu_permohonan_real'].dt.month
df_join['date'] = df_join['waktu_permohonan_real'].dt.date
df_join['day'] = df_join['waktu_permohonan_real'].dt.day_name()
df_join['hour'] = df_join['waktu_permohonan_real'].dt.hour


# Menghapus baris dengan year 2024
df_join = df_join[df_join['year'] != 2024]
df_join = df_join[df_join['year'] != 2023]

df_join.head()

#Checking bug
df_join_bug=df_join[df_join['approval_time']<timedelta(seconds=0)]
df_join_bug.head()

df_join_bug.head()
#df_join_bug.to_excel('data_bug.xlsx', index=False)
