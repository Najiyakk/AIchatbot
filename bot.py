import json
import os

# Memory file location (you can change this path if needed)
MEMORY_FILE = r"C:\Users\hp\Desktop\AIchatbot\isro_memory.json"

# Default knowledge base
qa = {
    ("isro founded", "established", "started"): "ISRO was founded in 1969.",
    ("pslv", "polar satellite launch vehicle"): "PSLV stands for Polar Satellite Launch Vehicle.",
    ("chandrayaan", "moon mission", "chandrayaan rocket"): "Chandrayaan was launched using GSLV Mk III.",
    ("gaganyaan", "human space mission", "astronauts"): "Gaganyaan is India’s human spaceflight program.",
    ("mars mission", "mangalyaan", "mom"): "Mangalyaan (Mars Orbiter Mission) was launched in 2013."
}

# Flatten keywords for quick lookup
keyword_to_answer = {}
for keywords, answer in qa.items():
    for key in keywords:
        keyword_to_answer[key] = answer

# Load memory if it exists
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
        keyword_to_answer.update(memory)
else:
    memory = {}

while True:
    question = input("Ask me about ISRO (or type 'exit' to quit): ").lower()
    if question == "exit":
        print("Goodbye!")
        break

    found_answer = None

    # Check if any keyword is a substring of the question
    for key, answer in keyword_to_answer.items():
        if key in question:   # substring match
            found_answer = answer
            break

    if found_answer:
        print(found_answer)
    else:
        print("❓ Sorry, I don’t know that.")
        teach = input("Do you want to teach me? (yes/no): ").lower()
        if teach == "yes":
            new_answer = input("👉 Please tell me the correct answer: ")
            new_keyword = input("🔑 Enter a keyword to trigger this answer: ").lower()
            
            # Save to memory
            keyword_to_answer[new_keyword] = new_answer
            memory[new_keyword] = new_answer
            
            with open(MEMORY_FILE, "w") as f:
                json.dump(memory, f, indent=4)
            
            print("✅ Thanks! I’ve learned something new.")
