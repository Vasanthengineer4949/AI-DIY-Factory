from crewai import Crew, Process

from agents import YoutubeAutomationAgents
from tasks import YoutubeAutomationTasks
from tools.youtube_video_details_tool import YoutubeVideoDetailsTool
from tools.youtube_video_search_tool import YoutubeVideoSearchTool
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os
load_dotenv()

manager_llm = ChatOpenAI(
    name="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

agents = YoutubeAutomationAgents()
tasks = YoutubeAutomationTasks()

youtube_video_search_tool = YoutubeVideoSearchTool()
youtube_video_details_tool = YoutubeVideoDetailsTool()

youtube_manager = agents.youtube_manager()
research_manager = agents.research_manager(
    youtube_video_search_tool, youtube_video_details_tool)

video_topic = "Crew AI Crash Course - Beginner Friendly to Build your Own Agents"
video_details = """
In this video, we're diving into crewAI framework which has different number of components like Agent, Task, Crew and many more. This is a beginner friendly step by step course for us to explore the CrewAI framework which enables us to build multi agent environment and automate many of our day to day task
"""

manage_youtube_video_creation = tasks.manage_youtube_video_creation(
    agent=youtube_manager,
    video_topic=video_topic,
    video_details=video_details
)
manage_youtube_video_research = tasks.manage_youtube_video_research(
    agent=research_manager,
    video_topic=video_topic,
    video_details=video_details,
)

# Create a new Crew instance
crew = Crew(
    agents=[youtube_manager,
            research_manager
            ],
    tasks=[manage_youtube_video_creation,
           manage_youtube_video_research],
    process=Process.hierarchical,
    manager_llm=manager_llm
)

# Kick of the crew
results = crew.kickoff()

print("Crew usage", crew.usage_metrics)

print("Crew work results:")
print(results)