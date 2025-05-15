# Blog Post Generator with CrewAI

This Streamlit application uses CrewAI and OpenAI models to generate SEO-optimized blog posts based on keyword research and enhanced with AI-generated visual content suggestions.

## Setup

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file in the root directory with your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

## Running the Application

Run the Streamlit app with:
```bash
streamlit run app.py
```

## Features

- Keyword research using AI agents and SerperDev API
- SEO-optimized content generation
- Structured blog post creation with proper heading hierarchy
- Support for multiple languages
- Customizable word count
- AI-generated visual content suggestions every 200 words:
  - Meme concepts
  - Infographic layouts
  - Custom graphics
  - Stock photo recommendations
  - Data visualization ideas
- Meta description and title analysis
- Comprehensive SEO pattern analysis

## How it Works

The application uses three specialized AI agents working in sequence:

1. **Research Agent**: Analyzes top search results for your keyword and creates a comprehensive SEO report
2. **Content Writer**: Creates a well-structured blog post with markers for visual content
3. **Visual Designer**: Generates detailed visual content suggestions for each marked section

Each visual suggestion includes:
- Detailed description
- Style and tone recommendations
- Key elements to include
- Text overlay suggestions
- Color scheme recommendations
- Recommended dimensions 