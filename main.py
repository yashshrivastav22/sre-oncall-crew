from crew.tasks.definitions import build_observe_task
from crewai import Crew


def run_observer(pod_name: str):
    task = build_observe_task(pod_name)
    crew = Crew(agents=[task.agent], tasks=[task], verbose=True)
    result = crew.kickoff()
    print("\n" + "=" * 60)
    print("OBSERVER OUTPUT")
    print("=" * 60)
    print(result)
    return result


if __name__ == "__main__":
    run_observer("memory-hog-7c66c47b8b-q4dp6")
