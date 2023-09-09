from phospho import Agent, Message

# Initialize the agent
agent = Agent()

def ph_agent(input : str):
    response = f"PH asked : {input}"
    return response

# Define your routes
# you don't have to implement both routes
"""
@agent.ask()
def myask(message):
    print(f"Your message was {message.content}, now I can do stuff in the background")
"""

@agent.chat()
def mychat(message):
    response = ph_agent(message.content)
    return Message(response)

# That's it, you're done!