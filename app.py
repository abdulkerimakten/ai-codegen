from flask import Flask, request, render_template
from llm_client import generate_code_from_prompt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    title, code = "", ""

    if request.method == "POST":
        # Get the prompt entered by the user
        user_prompt = request.form["prompt"]
        
        # Generate title and code based on the prompt
        title, code = generate_code_from_prompt(user_prompt)

    # Render the template with the generated title and code
    return render_template("index.html", title=title, code=code)
