import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew, LLM

llm = LLM(
    model="anthropic/claude-sonnet-4-6",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)

test_agent = Agent(
    role="Greeter",
    goal="Say hello and confirm you're working",
    backstory="A simple agent used to test the setup.",
    llm=llm,
)

test_task = Task(
    description="Say hello and confirm the connection is working.",
    expected_output="A short friendly confirmation message.",
    agent=test_agent,
)

crew = Crew(agents=[test_agent], tasks=[test_task])
result = crew.kickoff()
print(result)
