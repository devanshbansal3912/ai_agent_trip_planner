from crewai import Agent
from textwrap import dedent
from langchain_openai import OpenAI  
from langchain_ollama import OllamaLLM as Ollama  
from langchain_openai import ChatOpenAI

from tools import search_tools
from tools.search_tools import SearchTools
from tools.calculator_tools import calculate

'''
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee
   you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal.
- Define which experts the captain needs to communicate with and delegate tasks to.
  Build a top down structure of the crew.

Goal:
- Create a 7-day travel iterary with detailed per day plans,
    including budget, packing suggestions and safety tips.


Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert
- Local Tour Guide



Notes: 
- Agents should be results driven and have a clear goal in mind 22
- Role is their job title 23
- Goals should actionable
- Backstory should be their resume
'''


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics.
                            I have decades of experience making travel iternaries."""),
            goal=dedent(f"""
                        Create a 7-day travel iterary with detailed per day plans, including budget,
                        packing suggestions and safety tips.
                         """),
            tools=[
                SearchTools.search_internet,
                calculate
            ],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations."""),
            goal=dedent(
                f"""Select the best city based on weather, season, prices, and travel interests."""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    
    def local_tour_guide(self):
        return Agent(
            role="local tour guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information about the city, it's attractions and customs."""),
            goal=dedent(f"""Provide BEST insights about the selected city"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )