from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Check API key
if not api_key:
    print("WARNING: GEMINI_API_KEY was not found in .env")
else:
    print("API KEY LOADED: True")

# Create Gemini client
client = genai.Client(api_key=api_key)


@app.route("/", methods=["GET", "POST"])
def home():

    analysis = None
    headline = ""

    if request.method == "POST":

        # Get headline from HTML form
        headline = request.form.get("headline", "").strip()

        if not headline:
            analysis = "Please enter a news headline."

        else:

            prompt = f"""
You are an AI News Headline Analyzer.

Analyze ONLY the language of this news headline.

IMPORTANT:
- Do NOT say the news is definitely true.
- Do NOT say the news is definitely false.
- Do NOT determine whether the claim is factual.
- Analyze only the wording of the headline.
- Identify emotional language.
- Identify possible clickbait words or phrases.
- Identify warning signs.
- Suggest information that should be verified.
- Give a careful and neutral analysis.

Use this format:

Analysis:

Emotional Language:
Low / Medium / High

Clickbait Possibility:
Low / Medium / High

Warning Signs:
- ...
- ...
- ...

Things to Verify:
- Source of the news
- Author
- Date of publication
- Supporting evidence

Final Note:
The headline alone cannot determine whether the news is true or false.

Headline:
{headline}
"""

            try:

                print("Sending headline to Gemini...")

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )

                analysis = response.text

                print("Gemini analysis received successfully.")

            except Exception as error:

                print("================================")
                print("GEMINI API ERROR:")
                print(error)
                print("================================")

                analysis = """
Unable to analyze the headline right now.

Please check your Gemini API key and internet connection.
"""


    return render_template(
        "index.html",
        analysis=analysis,
        headline=headline
    )


if __name__ == "__main__":
    app.run(debug=True)