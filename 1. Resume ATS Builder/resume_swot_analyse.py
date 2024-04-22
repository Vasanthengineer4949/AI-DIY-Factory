# Importing the dependencies

import os
from crewai import Crew, Process
from dotenv import load_dotenv, find_dotenv # Groq, Serper
from langchain_groq import ChatGroq # Mixtral
from utils import *
from agents import agents
from tasks import tasks
load_dotenv(find_dotenv())

# Configuration
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Load the llm
llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0)

# Provided the inputs
resume = read_all_pdf_pages("data/resume.pdf")
job_desire = input("Enter Desiring Job: ")

# Creating agents and tasks
job_requirements_researcher, resume_swot_analyser = agents(llm)

research, resume_swot_analysis = tasks(llm, job_desire, resume)

# Building crew and kicking it off
crew = Crew(
    agents=[job_requirements_researcher, resume_swot_analyser],
    tasks=[research, resume_swot_analysis],
    verbose=1,
    process=Process.sequential
)

result = crew.kickoff()
print(result)


