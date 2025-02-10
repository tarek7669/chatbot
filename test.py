from transformers import AutoModelForCausalLM, AutoTokenizer
from langchain.vectorstores import Chroma
import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load Model
model_name = "D:\Projects\chatbot\chatbot_model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32, device_map="cpu")

# Load vector store
vectorstore = Chroma(persist_directory="D:\Projects\chatbot\chroma_db")
retriever = vectorstore.as_retriever()

print("Chatbot loaded successfully!")


def chatbot_response(user_input):
    inputs = tokenizer(user_input, return_tensors="pt").to("cpu")
    output = model.generate(**inputs, max_length=200)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Gradio UI
iface = gr.Interface(fn=chatbot_response, inputs="text", outputs="text", title="Chatbot")

iface.launch()

