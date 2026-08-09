from langchain_mcp_adapters.client import MultiServerMCPClient

from langchain.agents import create_agent

from langchain_groq import ChatGroq

from dotenv import load_dotenv

import asyncio
load_dotenv()

async def main():
    Client =MultiServerMCPClient(
        {
            "Math":{
                "command":"python",
                "args":["MathServer.py"],## ensure correct path
                "transport":"stdio",
            },

            "Weather":{
                "url":"http://127.0.0.1:8000/mcp",
                "transport":"streamable-http"
            }
        }
    )



    import os

    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    tools = await Client.get_tools()
    for t in tools:
        print(t.name)
    model = ChatGroq(model="llama-3.1-8b-instant")

    agent = create_agent(
        model,tools
    )

    math_response = await agent.ainvoke(
        {"messages":[{"role":"user","content":"what is multiplication of 18 and 9 and adding 100 ?"}]}
    )

    print("Math_response  :",math_response["messages"][-1].content)

    weather_response = await agent.ainvoke(
        {"messages":[{"role":"user","content":"what is weather in mumbai?"}]}
    )

    print("Weather_response  :",weather_response["messages"][-1].content)
    print(weather_response["messages"][-1].content)

asyncio.run(main())  