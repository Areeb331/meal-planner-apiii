from flask import Flask, request, jsonify
from prompt_utils import build_dynamic_prompt
from openrouter_utils import call_openrouter_gpt
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/generate-meal-plan", methods=["POST"])
def generate_meal_plan():
    try:
        user_data = request.json
        prompt = build_dynamic_prompt(user_data)
        response = call_openrouter_gpt(prompt)
        return jsonify({"success": True, "meal_plan": response})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
