from dotenv import load_dotenv 
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel
from langchain_groq import ChatGroq
import os

from ocr import extracted_text

ocr_text=extracted_text 

load_dotenv() 


model=ChatGroq(model="llama-3.1-8b-instant")


summarize_prompt=ChatPromptTemplate.from_messages([("system", "You are an AI model which summarizes a given passage of text"), ("human", "Summarize this: {text}")])

key_prompt=ChatPromptTemplate.from_messages([("system", "You are an AI model which specialises in pointing out the key entities from a passage of text"), ("human", "List out the key entities from this passage: {text}")])
    

summary_chain=(summarize_prompt | model | StrOutputParser())
key_chain= (key_prompt | model | StrOutputParser())

def combined(summary, key):
    return (f"Summary:\n{summary}\n\nKey entities:\n{key}")

chain=(RunnableParallel(branches={"Summary":summary_chain, "Key entities":key_chain}) | RunnableLambda(lambda x:combined(x["branches"]["Summary"], x["branches"]["Key entities"])))

result=chain.invoke({"text": ocr_text})
print(result)