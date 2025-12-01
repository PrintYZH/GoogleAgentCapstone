from ..config import agentConfig, retryConfig
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import google_search

accommodation_research_agent = LlmAgent(
    model = Gemini(model = agentConfig.working_model, retry_options=retryConfig),
    name = 'accommodation_research_agent',
    description='A sub-agent that researches detailed information about accommodations at the specified travel destination.',
    instruction = """You are an expert accommodation researcher.
    You will use 'google_search' tool to research information about the price and location of the accommodations with more than 4.0 star-rating with good reviews in the destination provided by the user.
    **IMPORTANT**: You should ONLY provide information that is relevant to the destination provided by the user.
    Your output should be a list of top 10 accommodations with more than 4.0 star-rating with good reviews, including the name, price per night, location, and a brief summary of pros and cons from the review for each accommodation.
""", 
    tools = [google_search],
    output_key='accommodation_research_results',
)