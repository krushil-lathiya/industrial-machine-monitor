import pandas as pd

data = pd.read_csv("sensor_data.csv")

print(data)

print("\n--- BASIC STATISTICS ---")
print(data.describe())

hottest_machine = data.loc[data["temperature"].idxmax()]

print("\n--- HOTTEST MACHINE ---")
print(hottest_machine)

highest_vibration = data.loc[data["vibration"].idxmax()]

print("\n--- HIGHEST VIBRATION ---")
print(highest_vibration)

attention = data[
    (data["temperature"] >= 70) |
    (data["vibration"] >= 8) |
    (data["pressure"] >= 100)
]


print("\n--- MACHINES NEEDING ATTENTION ---")
print(attention)


print("\n--- AVERAGE SENSOR VALUES ---")

print(f"Average temperature: {data['temperature'].mean():.2f}°C")
print(f"Average vibration: {data['vibration'].mean():.2f} mm/s")
print(f"Average pressure: {data['pressure'].mean():.2f} bar")