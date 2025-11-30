import uuid
import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from travel_planner_agent.agent import root_agent
from google.genai import types

APP_NAME = "travel_planner_agent_app"
USER_NAME = "TestUser"

async def run_session(
    runner_instance: Runner,
    user_queries: list[str] | str = None,
    session_name: str = "default",
):
    print(f"\n ### Session: {session_name}")

    # Get app name from the Runner
    app_name = runner_instance.app_name

    # Attempt to create a new session or retrieve an existing one
    try:
        session = await session_service.create_session(
            app_name=app_name, user_id=USER_NAME, session_id=session_name
        )
    except:
        session = await session_service.get_session(
            app_name=app_name, user_id=USER_NAME, session_id=session_name
        )

    # Process queries if provided
    if user_queries:
        # Convert single query to list for uniform processing
        if type(user_queries) == str:
            user_queries = [user_queries]

        # Process each query in the list sequentially
        for query in user_queries:
            print(f"\nUser > {query}")

            # Convert the query string to the ADK Content format
            query = types.Content(role="user", parts=[types.Part(text=query)])

            # Stream the agent's response asynchronously
            async for event in runner_instance.run_async(
                user_id=USER_NAME, session_id=session.id, new_message=query
            ):
                # Check if the event contains valid content
                if event.content and event.content.parts:
                    # Filter out empty or "None" responses before printing
                    if (
                        event.content.parts[0].text != "None"
                        and event.content.parts[0].text
                    ):
                        print(event.content.parts[0].text)
    else:
        print("No queries!")

session_service = InMemorySessionService()
session_id = f'TestSession-{uuid.uuid4().hex[:8]}' 

async def main():
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_NAME,
        session_id=session_id,)

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service)

    await run_session(
        runner,[
        "Hi, I want to plan a trip but I'm not sure where to go. I like beaches and historical sites. My budget is around $2000 and I can travel anytime in the next 3 months. Can you help me decide on a destination and plan my itinerary?",
        "I like the second destination you suggested. Can you provide more details about it and help me plan a day-by-day itinerary for a week-long trip there?",
        "I would prefer to stay in mid-range hotels and I'm interested in local cuisine and cultural experiences. Can you include these preferences in the itinerary?"]
        , session_name=session_id,) 

if __name__ == "__main__":
    asyncio.run(main())


    
    







