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

    return {
        "machine": machine_name,
        "temperature": temperature,
        "vibration": vibration,
        "pressure": pressure,
        "problems": problems,
        "health_score": health_score
    }


machines = [
    ("Machine A", 65, 4.5, 80),
    ("Machine B", 75, 9.2, 105),
    ("Machine C", 85, 6.0, 95)
]

for machine in machines:
    result = check_machine(*machine)

    print(f"\n{result['machine']}")
    print(f"Health Score: {result['health_score']}/100")

    if result["problems"]:
        print("Problems:")
        for problem in result["problems"]:
            print(f"- {problem}")
    else:
        print("Machine is operating normally.")