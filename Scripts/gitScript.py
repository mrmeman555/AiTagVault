import os
import subprocess

def run_command(command):
  """Runs a command in the shell and returns the output."""
  try:
    output = subprocess.check_output(command, shell=True, text=True)
    return output.strip()
  except subprocess.CalledProcessError as e:
    return f"Error: {e.output}"

def check_git_installation():
  """Checks if Git is installed."""
  output = run_command("git --version")
  if "git version" in output:
    print(f"Git is installed: {output}")
  else:
    print(f"Git is not installed. Please install Git: {output}")

def check_git_repository():
  """Checks if the current directory is a Git repository."""
  output = run_command("git rev-parse --is-inside-work-tree")
  if output == "true":
    print("Current directory is a Git repository.")
  else:
    print("Current directory is not a Git repository.")

def check_remote_origin():
  """Checks if the remote 'origin' is configured."""
  output = run_command("git remote -v")
  if "origin" in output:
    print(f"Remote 'origin' is configured:\n{output}")
  else:
    print("Remote 'origin' is not configured.")

def check_line_endings():
  """Checks the Git line ending configuration."""
  output = run_command("git config --global core.autocrlf")
  print(f"Line ending setting (core.autocrlf): {output}")

def check_index_lock():
  """Checks for the existence of the index.lock file."""
  index_lock_path = os.path.join(".git", "index.lock")
  if os.path.exists(index_lock_path):
    print(f"Warning: Index lock file exists: {index_lock_path}")
    print("This might indicate a crashed Git process. Please resolve any issues and remove the file if necessary.")
  else:
    print("No index lock file found.")

def check_untracked_files():
  """Lists untracked files."""
  output = run_command("git ls-files --others --exclude-standard")
  if output:
    print(f"Untracked files:\n{output}")
  else:
    print("No untracked files found.")

def check_modified_files():
  """Lists modified files."""
  output = run_command("git diff --name-only")
  if output:
    print(f"Modified files:\n{output}")
  else:
    print("No modified files found.")

def main():
  """Runs the Git diagnostics."""
  print("Running Git Diagnostics...")
  check_git_installation()
  check_git_repository()
  check_remote_origin()
  check_line_endings()
  check_index_lock()
  check_untracked_files()
  check_modified_files()
  print("Git Diagnostics Completed.")

if __name__ == "__main__":
  main()