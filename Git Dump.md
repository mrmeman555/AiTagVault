

## Setting Up Git for Your Obsidian Vault

**1. Install Git:**

- Download and install the latest version of Git from the official website: [https://git-scm.com/](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgit-scm.com%2F).
    

**2. Create a GitHub Account (Optional but Recommended):**

- For collaboration and remote backups, create a free GitHub account: [https://github.com/](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2F).
    

**3. Initialize a Git Repository in Your Vault:**

- **Open Your Obsidian Vault:** Navigate to your vault's folder in your file explorer.
    
- **Open Terminal/Command Prompt:** Open a terminal (Mac/Linux) or command prompt (Windows) and navigate to your vault's directory using the cd command.
    
- **Initialize Git:** Type git init and press Enter. This creates a hidden .git folder, turning your vault into a Git repository.
    

**4. Configure Git:**

- **Set Your Name and Email:**
    
    - Type git config --global user.name "Your Name" and press Enter.
        
    - Type git config --global user.email "your_email@example.com" and press Enter, using your actual email.


Type the following command and press Enter to check your global Git email:

lua

Copy code

`git config --global user.email`


add the repo you creaet to github desktop (basically github) by using 'add local repo' in github desktop

navigate to the location I'm storing ssh keys (in .ssh folder (in onedrive))
ssh-keygen -t ed25519 -C "your_email@example.com"

ssh is in user root dir
Your public key has been saved in /c/Users/User/.ssh/id_ed25519.pub


save copy in one drive

confirm github connection
ssh -T git@github.com

```
git remote add origin git@github.com:mrmeman555/AiTagVault.git
```

content_copyUse code [with caution](https://support.google.com/legal/answer/13505487).Bash

**Explanation:**

- git remote add: This command tells Git to add a new remote repository.
    
- origin: This is a conventional name for the remote repository on GitHub (you can use other names if you like).
    
- git@github.com:mrmeman555/AiTagVault.git: This is the SSH URL for your GitHub repository, which you'll use to connect via SSH.
    

**Verification:**

After running this command, you can verify that the remote was added correctly by running:

```
git remote -v
```

content_copyUse code [with caution](https://support.google.com/legal/answer/13505487).Bash

This should output the following:

```
origin  git@github.com:mrmeman555/AiTagVault.git (fetch)
origin  git@github.com:mrmeman555/AiTagVault.git (push)
```

content_copyUse code [with caution](https://support.google.com/legal/answer/13505487).

**Now you can proceed with changing the remote URL to use SSH, as instructed previously:**

```
git remote set-url origin git@github.com:mrmeman555/AiTagVault.git
```