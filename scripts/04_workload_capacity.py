#workload capacity
import pandas as pd
import numpy as np

# waktu proses dalam menit
df_join['processing_time_minutes'] = (df_join['waktu_respon'] - df_join['waktu_permohonan_real']).dt.total_seconds()/60

daily_workload = (
    df_join.groupby(df_join['waktu_permohonan_real'].dt.date)
    .size()
    .reset_index(name='jumlah_permohonan')
)

import matplotlib.pyplot as plt

#top 5 subsimision by date
top_5 = daily_workload.nlargest(5, 'jumlah_permohonan')

plt.figure(figsize=(12, 6))

#Create Plot
plt.plot(daily_workload['waktu_permohonan_real'], daily_workload['jumlah_permohonan'], label='Daily Requests', color='#1f77b4', linewidth=1.5)

#Adding label 
for i, row in top_5.iterrows():
    plt.annotate(
        f"{int(row['jumlah_permohonan'])}", 
        (row['waktu_permohonan_real'], row['jumlah_permohonan']),
        textcoords="offset points", 
        xytext=(0, 10), # Posisi teks 10 poin di atas titik
        ha='center', 
        fontsize=10, 
        fontweight='bold',
        color='red', # Warna merah agar mencolok
        arrowprops=dict(arrowstyle='->', color='red', lw=1) # Menambahkan panah kecil
    )

#Complement the attribute
plt.title("Daily Workload (Top 5 Peaks Highlighted)", fontsize=14, fontweight='bold')
plt.xlabel("Date")
plt.ylabel("Number of Requests")
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

#Giving margin
plt.ylim(daily_workload['jumlah_permohonan'].min() - 2, daily_workload['jumlah_permohonan'].max() + 5)

plt.tight_layout()
plt.show()

#workload vs approval time (port)
capacity_analysis = df_join.groupby('PELABUHAN').agg(
    total_request=('nomor_pkk','count'),
    avg_processing_time=('approval_hours','mean')
).reset_index()


capacity_analysis
plt.figure(figsize=(8,6))

plt.scatter(
    capacity_analysis['total_request'],
    capacity_analysis['avg_processing_time']
)

plt.xlabel("Total Requests")
plt.ylabel("Average Processing Time (minutes)")
plt.title("Workload vs Capacity")
plt.show()
