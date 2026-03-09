#port classification
port_metrics = df.groupby('PELABUHAN').agg(
    total_request=('nomor_pkK','count'),
    avg_processing_time=('processing_time_minutes','mean')
).reset_index()

port_metrics

workload_threshold = port_metrics['total_request'].median()
capacity_threshold = port_metrics['avg_processing_time'].median()

def classify_port(row):
    if row['total_request'] >= workload_threshold and row['avg_processing_time'] <= capacity_threshold:
        return "High Demand - Efficient"
    
    elif row['total_request'] >= workload_threshold and row['avg_processing_time'] > capacity_threshold:
        return "High Demand - Bottleneck"
    
    elif row['total_request'] < workload_threshold and row['avg_processing_time'] <= capacity_threshold:
        return "Underutilized"
    
    else:
        return "Low Performance"

port_metrics['port_classification'] = port_metrics.apply(classify_port, axis=1)

import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

plt.scatter(
    port_metrics['total_request'],
    port_metrics['avg_processing_time']
)

plt.axvline(workload_threshold, linestyle='--')
plt.axhline(capacity_threshold, linestyle='--')

plt.xlabel("Total Request (Workload)")
plt.ylabel("Average Processing Time (Capacity)")
plt.title("Port Classification Matrix")

for i, row in port_metrics.iterrows():
    plt.text(row['total_request'], row['avg_processing_time'], row['PELABUHAN'])

plt.show()
