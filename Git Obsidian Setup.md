---
tags:
  - obsidian
  - github
Desc: Setting up git for obsidian
---
# OSI Overview

### Setting Up Git for Your Obsidian Vault - A Detailed Guide

This guide outlines the steps to set up Git for version control of your Obsidian vault and connect it to a GitHub repository, along with troubleshooting tips based on real-world experiences.

**1. Install Git:**

- Download and install the latest version of Git from the official website: [https://git-scm.com/](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgit-scm.com%2F).

**2. Create a GitHub Account (Optional but Recommended):**

- For collaboration and remote backups, create a free GitHub account: [https://github.com/](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2F).

**3. Create a New Repository on GitHub:**

- Go to [https://github.com/](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2F) and create a new, empty repository.  
- **Important:**  Do **not** initialize the repository with a README, license file, or `.gitignore` file. We'll create these locally.

**4. Initialize a Git Repository in Your Vault:**

- **Open Your Obsidian Vault:** Navigate to your vault's folder in your file explorer.
- **Open Terminal/Command Prompt:** Open a terminal (Mac/Linux) or command prompt (Windows) and navigate to your vault's directory using the `cd` command.
- **Initialize Git:** Type `git init` and press Enter. This creates a hidden `.git` folder, turning your vault into a Git repository.

**5. Configure Git:**

- **Set Your Name and Email:**
    - Type `git config --global user.name "Your Name"` and press Enter.
    - Type `git config --global user.email "your_email@example.com"` and press Enter, using your actual email.

- **Check Your Email Configuration:**
    - Type `git config --global user.email` and press Enter to confirm your email is set correctly.

**6.  Set Line Ending Configuration:**

* **Important for Cross-Platform Compatibility:**
    - Type `git config --global core.autocrlf input` and press Enter.
    - This tells Git to convert Windows-style line endings (CRLF) to Unix-style line endings (LF) when committing but leave LF endings as LF when checking out files. 

**7. Generate an SSH Key:**

- **Navigate to SSH Directory:** Open your terminal/command prompt and navigate to your SSH directory (usually `~/.ssh/` or `C:\Users\YourUsername\.ssh\` on Windows).
- **Generate the Key:** Type `ssh-keygen -t ed25519 -C "your_email@example.com"` and press Enter, replacing "your_email@example.com" with your actual GitHub email. 
- **Save Location:** Press Enter to accept the default file location.
- **Passphrase (Optional but Recommended):**  Create a strong passphrase for your SSH key (this adds extra security) or press Enter to skip.

**8. Add Your SSH Public Key to GitHub:**

- **Open Public Key File:** Open the `id_ed25519.pub` file (in your SSH directory) with a text editor and copy the entire contents.
- **Go to GitHub SSH Settings:** In your web browser, log into GitHub, go to your account settings, and navigate to "SSH and GPG keys".
- **Add New SSH Key:** Click "New SSH key." Give it a title (e.g., "My Laptop") and paste the contents of your public key file into the "Key" field.  Click "Add SSH key."

**9. Create a `.gitignore` File:**

- **Create the File:** In your vault's root folder, create a new file named `.gitignore`.
- **Add Exclusions:**  Open the `.gitignore` file with a text editor and add the following lines:
    ```
    # Ignore Obsidian settings and plugin data
    .obsidian/
    .trash/

    # Ignore operating system files
    .DS_Store
    Thumbs.db

    # Ignore any log files
    *.log
    ```

**10.  Connect to GitHub:**

* **Add the Remote:** In your terminal, navigate to your Obsidian vault directory. Type `git remote add origin git@github.com:<username>/<repository>.git` and press Enter, replacing `<username>` with your GitHub username and `<repository>` with the name of your repository.
* **Verify the Remote URL:** Type `git remote -v` and press Enter. You should see output similar to:
    ```
### Application Layer Interactions

- **Obsidian Vault and Git:**
    - **#obsidian:** Obsidian is the application we're using for note-taking.
    - **#git:** Git is the version control system we're integrating with Obsidian. 
- **Git Commands:**
    - **#git:** We'll use Git commands like `git init`, `git add`, `git commit`, `git push`, and `git pull` to manage our vault. 
- **GitHub Web Interface:**
    - **#github:** We'll interact with GitHub's website to create a repository, manage settings, and view our synced vault. 

### Presentation Layer: Securing Communication

- **SSH Key Generation and Management:**
    - **#protocols/ssh:** SSH is the secure protocol we'll use to communicate with GitHub. 
    - **#github:** GitHub uses SSH keys for secure authentication.

### Session Layer: Establishing Connections

- **SSH Connection:**
    - **#protocols/ssh:** We'll establish a secure SSH connection to interact with our GitHub repository. 
    - **#github:** This connection allows us to push and pull changes to our remote repository on GitHub.
- **Git Remote:**
    - **#git:** We'll configure a "remote" in Git to point to our GitHub repository. 
    - **#github:** This establishes the link between our local and remote repositories. 

### Transport Layer Protocols

- **SSH Protocol:**
    - **#protocols/ssh:** SSH relies on the TCP protocol for reliable data transmission.
- **Git Protocol:**
    - **#git:** Git can use either SSH (over TCP) or HTTPS (over TCP) to transfer data. 

### Network Layer Routing

- **IP Addressing:**
    - **#git, #github, #protocols/ssh:** All network communication, including Git and SSH interactions, relies on IP addressing for routing data.

### Data Link & Physical Layers: Network Infrastructure

- **Underlying Network:**
    - **#git, #github, #protocols/ssh, #obsidian:** All these technologies ultimately depend on the physical and data link layers of your network infrastructure. 

