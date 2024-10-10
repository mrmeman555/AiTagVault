import os

def list_files_and_folders(root_path, output_filename="directory_listing.txt"):
  """Recursively lists all files and folders and writes the output to a file."""
  output_path = os.path.join(root_path, output_filename) # Path to output file
  with open(output_path, 'w', encoding='utf-8') as outfile:
    for root, dirs, files in os.walk(root_path):
      outfile.write(f"Directory: {root}\n")
      for dir in dirs:
        outfile.write(f"  Subdirectory: {dir}\n")
      for file in files:
        outfile.write(f"  File: {file}\n")

# Example Usage:
root_path = "G:\My Drive\MyObsidian\AiTagVault" # Replace with your folder path
list_files_and_folders(root_path)

print(f"Directory listing saved to: {os.path.join(root_path, 'directory_listing.txt')}")