from google.adk.agents import ParallelAgent, SequentialAgent
from .destination_research_agent import destination_research_agent
from .flight_research_agent import flight_research_agent
from .accommodation_research_agent import accommodation_research_agent
from .info_summarizer_agent import info_summarizer_agent

destination_research_team = ParallelAgent(
    sub_agents=[destination_research_agent, flight_research_agent, accommodation_research_agent],
    name='destination_research_team',
)

destination_planner_team = SequentialAgent(
    sub_agents=[destination_research_team, info_summarizer_agent],
    name='destination_planner_team',
)