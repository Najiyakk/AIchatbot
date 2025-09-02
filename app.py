from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Memory file location
MEMORY_FILE = "isro_memory.json"

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

# Load memory if exists
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
        keyword_to_answer.update(memory)
else:
    memory = {}

# Temporary state for teaching
teaching_state = {
    "waiting_for_answer": False,
    "waiting_for_keyword": False,
    "pending_answer": None
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json["question"].lower()
    found_answer = None

    # Check if any keyword matches
    for key, answer in keyword_to_answer.items():
        if key in user_question:  # substring match
            found_answer = answer
            break

    # If bot is waiting for an answer
    if teaching_state["waiting_for_answer"]:
        teaching_state["pending_answer"] = user_question
        teaching_state["waiting_for_answer"] = False
        teaching_state["waiting_for_keyword"] = True
        return jsonify({"answer": "🔑 Enter a keyword to trigger this answer:"})

    # If bot is waiting for a keyword
    if teaching_state["waiting_for_keyword"]:
        new_keyword = user_question
        new_answer = teaching_state["pending_answer"]

        # Save in memory
        keyword_to_answer[new_keyword] = new_answer
        memory[new_keyword] = new_answer
        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=4)

        # Reset teaching state
        teaching_state["waiting_for_keyword"] = False
        teaching_state["pending_answer"] = None
        return jsonify({"answer": "✅ Thanks! I’ve learned something new."})

    # Normal Q&A flow
    if found_answer:
        return jsonify({"answer": found_answer})
    else:
        teaching_state["waiting_for_answer"] = True
        return jsonify({"answer": "❓ Sorry, I don’t know that.\n👉 Please tell me the correct answer:"})


if __name__ == "__main__":
    app.run(debug=True)
