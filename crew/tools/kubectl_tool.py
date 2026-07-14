import subprocess
from crewai.tools import tool


def _kubectl(args: list[str]) -> str:
    cmd = ["kubectl"] + args
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        return f"kubectl error: {result.stderr.strip()}"
    return result.stdout.strip()


@tool("Get pod status")
def get_pod_status(pod_name: str) -> str:
    """Get the current status and restart count of a specific pod."""
    return _kubectl(["get", "pod", pod_name, "-o", "wide"])


@tool("Get pod events")
def get_pod_events(pod_name: str) -> str:
    """Get recent Kubernetes events for a specific pod, useful for
    diagnosing OOMKilled, CrashLoopBackOff, and scheduling issues."""
    return _kubectl([
        "get", "events",
        "--field-selector", f"involvedObject.name={pod_name}",
        "--sort-by", ".lastTimestamp",
    ])


@tool("Get pod resource limits")
def get_pod_resources(pod_name: str) -> str:
    """Get the configured memory/CPU requests and limits for a pod."""
    return _kubectl([
        "get", "pod", pod_name,
        "-o", "jsonpath={.spec.containers[*].resources}",
    ])
