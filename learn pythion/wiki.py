import wikipedia

# Search for a topic
topic = "Philosophy of life"  # You can change this to anything you like

# Get a summary of the topic
summary = wikipedia.summary(topic, sentences=3)

# Print the result
print(f"Summary for '{topic}':\n")
print(summary)
