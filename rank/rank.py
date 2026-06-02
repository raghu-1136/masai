def rank_students(students, exclude_names):
    filtered = []
    for student in students:
        if student["name"] in exclude_names:
            continue
        if student["score"] == 0:
            break
        filtered.append(student)

    rank = 0
    result = []
    for student in sorted(filtered, key=lambda x: x["score"], reverse=True):
        rank += 1
        if student["score"] >= 50:
            result.append({
                "name": student["name"],
                "rank": rank
            })
    return result

if __name__ == "__main__":
    students = [
        {"name": "Venki",    "score": 95},
        {"name": "Karthik",  "score": 72},
        {"name": "Harini",   "score": 45},
        {"name": "Abishek",  "score": 88},
        {"name": "Vicky",    "score": 60},
        {"name": "Rinky",    "score":  0},
        {"name": "Surya",    "score": 55},
    ]
    exclude_names = ["Harini"]
    print(rank_students(students, exclude_names))
