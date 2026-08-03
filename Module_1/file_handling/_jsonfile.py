import json

students = [
    {"name": "Aryan", "score": 88},
    {"name": "Divya", "score": 74},
    {"name": "Keerthana", "score": 91},
    {"name": "Rajan", "score": 65},
    {"name": "Snehal", "score": 79},
]
log_message = "Records written successfully."

# Step 1: Write student records to records.json
# TODO: open "records.json" in write mode and use json.dump
with open("records.json","w") as f:
    json.dump(students,f)
# Step 2: Append log message to events.log
# TODO: open "events.log" in append mode and write log_message
with open("events.log","a") as e:
    e.write(log_message +"\n")
# Step 3: Read records.json back and print each student's name and score
# TODO: open "records.json" in read mode, use json.load, iterate and print
with open ("records.json","r") as r:
  loaded_students =  json.load(r)
  for i in loaded_students:
      print(f"{i['name']}:{i['score']}")
