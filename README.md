# AI News Headline Analyzer

## Project Overview
AI News Headline Analyzer is a web application that examines news headlines for subjective language, sensational wording, and possible clickbait. It also provides warning signs and suggestions for verifying news.

## Features
- Analyze the wording of a news headline.
- Identify subjective or sensational expressions.
- Highlight missing contextual details.
- Suggest information to verify, including the source, author, publication date, and supporting evidence.
- Display the analysis in a simple web interface.

## Example
**Input:**

India wins the cricket final after an exciting last-over finish.

**Example observations:**
- Identifies "exciting" as a subjective descriptor.
- Notes that the headline does not specify the tournament, opponent, or official score.
- Recommends checking the source, author, publication date, and supporting evidence.

## Technologies Used
- Python
- Flask
- HTML
- CSS

## How to Run Locally
1. Clone or download this repository.
2. Install the required dependencies:

   `pip install -r requirements.txt`

3. Configure any required environment variables in a local `.env` file.
4. Run the application:

   `python app.py`

5. Open `http://127.0.0.1:5000/` in your browser.

## Important Note
This application analyzes headline wording and suggests verification steps. It does not independently determine whether a news story is true or false. Always check reliable sources and supporting evidence.

## Security
Do not upload `.env` files, API keys, or other secrets to GitHub.