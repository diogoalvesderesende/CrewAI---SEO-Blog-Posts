# AI Blog Post Generator

This Streamlit app uses CrewAI to generate SEO-optimized blog posts with visual design suggestions based on a given keyword.

## Setup

1. Clone the repository
2. Create a virtual environment and activate it
3. Install the requirements:
```bash
pip install -r requirements.txt
```
4. Create a `.env` file in the root directory with the following variables:
```
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

## Running the app

```bash
streamlit run app.py
```

## Requirements

- Python 3.9+
- OpenAI API key
- Serper API key (for web search)

## Features

- SEO research on target keywords
- Blog post generation with proper structure
- Visual design suggestions for the blog post
- Support for multiple languages (English, Spanish, Portuguese, French, German)
- Customizable word count

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