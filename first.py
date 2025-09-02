print("Hello AI Help Bot!")

year = 1969
org = "ISRO"
print("The year ISRO was founded:", year)
print("Organization:", org)

missions = ["Chandrayaan", "Mangalyaan", "Aditya-L1"]
print(missions[0])   # prints first mission

qa={
     "When was ISRO founded?": "1969",
    "What does PSLV stand for?": "Polar Satellite Launch Vehicle",
    "Which rocket carried Chandrayaan?": "GSLV Mk III"
}
print(qa["When was ISRO founded?"])

year = 1969
if year == 1969:
    print("Correct! ISRO was founded in 1969.")
else:
    print("Wrong year!")

for mission in missions:
    print("Mission:", mission)

q={
    
 "When was ISRO founded?": "1969",
    "What does PSLV stand for?": "Polar Satellite Launch Vehicle",
    "Which rocket carried Chandrayaan?": "GSLV Mk III"
}
question=input("ask me about");
print(qa.get(question,"sorry"))


qa = {
    "isro founded": "ISRO was founded in 1969.",
    "pslv": "PSLV stands for Polar Satellite Launch Vehicle.",
    "chandrayaan rocket": "Chandrayaan was launched using GSLV Mk III."
}
question = input("Ask me about ISRO: ").lower()


found = False
for key in qa:   # check each keyword
    if key in question:   # if keyword matches inside user input
        print(qa[key])
        found = True
        break

if not found:
    print("Sorry, I don’t know.")



#improved
# Q&A with multiple keywords per answer


qa = {
    ("isro founded", "established", "started"): "ISRO was founded in 1969.",
    ("pslv", "polar satellite launch vehicle"): "PSLV stands for Polar Satellite Launch Vehicle.",
    ("chandrayaan", "moon mission", "chandrayaan rocket"): "Chandrayaan was launched using GSLV Mk III."
}

while True:
    question = input("Ask me about ISRO (or type 'exit' to quit): ").lower()
    if question == "exit":
        print("Goodbye!")
        break

    found = False
    for keywords, answer in qa.items():
        for key in keywords:
            if key in question:   # <-- checks if keyword is *inside* question
                print(answer)
                found = True
                break
        if found:
            break

    if not found:
        print("Sorry, I don’t know.")


#spelling mistake
import difflib

qa = {
    ("isro founded", "established", "started"): "ISRO was founded in 1969.",
    ("pslv", "polar satellite launch vehicle"): "PSLV stands for Polar Satellite Launch Vehicle.",
    ("chandrayaan", "moon mission", "chandrayaan rocket"): "Chandrayaan was launched using GSLV Mk III.",
    ("gaganyaan", "human space mission", "astronauts"): "Gaganyaan is India’s human spaceflight program.",
    ("mars mission", "mangalyaan", "mom"): "Mangalyaan (Mars Orbiter Mission) was launched in 2013."
}

# Flatten keywords
all_keywords = []
keyword_to_answer = {}

for keywords, answer in qa.items():
    for key in keywords:
        all_keywords.append(key)
        keyword_to_answer[key] = answer

while True:
    question = input("Ask me about ISRO (or type 'exit' to quit): ").lower()
    if question == "exit":
        print("Goodbye!")
        break

    # Find closest keyword (tolerance = 0.6)
    matches = difflib.get_close_matches(question, all_keywords, n=1, cutoff=0.6)

    if matches:
        best_match = matches[0]
        print(keyword_to_answer[best_match])
    else:
        print("Sorry, I don’t know.")



#by adding did you mean
import difflib

qa = {
    ("isro founded", "established", "started"): "ISRO was founded in 1969.",
    ("pslv", "polar satellite launch vehicle"): "PSLV stands for Polar Satellite Launch Vehicle.",
    ("chandrayaan", "moon mission", "chandrayaan rocket"): "Chandrayaan was launched using GSLV Mk III.",
    ("gaganyaan", "human space mission", "astronauts"): "Gaganyaan is India’s human spaceflight program.",
    ("mars mission", "mangalyaan", "mom"): "Mangalyaan (Mars Orbiter Mission) was launched in 2013."
}

# Flatten keywords
all_keywords = []
keyword_to_answer = {}

for keywords, answer in qa.items():
    for key in keywords:
        all_keywords.append(key)
        keyword_to_answer[key] = answer

