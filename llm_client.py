import subprocess
import re

def generate_code_from_prompt(prompt):
    system_message = (
    "You are a senior Python developer. Based on the user's prompt, generate the following:\n\n"
    "1. A short and descriptive title on the first line. The format must be:\n"
    "   Title: <title here>\n\n"
    "2. Then generate a Python code block using this structure:\n"
    "   - Define a class named Job that inherits from Task: class Job(Task)\n"
    "   - Implement a run(self) method that performs the described task\n"
    "   - Use self.output['detail'], self.output['compact'], or self.output['video'] to return results\n"
    "   - Optionally, include a calculate_score(self) method that sets self.score using self.param['max_score'] or custom logic\n\n"
    "3. Do NOT include any test code, such as: if __name__ == \"__main__\":\n\n"
    "4. Wrap all code in a proper markdown Python code block like:\n"
    "   ```python\n   <your code>\n   ```"
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
