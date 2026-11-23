
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# 1. Define the local model path
model_path = "./models/qwen"

# 2. Select the device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Running on: {device}")

# 3. Load tokenizer
print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_path)

# 4. Load model
print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(model_path)

model.to(device)
model.eval()

print("\nQwen AI Model is ready!")
print("Type 'exit' to stop.\n")

# 5. Take user input and generate responses
while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Exiting AI model...")
        break

    # Format the conversation
    messages = [
        {"role": "user", "content": user_input}
    ]

    # Convert prompt into PyTorch tensor
    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt",
        return_dict=False
    ).to(device)

    # Generate response
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id
        )

    # Extract only newly generated tokens
    generated_tokens = outputs[0][inputs.shape[-1]:]

    # Convert tokens into readable text
    response = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    )

    print("\nAI:", response, "\n")
