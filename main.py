import csv


def get_health_status(health_score):
    if health_score >= 80:
        return "HEALTHY"
    elif health_score >= 50:
        return "WARNING"
    else:
        return "CRITICAL"

    
def check_machine(machine_name, temperature, vibration, pressure):
    problems = []
    health_score = 100

    if temperature >= 80:
        problems.append("High temperature")
        health_score -= 30
    elif temperature >= 70:
        problems.append("Temperature warning")
        health_score -= 15

    if vibration >= 8:
        problems.append("High vibration")
        health_score -= 30

    if pressure >= 100:
        problems.append("High pressure")
        health_score -= 20

    health_score = max(health_score, 0)

    return problems, health_score

healthy_count = 0
warning_count = 0
critical_count = 0

with open("sensor_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        machine = row["machine"]
        temperature = float(row["temperature"])
        vibration = float(row["vibration"])
        pressure = float(row["pressure"])

        problems, health_score = check_machine(
            machine,
            temperature,
            vibration,
            pressure
        )

        status = get_health_status(health_score)

        if status == "HEALTHY":
            healthy_count += 1
        elif status == "WARNING":
            warning_count += 1
        else:
            critical_count += 1

        print(f"\n{machine}")
        print(f"Health Score: {health_score}/100 - {status}")

        if problems:
            print("Problems:")
            for problem in problems:
                print(f"- {problem}")
        else:
            print("Machine is operating normally.")

print("\n--- SYSTEM SUMMARY ---")
print(f"Healthy machines: {healthy_count}")
print(f"Warning machines: {warning_count}")
print(f"Critical machines: {critical_count}")