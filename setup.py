import os

# Define the directory structure
folders = [
    ".github/workflows",
    "images",
    "scripts"
]

# Create directories
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Define file contents
workflow_content = """name: Update NTAS Image

on:
  schedule:
    - cron: '0 * * * *'  # Runs every hour
  workflow_dispatch:  # Allows manual triggering

jobs:
  update-image:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install requests pillow

      - name: Fetch and update NTAS image
        run: |
          python scripts/update_ntas_image.py
          git config --global user.email "your-email@example.com"
          git config --global user.name "Your Name"
          git add images/ntas_current_status.png
          git commit -m "Update NTAS image"
          git push
"""

python_script_content = """import requests
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

# Fetch the NTAS XML data
response = requests.get("http://www.dhs.gov/ntas/1.1/feed.xml")
xml_data = response.content

# Parse the XML data
root = ET.fromstring(xml_data)
alerts = root.findall('alert')

# Determine the current alert status
if alerts:
    current_alert = alerts[0]  # Assuming we want the most recent alert
    alert_type = current_alert.get('type')
    alert_summary = current_alert.find('summary').text.strip()
else:
    alert_type = "No Current Advisories"
    alert_summary = "There are no active NTAS advisories at this time."

# Create an image based on the alert type
image = Image.new('RGB', (300, 100), color='white')
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

draw.text((10, 10), f"Alert Type: {alert_type}", fill="black", font=font)
draw.text((10, 50), f"Summary: {alert_summary}", fill="black", font=font)

# Save the image
image.save('images/ntas_current_status.png')
"""

readme_content = """# NTAS Alert System

![National Terrorism Advisory System](https://username.github.io/repo-name/images/ntas_current_status.png)

This repository dynamically updates an image displaying the current NTAS alert status using GitHub Actions.
"""

gitignore_content = """# Ignore Python cache files
__pycache__/
*.py[cod]

# Ignore local virtual environment
venv/
"""

# Create files with specified content
with open(".github/workflows/update_image.yml", "w") as file:
    file.write(workflow_content)

with open("scripts/update_ntas_image.py", "w") as file:
    file.write(python_script_content)

with open("README.md", "w") as file:
    file.write(readme_content)

with open(".gitignore", "w") as file:
    file.write(gitignore_content)

# Check directory structure
os.listdir("."), os.listdir(".github/workflows"), os.listdir("images"), os.listdir("scripts")
