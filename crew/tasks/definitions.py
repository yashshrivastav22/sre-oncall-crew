from crewai import Task
from crew.agents.definitions import observer_agent


def build_observe_task(pod_name: str):
    return Task(
        description=(
            f"Investigate pod '{pod_name}'. Get its status, recent events, "
            f"and configured resource limits. Report the raw facts only."
        ),
        expected_output="A factual summary of pod status, events, and "
                        "resource limits. No interpretation.",
        agent=observer_agent,
    )
