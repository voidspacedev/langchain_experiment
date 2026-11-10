from langchain.agents import create_agent
from langchain_core.runnables import RunnableConfig
from langchain_ollama import ChatOllama
from langchainexperiment.tools.search_tool import search_tool
from langgraph.checkpoint.memory import InMemorySaver


model = ChatOllama(
    model="qwen3.5:4b",
    temperature=0,
    
)

agent = create_agent(
    model=model,
    tools=[search_tool],
    checkpointer=InMemorySaver(),
    system_prompt="""
    You are a chef with 10 years of cooking experience.

        Your responsibilities:
        1. Analyze the ingredients provided by the user.
        2. Identify suitable dishes that can be prepared using those ingredients.
        3. Use search_tool to research suitable dishes and cooking methods.
        4. Select the most appropriate dish.
        5. Generate a delicious, easy-to-follow recipe.

        The recipe must include:
        - Dish name
        - Ingredient quantities
        - Preparation instructions
        - Step-by-step cooking instructions
        - Cooking temperatures
        - Cooking times
        - Lid and heat settings where applicable.

        Only use ingredients provided by the user.
        Mention any additional ingredients separately.
        Never invent search results.  
        """
)

thread_config: RunnableConfig = {"configurable": {"thread_id": "1"}}

response= agent.invoke(
    {"messages": [
        {
            "role": "user",
            "content": """I have chicken, rice, onions, salt, red chilli powder, 
                        ginger garlic paste, garam masala, 
                        water, turmeric powder and spices."""
        }
    ]},config=thread_config,)
print(response["messages"][-1].content)

response2 = agent.invoke(
    {"messages": [{"role": "user", "content": "Can you make it spicier?"}]},
    config=thread_config,
)

print(response2["messages"][-1].content)
