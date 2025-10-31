import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model_name = 'gemini-2.0-flash-001'

    prompt = sys.argv[1]
    is_verbose = '--verbose' in sys.argv

    messages = [
        genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)]),
        ]

    response = client.models.generate_content(model=model_name, contents=messages)
    print(response.text)

    if is_verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
