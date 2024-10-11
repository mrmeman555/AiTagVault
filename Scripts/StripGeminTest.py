def simplify_chat_data(input_file, output_file):
    """Reads the chat session data, extracts messages, and writes them 
    to a new file line by line.
    """
    print(f"Reading chat session data from: {input_file}...")
    with open(input_file, 'r') as f:
        chat_session = f.read()
    print("File read successfully.")

    print("Extracting messages and writing to output file...")
    skip_next_line = False
    current_role = None
    with open(output_file, 'w') as outfile:
        for line in chat_session.splitlines():
            print(f"Processing line: {line}") # Print the line before processing
            if '"role":' in line:
                if '"user"' in line:
                    current_role = "user"
                elif '"model"' in line:
                    current_role = "model"
                skip_next_line = True  
            elif skip_next_line:
                skip_next_line = False
            else: 
                if current_role:
                    message_part = line.split('"(', 1)[1].split(')"', 1)[0] 
                    print(f"{current_role.capitalize()} message part: {message_part}")
                    outfile.write(f"{current_role}: {message_part}\n")

    print(f"Simplified chat data written to: {output_file}")
def main():
    input_file = r"G:\My Drive\MyObsidian\AiTagVault\Scripts\GeminiInput.txt"
    output_file = r"G:\My Drive\MyObsidian\AiTagVault\Scripts\simplified_chat.txt"
    simplify_chat_data(input_file, output_file)

if __name__ == "__main__":
    main()