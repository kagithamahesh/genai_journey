# A small dataset of question-answer pairs
results = [
    {"id": 1, "category": "factual",    "expected": "Paris",       "predicted": "Paris",       "latency_ms": 320},
    {"id": 2, "category": "factual",    "expected": "1969",        "predicted": "1968",        "latency_ms": 290},
    {"id": 3, "category": "reasoning",  "expected": "positive",    "predicted": "positive",    "latency_ms": 510},
    {"id": 4, "category": "reasoning",  "expected": "negative",    "predicted": "neutral",     "latency_ms": 480},
    {"id": 5, "category": "factual",    "expected": "Newton",      "predicted": "Newton",      "latency_ms": 305},
    {"id": 6, "category": "reasoning",  "expected": "positive",    "predicted": "positive",    "latency_ms": 540},
    {"id": 7, "category": "creative",   "expected": "varies",      "predicted": "some poem",   "latency_ms": 890},
    {"id": 8, "category": "creative",   "expected": "varies",      "predicted": "another one", "latency_ms": 760},
]


def exact_match(results):
    valid = [r for r in results if r["expected"] != "varies"]

    if not valid:
        return 0.0

    correct = sum(1 for r in valid if r["expected"] == r["predicted"])
    return correct / len(valid)


def accuracy_by_category(results):
    categories = {}

    for row in results:
        cat = row["category"]
        categories.setdefault(cat, []).append(row)

    report = {}

    for cat, rows in categories.items():
        valid = [r for r in rows if r["expected"] != "varies"]

        if not valid:
            report[cat] = None
        else:
            correct = sum(1 for r in valid if r["expected"] == r["predicted"])
            report[cat] = correct / len(valid)

    return report


def latency_report(results):
    latencies = [r["latency_ms"] for r in results]

    slowest = max(results, key=lambda r: r["latency_ms"])

    return {
        "mean_ms": sum(latencies) / len(latencies),
        "min_ms": min(latencies),
        "max_ms": max(latencies),
        "slowest_id": slowest["id"]
    }


def failing_cases(results):
    failures = []

    for r in results:
        if r["expected"] != "varies" and r["expected"] != r["predicted"]:
            failures.append({
                "id": r["id"],
                "category": r["category"],
                "expected": r["expected"],
                "predicted": r["predicted"]
            })

    return failures


def full_report(results):
    overall = exact_match(results)
    by_cat = accuracy_by_category(results)
    latency = latency_report(results)
    failures = failing_cases(results)

    # Round category values
    rounded_cat = {
        k: (None if v is None else round(v, 2))
        for k, v in by_cat.items()
    }

    print("=== Eval Report ===")
    print(f"Overall accuracy : {overall:.2f}")
    print(f"By category      : {rounded_cat}")
    print(
        f"Mean latency     : {round(latency['mean_ms'])}ms   "
        f"Min: {latency['min_ms']}ms   "
        f"Max: {latency['max_ms']}ms   "
        f"Slowest ID: {latency['slowest_id']}"
    )
    print(f"Failing cases    : {len(failures)}")

    for f in failures:
        print(
            f"  [{f['id']}] {f['category']} — "
            f"expected '{f['expected']}', got '{f['predicted']}'"
        )


# Run report
full_report(results)