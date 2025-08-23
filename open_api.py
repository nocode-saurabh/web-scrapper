import openai
from prompt import city_fact_prompt
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
def open_api_call(content:str)->str:
    prompt=messages_for(content)
    response = openai.chat.completions.create(
        model = "gpt-4.1",
        messages=[
            {"role": "system", "content": prompt["system_prompt"]},
            {"role": "user", "content": prompt["user_prompt"].format(website=content)}
        ]   )
    return response.choices[0].message.content
def messages_for(content: str):
    city_fact_prompt = {
        "system_prompt": "You are a helpful assistant that generates concise and interesting facts about cities. Your task is to analyze the provided content about a city and generate exactly 10 key facts that best represent the city's unique characteristics, history, culture, and significance. Follow these guidelines:\n\n1. Each fact should be clear, concise, and self-contained\n2. Focus on unique and distinctive aspects of the city\n3. Include a mix of:\n   - Historical facts\n   - Cultural significance\n   - Economic importance\n   - Geographical features\n   - Modern developments\n4. Avoid repetitive information\n5. Present facts in a numbered list format\n6. Keep each fact to 1-2 sentences\n7. Use present tense for current facts and past tense for historical facts\n8. Prioritize accuracy and verifiable information\n9. Exclude opinions or subjective statements\n10. Format each fact to start with 'Fact #: '\n\nExample format:\nFact 1: [Clear, concise statement about the city]\nFact 2: [Another interesting fact]\n[...and so on until Fact 10]",
        "user_prompt": "Based on the following content identify the city name from it, generate exactly 10 most interesting and important facts about the city:\n\n{website}\n\nPlease present the facts in a numbered list, focusing on the most significant and unique aspects of the city.",
        "example_output": {
            "format": [
                "Fact 1: The city serves as the capital of Maharashtra's Vidarbha region.",
                "Fact 2: Founded in the 18th century, the city was established by the Gond King Bakht Buland Shah.",
                "Fact 3: The city is known for its orange cultivation, earning it the nickname 'Orange City'.",
                "[...continue until Fact 10]"
            ]
        }
    }
    return city_fact_prompt