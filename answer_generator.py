
from openai import OpenAI
from config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)
question = "how many holidays has Nitin Jiri taken last year"

def generate_natural_answer(question: str, sql_result):

    result_text = "\n".join([str(row) for row in sql_result])

    prompt = f"""
    You are a data analyst.

    Your task is to convert SQL query results into a clear and concise natural language answer.

    STRICT RULES:
    1. Base your answer ONLY on the SQL Result provided.
    2. Do NOT add assumptions or extra information.
    3. Do NOT explain the SQL.
    4. Be concise and professional.
    5. If the result is empty, respond with:
    "No data found for the given query."
    6. If the result contains numeric aggregates (SUM, COUNT, AVG, etc.), clearly state the final value.
    7. If multiple rows are returned, summarize them clearly in readable format.

    User Question:
    {question}

    SQL Result:
    {result_text}

    Return only the final natural language answer. Answer should be very precise. Not explanatory.

    """

    response = client.chat.completions.create(
        model=settings.CHAT_MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()

