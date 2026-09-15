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


with open("report.txt", "w") as report:
    report.write("INDUSTRIAL MACHINE MONITORING REPORT\n")
    report.write("=" * 40 + "\n\n")

    report.write(f"Average temperature: {data['temperature'].mean():.2f}°C\n")
    report.write(f"Average vibration: {data['vibration'].mean():.2f} mm/s\n")
    report.write(f"Average pressure: {data['pressure'].mean():.2f} bar\n\n")

    report.write("MACHINE STATUS\n")
    report.write("-" * 40 + "\n")

    for _, machine in data.iterrows():

        temperature = machine["temperature"]
        vibration = machine["vibration"]
        pressure = machine["pressure"]

        health_score = 100

        if temperature >= 80:
            health_score -= 30
        elif temperature >= 70:
            health_score -= 15

        if vibration >= 8:
            health_score -= 30

        if pressure >= 100:
            health_score -= 20

        health_score = max(health_score, 0)

        if health_score >= 80:
            status = "HEALTHY"
        elif health_score >= 50:
            status = "WARNING"
        else:
            status = "CRITICAL"

        report.write(
            f"{machine['machine']}: "
            f"{health_score}/100 - {status}\n"
        )