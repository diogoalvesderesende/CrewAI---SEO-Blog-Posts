from crewai import Agent, Task
from langchain_openai import ChatOpenAI

class WriterAgent:
    def __init__(self, llm: ChatOpenAI):
        self.llm = llm
        self._agent = None

    def create(self) -> Agent:
        self._agent = Agent(
            role='Content Writer',
            goal='Write engaging, SEO-optimized blog posts with clear visual content placement markers',
            backstory="""You are a professional content writer with expertise in creating 
            well-structured, engaging blog posts that follow SEO best practices and formatting guidelines.
            You understand how to effectively integrate visual content to enhance the reader's experience.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
        return self._agent

    def get_task(self, word_count: int, language: str) -> Task:
        if not self._agent:
            self.create()
            
        return Task(
            description=f"""
            Write a {word_count}-word blog post in {language} that:
            1. Uses proper heading hierarchy (H1 for title, H2 for main sections, H3 for subsections)
            2. Includes clear markers for visual content placement every 200 words using this format:
               [VISUAL_CONTENT_MARKER: Brief description of the content being discussed here]
            3. Is formatted for skimmability with short paragraphs and bullet points
            4. Prefer to use short paragraphs -1-2 sentences max - over bullet points.
            5. Naturally incorporates the main keyword and related terms
            6. Addresses common questions and user intent
            7. Follows SEO best practices
            
            Format the output in Markdown and ensure the visual content markers are placed at natural 
            breaks in the content where visuals would enhance understanding or engagement.
            """,
            expected_output=f"""A {word_count}-word SEO-optimized blog post in {language} with:
            1. Clear heading hierarchy
            2. Visual content placement markers
            3. Proper formatting and structure
            4. Integrated keywords and related terms
            5. Markdown formatting""",
            agent=self._agent
        ) 