while True:
    question = input("Ask me about ISRO (or type 'exit' to quit): ").lower()
    if question == "exit":
        print("Goodbye!")
        break

    # Get top 3 close matches (instead of just 1)
    matches = difflib.get_close_matches(question, all_keywords, n=3, cutoff=0.5)

    if matches:
        # If the best match is very confident (≥ 0.8), just answer directly
        if difflib.SequenceMatcher(None, question, matches[0]).ratio() >= 0.8:
            print(keyword_to_answer[matches[0]])
        else:
            print("Did you mean:")
            for i, match in enumerate(matches, 1):
                print(f"{i}. {match}")

            choice = input("Enter the number (or press Enter to skip): ")
            if choice.isdigit() and 1 <= int(choice) <= len(matches):
                print(keyword_to_answer[matches[int(choice)-1]])
            else:
                print("Okay, skipping this one.")
    else:
        print("Sorry, I don’t know.")




#by using memeory
import difflib

# Knowledge base
qa = {
    ("isro founded", "established", "started"): "ISRO was founded in 1969.",
    ("pslv", "polar satellite launch vehicle"): "PSLV stands for Polar Satellite Launch Vehicle.",
    ("chandrayaan", "moon mission", "chandrayaan rocket"): "Chandrayaan was launched using GSLV Mk III.",
    ("gaganyaan", "human space mission", "astronauts"): "Gaganyaan is India’s human spaceflight program.",
    ("mars mission", "mangalyaan", "mom"): "Mangalyaan (Mars Orbiter Mission) was launched in 2013."
}

# Flatten keywords
all_keywords = []
keyword_to_answer = {}

for keywords, answer in qa.items():
    for key in keywords:
        all_keywords.append(key)
        keyword_to_answer[key] = answer

# Memory for user corrections
memory = {}

while True:
    question = input("Ask me about ISRO (or type 'exit' to quit): ").lower()
    if question == "exit":
        print("Goodbye!")
        break

    # ✅ If user already taught the bot before
    if question in memory:
        print(memory[question])
        continue

    # Find close matches
    matches = difflib.get_close_matches(question, all_keywords, n=3, cutoff=0.5)

    if matches:
        # High confidence → direct answer
        if difflib.SequenceMatcher(None, question, matches[0]).ratio() >= 0.8:
            print(keyword_to_answer[matches[0]])
        else:
            # Suggest options
            print("Did you mean:")
            for i, match in enumerate(matches, 1):
                print(f"{i}. {match}")

            choice = input("Enter the number (or press Enter to skip): ")
            if choice.isdigit() and 1 <= int(choice) <= len(matches):
                selected = matches[int(choice)-1]
                answer = keyword_to_answer[selected]
                print(answer)

                # ✅ Save in memory (so bot remembers next time)
                memory[question] = answer
            else:
                print("Okay, skipping this one.")
    else:
        print("Sorry, I don’t know.")
#permanent memory file
import difflib
import json
import os

# Knowledge base
qa = {
    ("isro founded", "established", "started"): "ISRO was founded in 1969.",
    ("pslv", "polar satellite launch vehicle"): "PSLV stands for Polar Satellite Launch Vehicle.",
    ("chandrayaan", "moon mission", "chandrayaan rocket"): "Chandrayaan was launched using GSLV Mk III.",
    ("gaganyaan", "human space mission", "astronauts"): "Gaganyaan is India’s human spaceflight program.",
    ("mars mission", "mangalyaan", "mom"): "Mangalyaan (Mars Orbiter Mission) was launched in 2013."
}

# Flatten keywords
all_keywords = []
keyword_to_answer = {}

for keywords, answer in qa.items():
    for key in keywords:
        all_keywords.append(key)
        keyword_to_answer[key] = answer

# File for memory
memory_file = "memory.json"

# Load memory if exists
if os.path.exists(memory_file):
    with open(memory_file, "r") as f:
        memory = json.load(f)
else:
    memory = {}

while True:
    question = input("Ask me about ISRO (or type 'exit' to quit): ").lower()
    if question == "exit":
        # Save memory before exiting
        with open(memory_file, "w") as f:
            json.dump(memory, f)
        print("Goodbye! Memory saved ✅")
        break

    # ✅ If user already taught the bot before
    if question in memory:
        print(memory[question])
        continue

    # Find close matches
    matches = difflib.get_close_matches(question, all_keywords, n=3, cutoff=0.5)

    if matches:
        # High confidence → direct answer
        if difflib.SequenceMatcher(None, question, matches[0]).ratio() >= 0.8:
            print(keyword_to_answer[matches[0]])
        else:
            # Suggest options
            print("Did you mean:")
            for i, match in enumerate(matches, 1):
                print(f"{i}. {match}")

            choice = input("Enter the number (or press Enter to skip): ")
            if choice.isdigit() and 1 <= int(choice) <= len(matches):
                selected = matches[int(choice)-1]
                answer = keyword_to_answer[selected]
                print(answer)

                # ✅ Save in memory (so bot remembers next time)
                memory[question] = answer
            else:
                print("Okay, skipping this one.")
    else:
        print("Sorry, I don’t know.")
