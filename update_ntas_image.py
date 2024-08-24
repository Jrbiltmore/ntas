import requests
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
image.save('ntas_current_status.png')
