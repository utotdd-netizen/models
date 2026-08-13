from fastapi import FastAPI
from pydantic import BaseModel
from llama_cpp import Llama

app = FastAPI()

print("Downloading and Loading Llama-3.2-1B-Instruct...")
llm = Llama.from_pretrained(
    repo_id="bartowski/Llama-3.2-1B-Instruct-GGUF",
    filename="Llama-3.2-1B-Instruct-Q2_K.gguf",
    n_ctx=256,        
    n_threads=1       
)
print("Llama AI is Online and Smart!")

class AIQuery(BaseModel):
    prompt: str

@app.post("/chat")
def ask_llama(query: AIQuery):
    full_prompt = f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n{query.prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    
    response = llm(
        full_prompt,
        max_tokens=80,    
        stop=["<|eot_id|>"],
        echo=False
    )
    return {"reply": response["choices"]["text"].strip()}
