import os
import streamlit as st
from dotenv import load_dotenv
from src.crew.blog_crew import BlogCrew
import json
from typing import Union, Tuple

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="Blog Post Generator",
    page_icon="📝",
    layout="wide"
)

def format_content(content: Union[str, Tuple[str, ...]]) -> str:
    """Format content for display"""
    if isinstance(content, tuple):
        return '\n\n'.join(str(item) for item in content)
    return str(content)

def main():
    st.title("🤖 AI Blog Post Generator")
    
    with st.form("blog_generation_form"):
        keyword = st.text_input("Enter your target keyword:")
        language = st.selectbox(
            "Select target language:",
            ["English", "Spanish", "European Portuguese", "French", "German"]
        )
        word_count = st.number_input(
            "Target word count:",
            min_value=300,
            max_value=10000,
            value=1000,
            step=500
        )
        
        submitted = st.form_submit_button("Generate Blog Post")
        
    if submitted and keyword:
        with st.spinner("Generating your blog post... This may take a few minutes."):
            try:
                # Initialize and run BlogCrew
                blog_crew = BlogCrew(keyword, language, word_count)
                result_mapping, metadata_content = blog_crew.run()
                st.success("Blog post generated successfully!")
                
                # Create tabs for different outputs
                research_tab, blog_tab, visual_tab = st.tabs(["Research", "Blog Post", "Visual Design"])
                
                # Research Tab
                with research_tab:
                    st.markdown("### SEO Research Results")
                    research_content = result_mapping.get("research_output.md", "No research output available")
                    st.markdown(format_content(research_content))
                    st.download_button(
                        label="Download Research Output",
                        data=format_content(research_content),
                        file_name="research_output.md",
                        mime="text/markdown"
                    )
                
                # Blog Post Tab
                with blog_tab:
                    st.markdown("### Generated Blog Post")
                    blog_content = result_mapping.get("blog_post.md", "No blog post available")
                    st.markdown(format_content(blog_content))
                    st.download_button(
                        label="Download Blog Post",
                        data=format_content(blog_content),
                        file_name="blog_post.md",
                        mime="text/markdown"
                    )
                
                # Visual Design Tab
                with visual_tab:
                    st.markdown("### Visual Design Suggestions")
                    visual_content = result_mapping.get("visual_design.md", "No visual design available")
                    st.markdown(format_content(visual_content))
                    st.download_button(
                        label="Download Visual Design",
                        data=format_content(visual_content),
                        file_name="visual_design.md",
                        mime="text/markdown"
                    )
                
                # Metadata download
                st.download_button(
                    label="Download Metadata",
                    data=format_content(metadata_content),
                    file_name="metadata.json",
                    mime="application/json"
                )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 