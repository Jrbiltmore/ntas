import os
import requests
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("update_ntas_image.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def fetch_ntas_data(xml_feed_url):
    """Fetches the NTAS XML data from the specified URL."""
    try:
        response = requests.get(xml_feed_url)
        response.raise_for_status()
        logging.info("Successfully fetched NTAS data.")
        return response.content
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching NTAS data: {e}")
        raise

def parse_ntas_data(xml_data):
    """Parses NTAS XML data and extracts the latest alert information."""
    try:
        root = ET.fromstring(xml_data)
        alerts = root.findall('alert')
        if alerts:
            current_alert = alerts[0]  # Assuming we want the most recent alert
            alert_type = current_alert.get('type', 'Unknown')
            alert_summary = current_alert.find('summary').text.strip() if current_alert.find('summary') is not None else "No summary available."
            logging.info(f"Found alert: {alert_type} - {alert_summary}")
            return alert_type, alert_summary
        else:
            logging.info("No current advisories.")
            return "No Current Advisories", "There are no active NTAS advisories at this time."
    except ET.ParseError as e:
        logging.error(f"Error parsing NTAS data: {e}")
        raise

def generate_image(alert_type, alert_summary, image_path):
    """Generates an image with the alert information."""
    try:
        # Create an image with white background
        image = Image.new('RGB', (400, 200), color='white')
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        # Draw text on the image
        draw.text((10, 10), f"Alert Type: {alert_type}", fill="black", font=font)
        draw.text((10, 50), f"Summary: {alert_summary}", fill="black", font=font)

        # Save the image
        image.save(image_path)
        logging.info(f"Image successfully saved to {image_path}.")
    except Exception as e:
        logging.error(f"Error generating image: {e}")
        raise

def main():
    """Main function to execute the NTAS update process."""
    xml_feed_url = os.getenv('XML_FEED_URL')
    image_path = os.getenv('IMAGE_PATH', 'images/ntas_current_status.png')

    logging.info("Starting NTAS image update process.")
    
    try:
        # Fetch, parse, and generate image
        xml_data = fetch_ntas_data(xml_feed_url)
        alert_type, alert_summary = parse_ntas_data(xml_data)
        generate_image(alert_type, alert_summary, image_path)
        logging.info("NTAS image update process completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred in the NTAS image update process: {e}")

if __name__ == "__main__":
    main()
