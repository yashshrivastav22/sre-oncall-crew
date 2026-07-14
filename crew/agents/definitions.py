from crewai import Agent
from crew.config.llm import get_llm
from crew.tools.kubectl_tool import get_pod_status, get_pod_events, get_pod_resources

llm = get_llm()

observer_agent = Agent(
    role="Kubernetes observer",
    goal="Gather all relevant facts about a failing pod: status, events, "
         "and resource limits. Report findings only, no interpretation.",
    backstory="A meticulous SRE who reads raw signals before jumping to "
              "conclusions. Never guesses at root cause; only reports facts.",
    tools=[get_pod_status, get_pod_events, get_pod_resources],
    llm=llm,
    verbose=True,
)
