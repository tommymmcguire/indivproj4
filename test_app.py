import unittest
from unittest.mock import patch
from app import app, overlay_image_on_tshirt
from PIL import Image
import io
import os

class TestDalleIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('requests.post')
    def test_generate_image(self, mock_post):
        # Mock the response of DALL-E API
        mock_image = Image.new('RGB', (100, 100))
        img_byte_arr = io.BytesIO()
        mock_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "data": [{"url": "https://..."}]
        }

        # Mock requests.get for image download
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.content = img_byte_arr

            response = self.app.post('/generate-image', data={"description": "test"})
            self.assertEqual(response.status_code, 200)
            # Add more assertions here as necessary

class TestImageOverlay(unittest.TestCase):
    def test_image_overlay(self):
        # Create a mock generated image and a mock t-shirt template
        generated_image = Image.new('RGB', (100, 100))
        tshirt_template = Image.new('RGB', (300, 300))
        tshirt_template_path = 'temp_tshirt_template.png'
        tshirt_template.save(tshirt_template_path)

        output_path = 'temp_output.png'
        overlay_image_on_tshirt(generated_image, tshirt_template_path, output_path)
        
        # Check if the output image exists and has the properties you expect
        self.assertTrue(os.path.exists(output_path))
        # Add more assertions as necessary

        # Cleanup: Remove the temporary files after the test
        os.remove(tshirt_template_path)
        os.remove(output_path)

if __name__ == '__main__':
    unittest.main()
