from ..config import agentConfig, retryConfig
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini

from google.adk.tools import google_search

recommender_agent = LlmAgent(
    model = Gemini(model = agentConfig.working_model, retry_options=retryConfig),
    name = 'recommender_agent',
    description = 'An agent that provides travel destinations recommendations based on the information provided by the user.',
    instruction = """You are the experienced travel consultant. 
    Your task is to use 'google_search' tool to find the best travel destinations for users based on the user's preferences and constraints (such as travel dates, season, budget, interests, etc.).
    Your output should be a list of the top 5 recommended travel destinations with a brief explanation for each recommendation.
""",
    tools = [google_search],
    output_key='recommendations',
)
