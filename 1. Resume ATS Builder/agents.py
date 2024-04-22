# Agents
# 1. Job Requirements Researcher
# 2. SWOT Analyser

## Importing the dependencies

from crewai import Agent
from crewai_tools import SerperDevTool, WebsiteSearchTool

search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

# Create agents which uses these tools

def agents(llm):
    '''
    Has two agents
    1. requirements_researcher - search_tool, web_rag_tool
    2. swot_analyser
    '''
    job_requirements_researcher = Agent(
                                            role='Market Research Analyst',
                                            goal='Provide up-to-date market analysis of industry job requirements of the domain specified',
                                            backstory='An expert analyst with a keen eye for market trends.',
                                            tools=[search_tool, web_rag_tool],
                                            verbose=True,
                                            llm=llm,
                                            max_iters=1
                                        )
    
    resume_swot_analyser = Agent(
                                    role='Resume SWOT Analyser',
                                    goal=f'Perform a SWOT Analysis on the Resume based on the industry Job Requirements report from job_requirements_researcher and provide a json report.',
                                    backstory='An expert in hiring so has a great idea on resumes',
                                    verbose=True,
                                    llm=llm,
                                    max_iters=1,
                                    allow_delegation=True
                            )
    return job_requirements_researcher, resume_swot_analyser


