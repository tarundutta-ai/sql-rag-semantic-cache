import os
import csv
from schema_loader import get_schema_metadata
from semantic_caching import SemanticSQLCache
from sql_generator import generate_sql
from database import fetch_data
from answer_generator import generate_natural_answer
from config import settings
from datetime import datetime
from zoneinfo import ZoneInfo
vector_cache = SemanticSQLCache()
session_memory = []


def ask_question(question: str):
    global session_memory

    print(" Checking semantic cache...")
    
    cache = vector_cache.search(question)
    if cache:
        print(" Reusing SQL from semantic cache")
        sql_query = cache["sql"]

    else: 

        print(" Loading schema...")
        tool = "sql_tool"
        schema = get_schema_metadata()
        print(" Generating SQL...")
        sql_query = generate_sql(question, schema, session_memory)
        vector_cache.add(question, sql_query)
    print(" Fetching SQL Result...")
    result = fetch_data(sql_query)
    print(" Generating answer...")
    answer = generate_natural_answer(question, result)
    print(answer)
    # ---- Update session memory ----
    session_memory.append({
        "question": question,
        "answer": answer
    })
    # Keep only last 5
    session_memory = session_memory[-5:]
    now = datetime.now()
    date_str = now.strftime("%d-%m-%Y") #"%d-%m-%Y"
    time_str = now.strftime("%H:%M:%S")
    #tz_str = settings.TIMEZONE
    file_exists = os.path.isfile(settings.LOG_FILE_PATH)
    with open(settings.LOG_FILE_PATH, mode='a', newline= "") as file:
        writer =csv.writer(file)
        if not file_exists:
            writer.writerow([settings.LOG_HEADER])
        writer.writerow([date_str,time_str, question,"SQL", sql_query, answer]) # Replace the tool with the actual tool



if __name__ == "__main__":
    while True:
        q = input("\nAsk a question: ")
        ask_question(q)