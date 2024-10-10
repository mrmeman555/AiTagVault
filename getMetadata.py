import os
import frontmatter

def extract_obsidian_metadata(vault_path):
    """Extracts metadata (tags, headers, and Description) from Obsidian Markdown files."""
    metadata = {}
    for root, dirs, files in os.walk(vault_path):
        print(f"Checking directory: {root}")  # Debugging output
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                print(f"   Processing file: {file_path}")  # Debugging output

                # Load the file front matter
                with open(file_path, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                    tags = post.get('tags', [])
                    description = post.get('Description', "")

                print(f"      Tags: {tags}")  # Debugging output
                print(f"      Description: {description}")  # Debugging output

                # Read file again to get headers (frontmatter.load consumes the file stream)
                headers = []
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.startswith("### "):
                            header = line.strip().lstrip("### ").rstrip("###")
                            headers.append(header)

                print(f"      Headers: {headers}")  # Debugging output

                # Store metadata for this file
                metadata[file] = {'tags': tags, 'description': description, 'headers': headers}
    return metadata

if __name__ == "__main__":
    vault_path = r"G:\My Drive\MyObsidian\AiTagVault\Inbox"  # Path to your vault
    metadata = extract_obsidian_metadata(vault_path)

    # Output to a Markdown file
    output_file = "metadata_output.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Obsidian Metadata\n\n")  # Heading
        for file, data in metadata.items():
            f.write(f"## {file}\n\n")
            f.write(f"**Tags:** {', '.join(data['tags'])}\n\n")
            f.write(f"**Description:** {data['description']}\n\n")
            f.write(f"**Headers:** {', '.join(data['headers'])}\n\n")
            f.write("\n---\n\n")

    print(f"Metadata extracted and saved to: {output_file}") 
    print(f"Current Working Directory: {os.getcwd()}") # Print the current working directory