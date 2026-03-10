from groq import Groq

# Initialize Groq client with your API key
client = Groq(api_key="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")

# System prompt - this defines who the chatbot is
system_prompt = """
You are a helpful customer support assistant for a clothing store called "StyleHub".

Your job:
- Help customers find the right clothes
- Answer questions about sizes, prices, and availability
- Be friendly and 
- Don't talk about anything unrelated to clothing and fashion
- Don't use ** emojis** or slang, keep it professional
- keep responses short and to the point (5-6 sentences max)
- keep your response clean and tidy, avoid unnecessary words or phrases or emojis
Rules:
- Only talk about clothing and fashion related topics
- If someone asks something unrelated, politely redirect them
- Always recommend checking the website for latest 
"""

# Store conversation history with system prompt
history = [
    {"role": "system", "content": system_prompt}
]

print("StyleHub Assistant is ready! (Type 'quit' to exit)")

while True:
    user_input = input("You: ")

    # Exit if user types 'quit'
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # Add user message to history
    history.append({
        "role": "user",
        "content": user_input
    })

    # Send message with full conversation history
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history
    )

    ai_response = response.choices[0].message.content

    # Add AI response to history
    history.append({
        "role": "assistant",
        "content": ai_response
    })

    print("AI:", ai_response)
    print()