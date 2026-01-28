from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

API_KEY = "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"

language_model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=API_KEY,
)


def call_llm(prompt: str) -> str:
    return language_model.invoke([HumanMessage(content=prompt)]).content
