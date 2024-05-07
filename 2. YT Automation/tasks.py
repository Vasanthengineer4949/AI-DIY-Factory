from functools import partial
from crewai import Task
from textwrap import dedent


class YoutubeAutomationTasks():

    def manage_youtube_video_creation(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""Oversee the YouTube prepration process including market research, title ideation, 
                description creation, thumbnail idea creation and relevant tags reqired to make a YouTube video. The ultimate goal is for you to generate 
                a report including a research table, potential high click-through-rate titles, 
                a rewritten YouTube video description based on the given description, a highly catchy thumbnail image generation prompt which shows about the background, color scheme, elements in image and so on and so forth that is detailed enough to give to DALL-E and some highly relevant tags to the video. It is important to have a detailed thumbnail image generation prompt.
                
                               
                The video topic is: {video_topic}
                The video details are: {video_details}  

                Here is an example report that you can use as a template:
                - It is important to note that the example report only contains 2 videos, 
                    but the final report should contain 15 videos.
                - It is important to note that the example report only contains 3 potential high CTRO titles,
                     but the final report should contain 10 titles. When writing titles make sure there is an emotion experessed in it like curiosity or excitment or fear/horror or sadness and so on and so forth             
                
                Example Report:
                # YouTube Competition Research Table:
                - Video 1:
                    - Title: "How to Make a YouTube Video"
                    - View Count: 100,000
                    - Days Since Published: 30
                    - Channel Subscriber Count: 1,000
                    - Video URL: https://www.youtube.com/watch?v=1234
                - Video 2:
                    - Title: "How to Make a YouTube Video"
                    - View Count: 100,000
                    - Days Since Published: 30
                    - Channel Subscriber Count: 1,000
                    - Video URL: https://www.youtube.com/watch?v=1234

                ...
                                    
                # Potential High CTRO Titles:
                - How to Make a YouTube Video
                - How to Make a YouTube Video in 2021
                - How to Make a YouTube Video for Beginners
                [THE REST OF THE POTENTIAL HIGH CTRO TITLES GO HERE]
                        
                # YouTube Video Description:

                Ready to lead an AI revolution? Watch and learn how to build your own CrewAI from the ground up using the latest CrewAI features, and get set to deploy an army of AI agents at your command. This video is your ultimate guide to creating a powerful digital workforce, enhancing your projects with intelligent automation and streamlined workflows. Discover the secrets to customizing AI agents, setting them on tasks, and managing a smooth operation with CrewAI. It’s time to amplify your tech capabilities, and after this tutorial, you'll be equipped to engineer an AI crew that transforms any complex challenge into a simple task. Start your journey to AI mastery with CrewAI today!
                [REWRITTEN HIGHLY CATCHY DESCRIPTION - WITH SUBHEADINGS]

                🤖 Download the CrewAI Source Code Here:
                https://github.com/Vasanthengineer4949/AI-DIY-Factory

                Don't forget to Like and Subscribe if you're a fan of free source code 😉

                📰 Stay updated with my latest projects and insights:
                LinkedIn: https://www.linkedin.com/in/vasanthengineer4949/

                # Thumbnail idea:
                [DETAILED IMAGE GENERATION PROMPT FOR A YOUTUBE THUMBNAIL IMAGE BASED ON THE VIDEO TITLE AND DESCRIPTION TO GIVE TO DALL-E]

                # Relevant tags:
                [FILL RELEVANT TAGS]
            """),
            agent=agent,
            output_file="output/YouTube_Video_Creation_Report.txt",
            expected_output=dedent(f"""
                Generate a report that is formatted exactly like the example report provided to you earlier.
                Make sure the report contains 15 videos, 10 potential high CTRO titles, a YouTube video descriptioN
                The researched video should have all the required details and valid URLs.
            """)
        )

    def manage_youtube_video_research(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""For a given video topic and description, search youtube videos to find 
                15 high-performing YouTube videos on the same topic. Once you have found the videos, 
                research the YouTube video details to finish populate the missing fields in the 
                research CSV. When delegating tasks to other agents, make sure you include the 
                URL of the video that you need them to research.
                            
                This research CSV which will be used by other agents to help them generate titles 
                and other aspects of the new YouTube video that we are planning to create.
                               
                Research CSV Outline:
                - Title of the video
                - View count
                - Days since published
                - Channel subscriber count
                - Video URL
                       
                The video topic is: {video_topic}
                The video details is: {video_details}

                Important Notes: 
                - Make sure the CSV uses ; as the delimiter
                - Make sure the final Research CSV Outline doesn't contain duplicate videos
                - It is SUPER IMPORTANT that you properly match up view counts, subscriber counts, 
                    and everything else to the video URL.
                - It is SUPER IMPORTANT that you only populate the research CSV with real YouTube videos 
                    and YouTube URLs that actually link to the YouTube Video.
                """),
            agent=agent,
            expected_output=dedent(f"""
                Video Title; View Count; Days Since Published; Channel Subscriber Count; Video URL
                How to Make a YouTube Video; 100,000; 30; 1,000; https://www.youtube.com/watch?v=1234;
                How to Get Your First 1000 Subscribers; 100,000; 30; 1,000; https://www.youtube.com/watch?v=1234;
                       ...              
                """)
        )