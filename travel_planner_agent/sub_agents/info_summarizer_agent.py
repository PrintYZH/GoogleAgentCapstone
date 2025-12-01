from ..config import agentConfig, retryConfig
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import google_search

info_summarizer_agent = LlmAgent(
    model = Gemini(model = agentConfig.working_model, retry_options=retryConfig),
    name = 'info_summarizer_agent',
    description='A sub-agent that summarizes and consolidates the researched information about the travel destination, accommodations, and flights into the full detailed travel iterinary.',
    instruction = """You are an expert travel summarizer.
    Your task is to summarize and consolidate information from these following research results:
    1. *Destination Research Results*: {destination_research_results}
    2. *Accommodation Research Results*: {accommodation_research_results}
    3. *Flight Research Results*: {flight_research_results}
    Your output should be the consolidated list of the researched information in a well-structured format for easy understanding and reference.
    **IMPORTANT**: Make sure to keep all the important details from each research result while summarizing (such as names, locations, FLIGHT NUMBERS, operating hours, prices, ratings, etc.).
    """, 
    tools = [google_search],
    output_key='summarized_info',
)