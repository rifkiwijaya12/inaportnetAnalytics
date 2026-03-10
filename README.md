# Inaportnet analytics - Indonesian Port 2025

This project was conducted to analyze the one of all port services across 109 port in Indonesia during 2025.
The objective is to evaluate service performance based on service level agreement compliance and classify the port efficiency according to operational workload and average approval time.

The analysis begins with data collection through web-scraping from the Inaportnet monitoring portal:
https://monitoring-inaportnet.dephub.go.id/
The data collection script is not included in this repository as the project focuses primarily on the analytical process.
The dataset covers PKK (Ship Arrival Approval) records collected throughout 2025.
Prior to analysis, data preprocessing was conducted to examine the dataset structure and calculate approval time based on the time difference between request submission and the approval response.


# Project Structure

inaportnet-analysis
│
├── data
│   ├── raw
│   └── processed
│
├── scripts
│   ├── data_collection.py
│   ├── traffic_analysis.py
│   ├── service_performance.py
│   ├── sla_risk_analysis.py
│   ├── workload_capacity_analysis.py
│   └── port_classification.py
│
├── results
│
└── README.md

# Potential insight

This analytical framework provides traffic concentration across major ports in Indonesia, temporal traffic pattern, service performance and compliance, workload analysis, and port classification.
The port classification framework helps identify ports that may require operational attention, particularly those categorized as **Low Performance** or **Bottleneck** ports.

# Future Improvement

This project can be further enhanced by developing an interactive dashboard visualization and applying predictive service demand modelling to forecast and estimating workforce requrierments.
