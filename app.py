from flask import Flask, render_template, request, jsonify
from PIL import Image
import requests
import io

app = Flask(__name__)

def overlay_image_on_tshirt(generated_image, tshirt_template_path, output_path):
    tshirt = Image.open(tshirt_template_path)
    generated_image = generated_image.resize((300, 300))  # Example size, adjust as needed

    # Example position, adjust as needed
    position = (100, 100)  
    tshirt.paste(generated_image, position, generated_image)
    tshirt.save(output_path)
    return output_path

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    description = request.form.get('description')

    # Replace with actual DALL-E 2 API call
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    api_url = "https://api.openai.com/v1/dalle-2/generate"
    response = requests.post(api_url, headers=headers, json={"prompt": description})

    if response.status_code == 200:
        # The response handling here depends on how DALL-E 2 returns the image.
        # You might receive a URL, binary data, etc. Adjust the following line accordingly.
        generated_image_data = response.json()["image_data"]  # Adjust based on actual response format

        # Convert the image data to a PIL Image object
        generated_image = Image.open(io.BytesIO(generated_image_data))

        # Overlay the image onto the t-shirt
        output_path = 'static/output_tshirt.png'
        tshirt_image_path = overlay_image_on_tshirt(generated_image, 'static/tshirt_template.png', output_path)

        return render_template('display_tshirt.html', tshirt_image=tshirt_image_path)
    else:
        return jsonify({"error": "Failed to generate image"}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)
