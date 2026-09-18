from collections import deque

processes = [
    {"pid": "P1", "arrival": 0, "burst": 7, "priority": 2},
    {"pid": "P2", "arrival": 2, "burst": 4, "priority": 1},
    {"pid": "P3", "arrival": 4, "burst": 1, "priority": 3},
    {"pid": "P4", "arrival": 5, "burst": 4, "priority": 2},
]

def priority_scheduling(processes):
    current_time = 0
    completed = set()
    result = []

    while len(completed) < len(processes):

        ready = [
            p for p in processes
            if p["arrival"] <= current_time
            and p["pid"] not in completed
        ]

        if not ready:
            next_time = min(
                p["arrival"] for p in processes
                if p["pid"] not in completed
            )

            result.append(("IDLE", current_time, next_time))
            current_time = next_time
            continue

        p = min(
            ready,
            key=lambda x: (x["priority"], x["arrival"], x["pid"])
        )

        start = current_time
        end = start + p["burst"]

        result.append((p["pid"], start, end))

        current_time = end
        completed.add(p["pid"])

    return result


result = priority_scheduling(processes)

for item in result:
    print(item)