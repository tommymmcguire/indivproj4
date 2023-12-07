from flask import Flask, render_template, request, jsonify
from PIL import Image
import requests
import io
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

app = Flask(__name__)


def overlay_image_on_tshirt(generated_image, tshirt_template_path, output_path):
    # Open the t-shirt template and convert it to RGBA if it's not already
    tshirt = Image.open(tshirt_template_path).convert("RGBA")

    # Resize the generated image
    generated_image = generated_image.resize((150, 150))  # Ex. adjust as needed

    # Ensure the generated image is in RGBA mode
    if generated_image.mode != "RGBA":
        generated_image = generated_image.convert("RGBA")

    # Example position, adjust as needed
    position = (200, 200)

    # Paste the generated image onto the t-shirt
    # Use the alpha channel of the generated image as the mask if it exists
    tshirt.paste(generated_image, position, generated_image)

    tshirt.save(output_path)
    return output_path


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/generate-image", methods=["POST"])
def generate_image():
    description = request.form.get("description")

    api_key = os.getenv("OPENAI_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}
    api_url = "https://api.openai.com/v1/images/generations"
    response = requests.post(api_url, headers=headers, json={"prompt": description})

    if response.status_code == 200:
        # The response handling here depends on how DALL-E 2 returns the image.
        image_urls = response.json()["data"]
        first_image_url = image_urls[0]["url"]  # Using the first image URL

        # Download the image from the URL (optional, if needed for processing)
        response = requests.get(first_image_url)
        if response.status_code == 200:
            generated_image = Image.open(io.BytesIO(response.content))
            output_path = "static/output_tshirt.png"
            tshirt_image_path = overlay_image_on_tshirt(
                generated_image, "static/tshirt_template.png", output_path
            )

            return render_template(
                "display_tshirt.html", tshirt_image="output_tshirt.png"
            )
        else:
            return (
                jsonify({"error": "Failed to download the image"}),
                response.status_code,
            )
    else:
        return jsonify({"error": "Failed to generate image"}), response.status_code


if __name__ == "__main__":
    app.run(debug=True)
