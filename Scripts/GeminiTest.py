import ast
import re
import os
from sentence_transformers import SentenceTransformer, util

def extract_messages(chat_session):
    """Extracts the original and recalled messages from the chat session string."""

    print("Attempting to extract messages...")

    # Find the start and end of the dictionary string within the file
    start_index = chat_session.find("history=[")
    end_index = chat_session.rfind("]") + 1  # Find the last ']' and include it

    # Extract the dictionary string and evaluate it
    chat_session_dict = ast.literal_eval(chat_session[start_index:end_index]) 

    # Find the recalled messages section
    recalled_start = chat_session.find(
        'You got it, Mimir! Here are the verbatim messages 3-5, where "Communication" emerged as a salient topic:'
    )
    if recalled_start == -1:
        print("Error: Could not find the recalled messages section in the input file.")
        return [], []
    
    recalled_end = chat_session.find("---\n### 4", recalled_start)
    if recalled_end == -1:
        print("Error: Could not find the end delimiter for recalled messages.")
        return [], []

    recalled_messages_section = chat_session[recalled_start:recalled_end].strip()

    # Extract the recalled messages, removing the leading ">>(This is Kvasir speaking)"
    recalled_messages = [
        re.sub(r'>>\(This is Kvasir speaking\)\n\n', '', message.strip()).strip() 
        for message in recalled_messages_section.split('\n\n**Message')[1:]  
    ]

    print(f"Successfully extracted {len(recalled_messages)} recalled messages.")

    # Extract all model responses from the chat history
    original_messages = [
        part
        for message in chat_session_dict  # Now using the extracted dictionary
        if message['role'] == 'model'
        for part in message['parts']
    ]
    print(f"Successfully extracted {len(original_messages)} original messages.")

    return original_messages, recalled_messages


def compare_words(original_text, recalled_text):
  """Compares words in two texts, ignoring spacing and formatting."""
  original_words = re.findall(r'\b\w+\b', original_text.lower()) 
  recalled_words = re.findall(r'\b\w+\b', recalled_text.lower())
  d = difflib.Differ()
  diff = d.compare(original_words, recalled_words)
  return '\n'.join(diff)

def find_closest_match(target_message, candidate_messages, model):
  """Finds the closest matching message based on semantic similarity."""
  print("Calculating semantic similarities...")
  target_embedding = model.encode(target_message, convert_to_tensor=True)
  best_match = None
  best_similarity = -1

  for candidate in candidate_messages:
    candidate_embedding = model.encode(candidate, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(target_embedding, candidate_embedding).item()
    if similarity > best_similarity:
      best_similarity = similarity
      best_match = candidate

  print("Found closest match.")
  return best_match

def main():
    # Load a pre-trained SentenceTransformer model for semantic similarity
    print("Loading SentenceTransformer model...")
    model = SentenceTransformer('all-mpnet-base-v2')
    print("Model loaded successfully.")

    # File path for the chat session data (using raw string)
    input_file = r"G:\My Drive\MyObsidian\AiTagVault\Scripts\GeminiInput.txt"

    # Read chat session data from the file
    print(f"Reading chat session data from: {input_file}...")
    with open(input_file, 'r') as f:
        chat_session = f.read()
    print("File read successfully.")

    # Extract the original and recalled messages
    original_messages, recalled_messages = extract_messages(chat_session)

    for i, recalled_message in enumerate(recalled_messages):
        print(f"---- Analyzing Recall of Message {i + 3} ----")  # Start from message 3
        closest_match = find_closest_match(recalled_message, original_messages, model)
        print("Original Message:")
        print(closest_match)
        print("\nRecalled Message:")
        print(recalled_message)
        print("-------------------------------------\n")

        # Compare the words in the closest match and recalled message
        word_comparison = compare_words(closest_match, recalled_message)
        if word_comparison:
            print("Word-level Discrepancies:")
            print(word_comparison)
        else:
            print("No word-level discrepancies found.")
        print("-------------------------------------\n")

if __name__ == "__main__":
    main()