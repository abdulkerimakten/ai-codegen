import subprocess
import re

def generate_code_from_prompt(prompt):
    system_message = (
        "You are a senior Python developer. Based on the user request, generate:"
        "\n1. A short and meaningful title on the first line, starting with 'Title: '"
        "\n2. Then generate the Python code, inside a code block like:\n```python\n<code>\n```, you can add comments in the code if needed."
        "\n3. If the code is too long, split it into multiple code blocks, but keep the title in the first block."
    )

    # Run the Ollama command
    result = subprocess.run(
        ["ollama", "run", "codellama", f"{system_message}\n\n{prompt}"],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    output = result.stdout
    print("*********** MODEL RESPONSE: ***********\n", output)

    # Extract title and code
    title_match = re.search(r"(?i)title:\s*(.*)", output)
    code_match = re.search(r"```python\n(.*?)```", output, re.DOTALL)

    try:
        title = title_match.group(1).strip()
    except Exception as e:
        print("!!!!!!!!! Title extraction error:", e)
        title = "Title could not be extracted"

    try:
        code = code_match.group(1).strip()
    except Exception as e:
        print("!!!!!!!!! Code extraction error:", e)
        code = output

    return title, code
