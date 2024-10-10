import os
import re
import frontmatter

def extract_obsidian_metadata(vault_path):
    """Extracts metadata (tags and Description) from Obsidian Markdown files."""
    # ... (function remains the same) ...

if __name__ == "__main__":
    vault_path = "your/vault/path"  # Replace with your actual vault path
    metadata = extract_obsidian_metadata(vault_path)

    # Output to a Markdown file
    output_file = "metadata_output.md" 
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Obsidian Metadata\n\n") # Heading
        for file, data in metadata.items():
            f.write(f"## {file}\n\n")  # File name as a heading
            f.write(f"- **Tags:** {', '.join(data['tags'])}\n")
            f.write(f"- **Description:** {data['Desc']}\n\n")

    print(f"Metadata extracted and saved to: {output_file}")