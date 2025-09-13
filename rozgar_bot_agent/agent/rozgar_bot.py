from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
import os
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

# ✅ Ab spawnAgent async bana do
async def spawnAgent(query: str):
    agent = Agent(
        name="Rozgar Assistant",
        instructions="""
        Tum job assistant ho. User ko sirf jobs related jawab do.
        Agar user 'web developer Karachi jobs' bole to us hisaab se output do.
        Har jawab me Job Title, Location aur Experience level clearly likho.
        """,
        model=model,
    )

    # ✅ async call use karo
    result = await Runner.run(agent, input=query)
    return result.final_output
