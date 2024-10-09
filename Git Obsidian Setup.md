---
tags:
---

## Setting Up Git for Your Obsidian Vault - A Detailed Guide

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
    origin  git@github.com:<username>/<repository>.git (fetch)
    origin  git@github.com:<username>/<repository>.git (push)
    ```
* **Double-Check Case:** Make sure the capitalization of the repository name in the remote URL matches the *exact* capitalization on GitHub. 

**11. Renormalize Existing Files (If Necessary):**

* **Address Line Ending Inconsistencies:** Run the command `git add --renormalize .` to normalize line endings in all files.

**12. Make Your First Commit:**

* **Stage All Changes:** Type `git add .` and press Enter to stage all the files that Git should track (your notes, attachments, and the `.gitignore` file). 
* **Commit:** Type `git commit -m "Initial commit"` and press Enter. 

**13. Push to GitHub:**

* **Initial Push:**  Type `git push -u origin master` (or `git push -u origin main`, if applicable) and press Enter. 

**14. Troubleshooting Tips:**

* **"Permission denied (publickey)":** 
    * Verify your SSH key is listed in your GitHub SSH settings.
    * Check your SSH agent (`ssh-add -l`) and add your key if it's not listed (`ssh-add ~/.ssh/id_ed25519`).
    * Restart your terminal.
* **"Repository not found":**
    * Double-check that the repository URL in your `git remote -v` output matches the exact URL on GitHub, including capitalization. 
    * Make sure the repository exists and you have the correct access permissions. 
* **"Everything up-to-date":** This message is normal if there are no new changes to push since your last commit. 

**Congratulations! Your Obsidian vault is now under version control with Git and connected to your GitHub repository.** You're ready to track your changes, collaborate with others (if desired), and enjoy the peace of mind that comes with a well-managed and backed-up knowledge base! 