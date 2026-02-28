##  Contact

**Tarun Dutta**  
Email: tarundutta.ai@gmail.com 
LinkedIn: https://www.linkedin.com/in/tarun-dutta-7b213b23/ 


#  SQL Server RAG Pipeline with Semantic Caching

This project demonstrates an end-to-end Retrieval-Augmented Generation (RAG) system over structured SQL Server data using OpenAI GPT models.

##  Features

- Natural language to SQL generation using LLM
- SQL execution against SQL Server
- Natural language answer generation
- Semantic caching using FAISS
- Short-term conversational memory (last 5 interactions)
- Logging system
- Modular architecture

---

##  Architecture

User Question  
→ Semantic Cache (FAISS)  
→ GPT SQL Generator  
→ SQL Server  
→ Natural Language Response  

---

##  Project Structure

- `main.py` – Entry point
- `sql_generator.py` – Converts question to SQL
- `answer_generator.py` – Converts result to natural answer
- `semantic_caching.py` – FAISS semantic cache
- `database.py` – SQL Server connection
- `schema_loader.py` – Schema extraction
- `config.py` – Configuration settings

---
###  Clone the repository


##  Setup Instructions
#Rename .env.example file as .env
#Replace the value with real value whereever marked as change the value


Install dependencies
-- pip install -r requirements.txt

Then Run the below python file
-- python main.py



Then start asking questions.

---

## Example Questions

- Who are the supervisors? How many leaves they have availed in last quarter?
- Show attendance of supervisors
- Show total sales by region
- Now filter for 2024

---

##  Use Case

This system can be used for:

- Business intelligence
- Internal data assistant
- Enterprise analytics chatbot
- SQL automation

---

##  Tech Stack

- Python
- OpenAI GPT Model
- SQL Server
- FAISS

---

##  License

MIT License