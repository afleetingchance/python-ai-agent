import os
import sys
import config
from dotenv import load_dotenv
from google import genai
from functions.call_function import call_function, available_functions    

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)
    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        genai.types.Content(role="user", parts=[genai.types.Part(text=user_prompt)]),
    ]

    i = 0
    while True:
        i += 1
        if i > config.MAX_CHARS:
            print(f"Maximum iterations ({config.MAX_ITERS}) reached.")
            sys.exit(1)
        
        try:
            response = generate_ai_content(client, messages, verbose)
            if response:
                print('Final response:')
                print(response)
                break
        except Exception as e:
            print(f'Error with genai: {e}')

def generate_ai_content(client, messages, verbose):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=genai.types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=config.SYSTEM_PROMPT
        )
    )

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.candidates and len(response.candidates):
        for candidate in response.candidates:
            messages.append(candidate.content)

    if isinstance(response.function_calls, list) and len(response.function_calls) > 0:
        for call in response.function_calls:
            func_result = call_function(call, verbose)
            func_response = func_result.parts[0].function_response.response

            if not func_response:
                raise Exception(f'No function response from {call.name}')
            
            if verbose:
                print(f"-> {func_response}")

            messages.append(genai.types.Content(role="user", parts=[genai.types.Part(text=func_response)]))
    else:
        return response.text


if __name__ == "__main__":
    main()
