from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage
import getpass
import os

load_dotenv()

# II. Using Language Models
if not os.environ.get("MISTRAL_API_KEY"):
    os.environ["MISTRAL_API_KEY"] = getpass.getpass("Enter API key for Mistral AI: ")

model = ChatMistralAI(model="mistral-large-latest")

messages = [
    SystemMessage("Translate the following from English into Korean"),
    HumanMessage("hi"),
]

model.invoke(messages)

# III. Prompt Templates

from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"language": "Italian", "text": "hi!"})
print(prompt)

prompt.to_messages()

response = model.invoke(prompt)
print(response.content)