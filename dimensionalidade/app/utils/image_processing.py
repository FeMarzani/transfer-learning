import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image, text, font_path="arial.ttf", font_size=30):
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)

    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        font = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = ((pil_image.width - text_width) // 2, 10)

    draw.text(position, text, (255, 255, 255), font=font)

    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

def process_image(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, image_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)

    image_with_text = add_text_to_image(image, "Imagem Original")
    gray_with_text = add_text_to_image(cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR), "Imagem em Cinza")
    binary_with_text = add_text_to_image(cv2.cvtColor(image_binary, cv2.COLOR_GRAY2BGR), "Imagem Binária")

    final_image = cv2.vconcat([image_with_text, gray_with_text, binary_with_text])

    return final_image
