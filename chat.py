import os
from dotenv import load_dotenv
from google import genai

load_dotenv() 
gemini_api_key = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=gemini_api_key)

def get_gemini_response(contents: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=contents,
    )
    return response.text

def process_transformation_prompt(prompt: str) -> str:
    query_count = 1
    history = []
    processed_prompt = prompt
    while query_count <= 5:
        if query_count > 1:
            prompt_with_history = (
                "Chat history:\n" +
                "\n".join(history) +
                f"\n\nCurrent transformation instructions: '{processed_prompt}'"
            )
        else:
            prompt_with_history = processed_prompt

        full_prompt = (
            "This is a transformation prompt for creating a new column in a CSV file. "
            "The CSV already contains existing columns. The values in the new column should be generated "
            f"based on the following transformation instructions: '{prompt_with_history}'. "
            "Are you clear on this transformation prompt? Please respond with 'Okay' if clear, or specify what is unclear."
        )

        ai_response = get_gemini_response(full_prompt)
        print(f'Gemini AI: {ai_response}')
        history.append(f"User: {processed_prompt}")
        history.append(f"Gemini AI: {ai_response}")

        user_input = input("Are you happy with your transformation command? (y/n): ").strip().lower()
        if user_input == 'y':
            break
        elif user_input == 'n':
            processed_prompt = input("Please refine your transformation command: ").strip()
            query_count += 1
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    # Ask Gemini to generate a short and simple transformation prompt for the new column description
    description_prompt = (
        f"Given the following transformation instructions: '{processed_prompt}', "
        "please return a short and simple description that can be used as the new column's description in a CSV file. "
        "The description should be clear and concise, summarizing the transformation."
    )
    processed_prompt = get_gemini_response(description_prompt)
    return processed_prompt
