

#installed tiktoken.
#   It converts text into tokens, which are the pieces of text that language models like GPT process.




import tiktoken

# Get the tokenizer for GPT-4o
enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hello world"

# Encode the text into tokens
tokens = enc.encode(text)

print(f"Text: {text}")
print(f"Tokens: {tokens}")
print(f"Number of tokens: {len(tokens)}")

# See what each token represents
print("\nToken breakdown:")

for token in tokens:
    print(f"{token} → '{enc.decode([token])}'")