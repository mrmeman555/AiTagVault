import os
import re
import frontmatter

def extract_obsidian_metadata(vault_path):
    """Extracts metadata (tags and Descriptionription) from Obsidian Markdown files."""
    metadata = {}
    for root, dirs, files in os.walk(vault_path):
        print(f"Checking directory: {root}") # Debugging output
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                print(f"   Processing file: {file_path}")  # Debugging output
                with open(file_path, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                    tags = post.get('tags', [])
                    Descriptionription = post.get('Description', "")
                    metadata[file] = {'tags': tags, 'Description': Descriptionription}
    return metadata

if __name__ == "__main__":
    vault_path = r"G:\My Drive\MyObsidian\AiTagVault\Inbox" 
    metadata = extract_obsidian_metadata(vault_path)

    # Output to a Markdown file
    output_file = "metadata_output.md" 
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Obsidian Metadata\n\n") # Heading
        for file, data in metadata.items():
            f.write(f"## {file}\n\n")  # File name as a heading
            f.write(f"- **Tags:** {', '.join(data['tags'])}\n")
            f.write(f"- **Description:** {data['Description']}\n\n")

    print(f"Metadata extracted and saved to: {output_file}") 