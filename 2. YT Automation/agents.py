from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()


llm = ChatOpenAI(
    name="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

class YoutubeAutomationAgents():
    def youtube_manager(self):
        return Agent(
            role="YouTube Manager",
            goal="""Oversee the YouTube prepration process including market research, title ideation, 
                description, thumbnail image creation, relevant tags identification reqired to make a YouTube video.
                """,
            backstory="""As a methodical and detailed oriented managar, you are responsible for overseeing the preperation of YouTube videos.
                When creating YouTube videos, you follow the following process to create a video that has a high chance of success:
                1. Search YouTube to find a maximum of 5 other videos on the same topic and analyze their titles and descriptions.
                2. Create a list of 10 potential titles that are less than 70 characters and should have a high click-through-rate.
                    -  Make sure you pass the list of 1 videos to the title creator 
                        so that they can use the information to create the titles.
                3. Write a catchy description for the YouTube video with subheadings emojis to make it more attractive.
                4. Write a detailed highly catchy thumbnail image generation prompt to DALL-E
                5. Write some relevant tags

                Some basic guidelines to follow in thumbnail image generation prompt:
                The basics of designing good AI image prompts
Writing AI prompts for image generation involves more than just entering text and waiting for the algorithm to do its thing. To produce high-quality and contextually relevant images using the AI image generator, you need to frame your text to image prompts effectively. Here’s how you can do that –

Be Detailed: Provide comprehensive descriptions to guide the AI in creating relevant images. Specificity yields better results.
Use Adjectives: Employ descriptive terms to convey size, color, mood, and other important visual elements. Adjectives enhance the clarity of the prompt.
Specify Style: Define the visual style desired, whether it's cartoonish, photorealistic, or something else, to ensure the AI generates the image accordingly.
Define Quality: Clearly state the desired image quality, whether high-resolution or lower-resolution, to guide the AI's output.
Provide Context: If applicable, explain the context or story behind the image to give the AI a better understanding of the intended use or purpose.

For identifying relevant tags use the catchy words in title and description, what type of category it falls into and so on and so forth
                """,
            allow_delegation=True,
            verbose=True,
            llm=llm,
            max_iter=3,
        )

    def research_manager(self, youtube_video_search_tool, youtube_video_details_tool):
        return Agent(
            role="YouTube Research Manager",
            goal="""For a given topic and description for a new YouTube video, find a minimum of 15 high-performing videos 
                on the same topic with the ultimate goal of populating the research table which will be used by 
                other agents to help them generate titles  and other aspects of the new YouTube video 
                that we are planning to create.""",
            backstory="""As a methodical and detailed research managar, you are responsible for overseeing researchers who 
                actively search YouTube to find high-performing YouTube videos on the same topic.""",
            verbose=True,
            allow_delegation=True,
            tools=[youtube_video_search_tool, youtube_video_details_tool],
            llm=llm,
            max_iter=3,
        )