# NTAS Alert Image Updater

![National Terrorism Advisory System](https://username.github.io/repo-name/images/ntas_current_status.png)

## Overview

The **NTAS Alert Image Updater** is a GitHub repository designed to dynamically fetch and display the current National Terrorism Advisory System (NTAS) alert status. This repository utilizes GitHub Actions to automatically fetch NTAS XML data every hour, process the data, and update an image that reflects the most recent alert status. The updated image can be embedded in various web pages or applications to provide real-time alert information.

## Features

- **Automated Data Fetching**: Uses GitHub Actions to fetch NTAS alert data from the official Department of Homeland Security XML feed every hour.
- **Dynamic Image Generation**: Generates an image reflecting the current NTAS alert status, which is automatically updated in the repository.
- **Error Handling and Logging**: Implements robust error handling and logging for reliable performance.
- **Slack Notifications**: Sends a notification to a specified Slack channel if the workflow fails, ensuring prompt attention to issues.
- **Secure Configuration**: Uses GitHub Secrets to securely manage sensitive information such as email addresses and Slack webhook URLs.

## Setup Instructions

### Prerequisites

- A GitHub account
- Basic knowledge of Git and GitHub Actions
- Python 3.9 or later installed locally for development

### Repository Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jrbiltmore/ntas.git
   cd repo-name
Set Up GitHub Secrets:

Go to the repository settings on GitHub.
Navigate to Secrets and variables > Actions.
Add the following secrets:
GIT_COMMIT_EMAIL: Your GitHub email used for committing updates.
GIT_COMMIT_NAME: Your GitHub username used for committing updates.
SLACK_WEBHOOK_URL: The webhook URL for your Slack channel to receive notifications.
Configure GitHub Actions:

The workflow file is located at .github/workflows/update_image.yml.
This file is already set up to run on an hourly schedule. You can adjust the schedule by modifying the cron expression in the workflow file.
Install Python Dependencies:

Create a requirements.txt file if it does not exist:
plaintext
Always show details

Copy code
requests
pillow
Install the dependencies:
bash
Always show details

Copy code
pip install -r requirements.txt
Run the Script Locally (Optional):

You can test the script locally by setting the environment variables and running the script:
bash
Always show details

Copy code
export XML_FEED_URL="http://www.dhs.gov/ntas/1.1/feed.xml"
export IMAGE_PATH="images/ntas_current_status.png"
python scripts/update_ntas_image.py
Usage
Once set up, the repository automatically updates the NTAS alert image every hour. You can embed this image in your GitHub profile or any webpage by linking to the image URL provided by GitHub Pages.

Embed Example
Use the following Markdown to embed the image:

markdown
Always show details

Copy code
[![National Terrorism Advisory System](https://jrbiltmore.github.io/ntas/images/ntas_current_status.png)](https://www.dhs.gov/ntas/)
Replace username and repo-name with your GitHub username and repository name.

Contributing
Contributions are welcome! Please follow these steps:

Fork the Repository: Click the 'Fork' button at the top right of this page.
Clone Your Fork: Clone your forked repository to your local machine.
Create a Branch: Create a new branch for your feature or bug fix.
Make Your Changes: Implement your changes and commit them.
Push to GitHub: Push your changes to your forked repository.
Submit a Pull Request: Create a pull request to have your changes reviewed and merged.
License
This repository is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
Department of Homeland Security for providing the NTAS alert data.
GitHub Actions for enabling automated workflows.
If you have any questions or need further assistance, feel free to open an issue or contact me directly
