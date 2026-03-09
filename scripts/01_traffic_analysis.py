#traffic analysis
#TRAFFFIC ANALYSIS
#total number of PKK service
total_pkk = df_join.shape[0]
print("Total PKK service on national:", total_pkk)

#average traffic per months
traffic_port = (
    df_join.groupby(['KODE','PELABUHAN'])
    .size()
    .reset_index(name='total_pkk')
    .sort_values('total_pkk', ascending=False)
)
traffic_port.head(10)

#national traffic share on each port
traffic_port['share_%'] = (
    traffic_port['total_pkk'] /
    traffic_port['total_pkk'].sum() * 100
)
traffic_port.head(10)

#top 10 port based on traffic volume
traffic_port = traffic_port.sort_values(by='total_pkk', ascending=False)
top10 = traffic_port.head(10).copy()
others = traffic_port.iloc[10:]
others_sum = others['total_pkk'].sum()
other_row = pd.DataFrame({
    'PELABUHAN': ['Other'],
    'total_pkk': [others_sum]
    })

pie_df = pd.concat([top10[['PELABUHAN','total_pkk']], other_row], ignore_index=True)

#plot top 10 busiest port
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8,8))

wedges, texts, autotexts = ax.pie(
    pie_df['total_pkk'],
    labels=pie_df['PELABUHAN'],
    autopct='%1.1f%%',
    startangle=90
)

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

ax.set_title("Market Share PKK - Top 10 Pelabuhan")

plt.tight_layout()
plt.show()

#Quartal trend
trend_qtr = df_join.groupby('quarter').size().reset_index(name='total_service')

# Plot
import matplotlib.pyplot as plt

trend_qtr.plot(
    x='quarter',
    y='total_service',
    kind='bar',
    color='skyblue',
    edgecolor='black',
    figsize=(10, 6),
    legend=False
)
plt.title('Submission trend per Quarter')
plt.xlabel('Quarter')
plt.ylabel('total_service')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#traffic per bulan
traffic_monthly = (
    df_join.groupby(['year','month'])
    .size()
    .reset_index(name='total_service')
    .sort_values(['year','month'])
)
month_names = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'Oktober', 11: 'November', 12: 'December'
}

traffic_monthly['month'] = traffic_monthly['month'].map(month_names)
# Plot
import matplotlib.pyplot as plt

ax = traffic_monthly.plot(
    x='month',
    y='total_service',
    kind='bar',
    color='skyblue',
    edgecolor='black',
    figsize=(10, 6),
    legend=False
)
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 9), 
                textcoords='offset points',
                fontsize=10,
                fontweight='bold')
plt.title('Submission trend per Months')
plt.xlabel('Month')
plt.ylabel('jtotal_service')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#traffic per hari
traffic_day = (
    df_join.groupby('day')
    .size()
    .reset_index(name='total_service')
)

order_day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

traffic_day['day'] = pd.Categorical(
    traffic_day['day'],
    categories=order_day,
    ordered=True
)

traffic_day = traffic_day.sort_values('day')
traffic_day.head(10)

import matplotlib.pyplot as plt

# Create Plot
ax = traffic_day.plot(
    x='day', 
    y='total_service', 
    kind='bar', 
    color='skyblue', 
    edgecolor='black', 
    figsize=(10, 6),
    legend=False  # remove legend
)

# Adding label above the graph
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 9), 
                textcoords='offset points',
                fontsize=10,
                fontweight='bold')

# Complementing the graph attribute
plt.title('Submission trend by Day', fontsize=14, fontweight='bold')
plt.xlabel('Day', fontsize=12)
plt.ylabel('total_service', fontsize=12)
plt.xticks(rotation=0) # Hari biasanya cukup pendek, jadi rotasi 0 saja agar tegak
plt.grid(axis='y', linestyle='--', alpha=0.5)

# adding height of graph to give more spaces
plt.ylim(0, traffic_day['total_service'].max() * 1.1)

plt.tight_layout()
plt.show()

#traffic by hour
traffic_hour = (
    df_join.groupby('hour')
    .size()
    .reset_index(name='total_service')
    .sort_values('hour')
)

# Creating Plot
ax = traffic_hour.plot(
    x='hour', 
    y='total_service', 
    kind='bar', 
    color='skyblue', 
    edgecolor='black', 
    figsize=(10, 6),
    legend=False  # Menghilangkan legend
)

#plot dataset
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 9), 
                textcoords='offset points',
                fontsize=10,
                fontweight='bold')

plt.title('Submission trend Per Hour', fontsize=14, fontweight='bold')
plt.xlabel('Hour', fontsize=12)
plt.ylabel('total_service', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Memberikan ruang di atas agar label tidak terpotong
plt.ylim(0, traffic_day['total_service'].max() * 1.1)

plt.tight_layout()
plt.show()
