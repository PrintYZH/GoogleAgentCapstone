import os

from dataclasses import dataclass
from google.genai import types

import google.auth
_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", 'GoogleAgentCapstone')
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "FALSE")

@dataclass
class AgentConfig:
    """
    Configuration settings for the Travel Planner Agent.
    
    Attributes:
        thinking_model (str): Model used for planning the travel itinerary and evaluating options.
        working_model (str): Model used for finding information and summarizing details.
    """
    thinking_model : str = "gemini-2.5-flash"
    working_model : str = "gemini-2.5-flash-lite"

agentConfig = AgentConfig()

def RetryConfig() -> types.HttpRetryOptions:
    """
    Returns a RetryConfig object with predefined settings for retrying HTTP failed requests.
    
    Returns:
        types.RetryConfig: Configuration for retrying requests.
    """
    return types.HttpRetryOptions(
        attempts=5, # maximum number of retry attempts
        exp_base=7, # Delay multiplier
        initial_delay=1.0,
        http_status_codes=[429,500,503,504],
    )

retryConfig = RetryConfig()
