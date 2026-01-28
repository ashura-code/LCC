<<<<<<< Updated upstream
=======
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


language_model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=GROQ_API_KEY,  # type:ignore
)


def call_llm(prompt: str) -> str:
    response = language_model.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content
>>>>>>> Stashed changes
