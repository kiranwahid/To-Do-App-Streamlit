import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled
import chainlit as cl
import rich
load_dotenv()
set_tracing_disabled(disabled=True)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
history = []
client = AsyncOpenAI(
api_key=OPENROUTER_API_KEY,
base_url="https://openrouter.ai/api/v1",
)
agent =Agent(
    name="My Agent",
    instructions="You are a helpful assistant that can answer questions and help with tasks.",
    model=OpenAIChatCompletionsModel(
        model="deepseek/deepseek-chat-v3-0324:free",openai_client=client
    ))
@cl.on_message
async def my_message(message:cl.Message):
    user_input = message.content
    history.append({"role":"user","content":user_input})
    message = cl.Message(content="")
    runner = Runner.run_streamed(agent,history)
    rich.print(runner.final_output)

    async for event in runner.stream_events():
        if event.type == "raw_response_event" and hasattr(event.data,"delta"):
            await message.stream_token(event.data.delta)

    
    






