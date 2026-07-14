"""
LLM provider config. Toggle between Ollama (local, free) and Claude API
by changing PROVIDER below - no agent code changes needed elsewhere.
"""
from crewai import LLM

PROVIDER = "ollama"  # change to "claude" later if desired


def get_llm():
    if PROVIDER == "ollama":
        return LLM(
            model="ollama/llama3.2:3b",
            base_url="http://localhost:11434",
        )
    if PROVIDER == "claude":
        import os
        return LLM(
            model="anthropic/claude-sonnet-4-6",
            api_key=os.getenv("ANTHROPIC_API_KEY"),
        )
    raise ValueError(f"Unknown provider: {PROVIDER}")
