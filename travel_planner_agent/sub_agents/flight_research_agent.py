from ..config import agentConfig, retryConfig
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search

flight_research_agent = LlmAgent(
    model = Gemini(model = agentConfig.working_model, retry_options=retryConfig),
    name = 'flight_research_agent',
    description='A sub-agent that researches detailed information about the flights from the origin to the specified travel destination.',
    instruction = """You are an expert flight researcher.
    You will use 'google_search' tool to research information about the price and schedule of the flights from the origin to the destination provided by the user.
    **IMPORTANT**: You should ONLY provide information that is relevant to the origin and the destination provided by the user.
    Your output should be a list of flights including the airline name, flight number, departure time, arrival time, duration, and price for each flight.
""", 
    tools = [google_search],
    output_key='flight_research_results',
)