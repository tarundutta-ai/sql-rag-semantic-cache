from openai import OpenAI
from config import settings
from schema_loader import get_schema_metadata

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_sql(question, schema, memory):

    memory_text = ""

    if memory:
        memory_text = "Previous Conversation:\n"
        for item in memory:
            memory_text += f"Q: {item['question']}\n"
            memory_text += f"A: {item['answer']}\n\n"


    prompt = f"""
    You are a senior Microsoft SQL Server expert.

    Your task is to generate a syntactically correct, executable SQL Server query.

    STRICT RULES:
    1. Generate ONLY a valid T-SQL query.
    2. Do NOT include explanations.
    3. Do NOT include markdown.
    4. Do NOT include comments.
    5. Do NOT include backticks.
    6. Only generate SELECT statements. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE.
    7. Always limit results to TOP 100 unless the user explicitly asks for all records.
    8. Use fully qualified column names when joins are involved.
    9. Use proper JOIN conditions based ONLY on the schema provided.
    10. Never assume columns that are not present in the schema.
    11. If aggregation is used, ensure proper GROUP BY clauses.
    12. If the question cannot be answered using the schema, return:
    SELECT 'Insufficient schema information to answer the question' AS Message

    I have also provided you the previous discussions. You could refer, if you find relevant with the questions, else ignore

    {memory_text}

    DATABASE SCHEMA:
    {schema}

    IMPORTANT
    Refertial integrity not maintained properly. You apply your own logic, and join the table based upon the common columns. 
    Find out Primary key, and Foreign key by yourself, and join the tables if require

    USER QUESTION:
    {question}

    Return ONLY the SQL query.
    """

    response = client.chat.completions.create(
        model=settings.CHAT_MODEL,
        messages=[
            {"role": "system", "content": "You generate SQL queries only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


