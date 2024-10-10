---
tags:
  - Anaconda
Description: All things Anaconda Related
---


I need to set env variable
### Anaconda Cheat Sheet - Essential Commands and Syntax

### Environment Management

- **Create:** `conda create -n <environment_name> python=<python_version>` 
- **Activate:** `conda activate <environment_name>`
- **Deactivate:** `conda deactivate`
- **List:** `conda env list`
- **Remove:**  `conda env remove -n <environment_name>`

### Package Management

- **Install:** `conda install <package_name>`
- **Install Multiple:** `conda install <package_1> <package_2> ...`
- **Install Specific Version:** `conda install <package_name>=<version>`
- **Update:** `conda update <package_name>`
- **Update All:** `conda update --all`
- **Search:**  `conda search <package_name>`
- **List Installed Packages:** `conda list`

### Working with Packages (pip)

- **Install:** `pip install <package_name>` 
- **Install from Requirements File:** `pip install -r requirements.txt`
- **Uninstall:** `pip uninstall <package_name>`
- **List Installed Packages:** `pip list`
- **Freeze Requirements:**  `pip freeze > requirements.txt`

### Additional Tips

- **Conda Cheat Sheet:** [https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- **Anaconda Documentation:** [https://docs.anaconda.com/](https://docs.anaconda.com/)


Integrating your local Conda environments with VS Code is essential for a smooth development workflow. Here's how you can do it and use a Conda command prompt within VS Code:

**1. Install the Python Extension:**

- **VS Code Marketplace:** If you haven't already, install the official Python extension for VS Code from the Extensions Marketplace.
    

**2. Select Your Conda Interpreter:**

- **Open Your Project:** Open the project folder you'll be working on in VS Code.
    
- **Command Palette:** Press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
    
- **Select Interpreter:** Type "Python: Select Interpreter" in the Command Palette and press Enter.
    
- **Choose Environment:** VS Code will automatically detect your Conda environments. Select the desired environment from the list.
    

**3. Use the VS Code Integrated Terminal:**

- **Open Terminal:** You can open the integrated terminal in VS Code by pressing Ctrl+ (backtick) or by going to "View > Terminal" in the menu.
    
- **Conda is Ready!** The terminal will automatically activate your selected Conda environment, so you can run Conda commands directly within VS Code.
    
    - For example, you can use conda install <package_name> to install packages or conda list to view the installed packages in your environment.
        

**4. Additional Tips:**

- **Conda Activation in Status Bar:** VS Code will display the currently active Conda environment in the bottom-left corner of the status bar. You can click on it to switch to a different environment.
    
- **Multiple Terminals:** You can open multiple terminals in VS Code, each with its own separate Conda environment activated. This is helpful if you need to work on multiple projects with different dependencies simultaneously.
    

**Benefits of Integration:**

- **Streamlined Workflow:** You can manage your Conda environments and run Conda commands without leaving VS Code, streamlining your development process.
    
- **Package Management:** Easily install, update, and manage packages within your Conda environments directly from the VS Code terminal.
    
- **Environment Isolation:** Ensure that each project uses its own isolated set of dependencies, preventing conflicts and ensuring consistency.

**The Role of the PATH Environment Variable:**

- **Finding Executables:** The PATH variable tells your operating system where to look for executable files (like the conda command) when you type a command in the terminal or command prompt.
    
- **If Anaconda is not in your PATH:** Your OS won't know where to find the conda executable, and VS Code won't be able to detect your Conda environments.
    

**How to Add Anaconda to your PATH:**

The exact steps vary slightly depending on your operating system:

**Windows:**

1. **Search for "Environment Variables":** Open the Start Menu and search for "Edit the system environment variables."
    
2. **System Properties:** Click on the result that appears.
    
3. **Environment Variables:** In the "System Properties" window, click the "Environment Variables" button.
    
4. **System Variables:** In the "System variables" section, look for a variable named "Path" (or "PATH").
    
    - **If It Exists:** Select "Path" and click "Edit."
        
    - **If It Doesn't Exist:** Click "New" to create a new system variable.
        
5. **Add Anaconda Paths:**
    
    - Click "New" and add the following paths (replace <Your Username> with your actual username):
        
        - C:\Users\<Your Username>\anaconda3
            
        - C:\Users\<Your Username>\anaconda3\Scripts
            
        - C:\Users\<Your Username>\anaconda3\Library\bin
            
6. **Apply Changes:** Click "OK" on all the open windows to save your changes.
    
7. **Restart VS Code:** Restart VS Code to ensure it recognizes the updated PATH environment variable.
Conda channels are online repositories where packages are stored. The default Anaconda channel (defaults) contains a curated set of packages. However, many other community-maintained channels, like conda-forge, provide a wider range of packages.

By specifying the -c conda-forge option, you're telling Conda to look for the frontmatter package in the conda-forge channel.


when files in vscode file explorer are green and have a green 'u' next to them, it's because they haven't yet been commited to git for the first time.


**Yellow with "M" indicates that the file has been modified since your last Git commit.** Git is keeping track of changes in your project, and it's letting you know that these files have been altered but haven't yet been staged for your next commit.

**Here's a breakdown of the common color codes in VS Code's Git integration:**

- **Green:** New files that have not been added to Git yet (untracked).
    
- **Red:** Deleted files.
    
- **Blue:** Files that have been modified and have been staged for your next commit (ready to be included in the snapshot).
    
- **Yellow (with "M"):** Modified files that have **not** been staged yet.

### TEST HEADER MOTHER FUCKERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR