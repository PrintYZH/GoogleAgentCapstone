from ..config import agentConfig, retryConfig
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search

destination_research_agent = LlmAgent(
    model = Gemini(model = agentConfig.working_model, retry_options=retryConfig),
    name = 'destination_research_agent',
    description='A sub-agent that researches detailed information about a specific travel destination, including attractions, local culture, cuisine, and travel tips.',
    instruction = """You are an expert travel researcher.
    You will use 'google_search' tool to research detailed information about the activities, famous attractions, and local restaurants with more than 4.0 star ratings with more than 100 reviews in the destination provided by the user.
    **IMPORTANT**: You should ONLY provide information that is relevant to the destination provided by the user.
    **WARNING**: be AWARE of the constraints provided by the user (such as budget, travel dates, interests, etc.) and make SURE that your research results align with these constraints.
    Your output should including:
    1. A list of top 10 must-visit attractions in the destination with the information on the location, the operating hours, and the entry price for each attraction.
    2. A list of top 10 popular local activities along with a brief description for each activity.
    3. A list of top 10 local restaurants with more than 4.0 star ratings and more than 100 reviews, along with the location, the operating hours, and the specialty of each restaurant.
""", 
    tools = [google_search],
    output_key='destination_research_results',
)