from langchain_text_splitters import RecursiveCharacterTextSplitter, Language 

text = """
def get_ai_response(user_input):
    # This is a placeholder for where your model logic (like LangChain) would go
    responses = {
        "hello": "Hi there! Ready to build some AI agents today?",
        "how are you": "I'm functioning at 100% capacity. How are you?",
        "bye": "Goodbye! Happy coding!"
    }
    
    # Return a response based on the dictionary, or a default message
    return responses.get(user_input.lower(), "That's interesting! Tell me more about your project.")

def main():
    print("--- AI Tutor Terminal ---")
    print("Type 'bye' to exit.")
    
    while True:
        user_msg = input("You: ")
        if user_msg.lower() == 'bye':
            print("AI: " + get_ai_response('bye'))
            break
            
        response = get_ai_response(user_msg)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=500,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])