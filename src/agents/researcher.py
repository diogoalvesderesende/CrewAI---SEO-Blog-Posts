from crewai import Agent, Crew, Process, Task
from langchain_openai import ChatOpenAI
from typing import List
from crewai_tools import SerperDevTool, WebsiteSearchTool

class ResearcherAgent:
    """Agent for SEO research and analysis"""

    def __init__(self):
        self.agents = []
        self.tasks = []

    def research_agent(self, keyword: str, language: str) -> Agent:
        """Create a research agent with tools."""
        return Agent(
            role='SEO Researcher',
            goal=f'Research and analyze top 5 search results for keyword "{keyword}" in {language}',
            backstory='You are an expert SEO researcher with vast experience in analyzing search results and identifying keyword patterns and content strategies.',
            verbose=True,
            allow_delegation=False,
            tools=[SerperDevTool(), WebsiteSearchTool()],
            llm=ChatOpenAI(temperature=0.7, model="gpt-4.1")
        )

    def research_task(self, keyword: str, language: str) -> Task:
        """Create a research task for analyzing search results."""
        return Task(
            description=f"""
            Analyze the top 5 Google search results for the keyword "{keyword}" in {language}.
            
            For each result:
            1. Extract how they use the main keyword
            2. Identify derived keywords and related terms
            3. Find questions and prepositions associated with the keyword
            
            Compile a detailed research report that includes:
            - Analysis of keyword usage in titles, headings, and content
            - List of derived keywords and their context
            - Common questions and prepositions found
            - Content structure patterns
            - SEO optimization insights
            
            The report should be comprehensive yet actionable.
            """,
            expected_output="""A detailed SEO research report containing:
            1. Analysis of top 5 search results
            2. Keyword usage patterns
            3. Related terms and phrases
            4. Common questions and prepositions
            5. Content structure insights
            6. SEO optimization recommendations""",
            agent=self.research_agent(keyword, language)
        )

    def create_crew(self, keyword: str, language: str) -> Crew:
        """Create a crew with the research agent and task."""
        agent = self.research_agent(keyword, language)
        task = self.research_task(keyword, language)
        
        return Crew(
            agents=[agent],
            tasks=[task],
            verbose=True
        )