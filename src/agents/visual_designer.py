from crewai import Agent, Task
from langchain_openai import ChatOpenAI

class VisualDesignerAgent:
    def __init__(self, llm: ChatOpenAI):
        self.llm = llm
        self._agent = None

    def create(self) -> Agent:
        self._agent = Agent(
            role='Visual Content Designer',
            goal='Create engaging and relevant visual content suggestions for blog posts',
            backstory="""You are a creative visual content designer with expertise in 
            creating engaging memes, infographics, and visual content that resonates with 
            audiences while maintaining professional standards and brand consistency. 
            You understand viral content, design principles, and how to convey complex 
            information through visuals.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
        return self._agent

    def get_task(self, language: str) -> Task:
        if not self._agent:
            self.create()
            
        return Task(
            description=f"""
            Analyze the blog post content and create visual content suggestions every 200 words. For each suggestion:

            1. Identify the key concept or message to visualize
            2. Propose multiple types of visuals:
               - Meme concept (if appropriate for the content)
               - Infographic layout and elements
               - Custom graphic or illustration description
               - Stock photo requirements and mood
               - Data visualization (if applicable)
            
            For each visual suggestion, provide:
            1. Detailed description in {language}
            2. Style and tone recommendations
            3. Key elements to include
            4. Text overlay suggestions (if applicable)
            5. Color scheme recommendations
            6. Estimated dimensions/aspect ratio
            
            Format each suggestion in Markdown with clear sections and maintain professional standards.
            Make sure all visual suggestions align with the content's tone and purpose.
            """,
            expected_output=f"""A comprehensive visual content plan in {language} containing:
            1. 2 visual suggestions for each content section
            2. Detailed specifications for each visual
            3. Style and design recommendations
            4. Technical requirements
            5. Placement guidelines""",
            agent=self._agent
        ) 