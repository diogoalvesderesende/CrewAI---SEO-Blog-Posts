from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from src.agents.researcher import ResearcherAgent
from src.agents.writer import WriterAgent
from src.agents.visual_designer import VisualDesignerAgent
import os
import json
from datetime import datetime

class BlogCrew:
    def __init__(self, keyword: str, language: str, word_count: int):
        self.keyword = keyword
        self.language = language
        self.word_count = word_count
        self.llm = ChatOpenAI(
            model="gpt-4-turbo",
            temperature=0.7
        )
        self.output_dir = self._create_output_dir()

    def _create_output_dir(self) -> str:
        """Create output directory with timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = os.path.join("output", f"blog_{timestamp}")
        os.makedirs(output_dir, exist_ok=True)
        return output_dir

    def _save_output(self, output: str | tuple, filename: str):
        """Save output to a file"""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            if isinstance(output, tuple):
                # If it's a tuple, join the elements with newlines
                f.write('\n\n'.join(str(item) for item in output))
            else:
                f.write(str(output))

    def run(self):
        # Initialize agents
        researcher_agent = ResearcherAgent()
        writer_agent = WriterAgent(self.llm)
        visual_designer_agent = VisualDesignerAgent(self.llm)

        # Create agents and get their tasks
        researcher = researcher_agent.research_agent(self.keyword, self.language)
        writer = writer_agent.create()
        visual_designer = visual_designer_agent.create()

        research_task = researcher_agent.research_task(self.keyword, self.language)
        writing_task = writer_agent.get_task(self.word_count, self.language)
        visual_task = visual_designer_agent.get_task(self.language)
        
        # Create and run crew
        crew = Crew(
            agents=[researcher, writer, visual_designer],
            tasks=[research_task, writing_task, visual_task],
            verbose=True,
            process=Process.sequential
        )
        
        # Run the crew and get results
        crew_output = crew.kickoff()
        
        # Save metadata
        metadata = {
            "keyword": self.keyword,
            "language": self.language,
            "word_count": self.word_count,
            "timestamp": datetime.now().isoformat()
        }
        self._save_output(json.dumps(metadata, indent=2), "metadata.json")
        
        # Map results to correct files based on task outputs
        result_mapping = {
            "research_output.md": crew_output.tasks_output[0].raw if len(crew_output.tasks_output) > 0 else "No research output available",
            "blog_post.md": crew_output.tasks_output[1].raw if len(crew_output.tasks_output) > 1 else "No blog post available",
            "visual_design.md": crew_output.tasks_output[2].raw if len(crew_output.tasks_output) > 2 else "No visual design available"
        }
        
        # Save each result to its corresponding file
        for filename, content in result_mapping.items():
            if isinstance(content, (str, tuple)):
                self._save_output(content, filename)
        
        return result_mapping 