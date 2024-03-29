"""
This script is used to edit a paint by numbers image:
- Fill the contours with a specified color
- Update borders' color
- Remove numbers inside contours

Input images can be generated in https://app.paint-by-number.com/index.html#.
"""
import cv2
import numpy as np
from sklearn.cluster import KMeans

BASE_PATH = "./"


def process_image_using_sklearn(
    input_path,
    output_path,
    fill_color=(255, 255, 255),
    border_color=(0, 0, 0),
    remove_numbers=True,
):
    # Read the image
    img = cv2.imread(input_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold the image to get contours
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    # contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Create an empty mask
    mask = np.zeros_like(gray)

    for contour in contours:
        # Draw contours on the mask
        cv2.drawContours(mask, [contour], 0, 255, thickness=cv2.FILLED)

    # Find the clusters in the image
    kmeans = KMeans(n_clusters=2, random_state=0, n_init=10)
    kmeans.fit(gray[mask == 255].reshape(-1, 1))

    # Get the cluster with the lower intensity (presumably the background)
    background_cluster = np.argmin(kmeans.cluster_centers_)

    # Set all pixels in the background cluster to white
    img[mask == 255] = [255, 255, 255] if background_cluster == 0 else [0, 0, 0]


    # Draw borders with specified color
    cv2.drawContours(img, contours, -1, border_color, 1)


    # Save the processed image
    cv2.imwrite(output_path, img)


# Example usage
for name, color in [
    # ('red', (0,0,255)),
    # ('blue', (255,0,0)),
    # ('green', (0,255,0)),
    # ('yellow', (0,255,255)),
    ('light', (200, 255, 255)),
    ]:
    process_image_using_sklearn(
        "zahra.png", f"zahra_output_image_sklearn-{name}.jpg", border_color=color
    )


def replace_non_white(input_path, output_path, replacement_color=(191, 207, 228)):
    # Read the image
    img = cv2.imread(input_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold the image to get non-white pixels
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    # Create a 3-channel image with the replacement color
    replacement_color = np.array(replacement_color, dtype=np.uint8)
    img_colored = np.zeros_like(img)
    img_colored[:, :] = replacement_color

    # Replace non-white pixels in the original image with the replacement color
    result = np.where(thresh[:, :, None] > 0, img_colored, img)

    # Save the processed image
    cv2.imwrite(output_path, result)

# Example usage
replace_non_white("zahra_output_image_sklearn-light.jpg", "zahra_color_border.jpg", replacement_color=(208, 253, 255))


# def replace_non_white_with_beige(input_path, output_path, replacement_color=(191, 207, 228)):
#     # Read the image
#     img = cv2.imread(input_path)

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Threshold the image to get the black lines
#     _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

#     # Create a 3-channel image with the replacement color
#     replacement_color = np.array(replacement_color, dtype=np.uint8)
#     img_colored = np.zeros_like(img)
#     img_colored[:, :] = replacement_color

#     # Replace black lines with the replacement color
#     result = np.where(thresh[:, :, None] > 0, img_colored, img)

#     # Save the processed image
#     cv2.imwrite(output_path, result)



# # Example usage
# replace_non_white_with_beige("zahra_output_image_sklearn.jpg", "zahra_output.jpg")


# def replace_non_white_with_beige(input_path, output_path, beige_color=(191, 207, 228)):
#     # Read the image
#     img = cv2.imread(input_path)

#     img[img != 255] = 0 # change everything to black where pixel is not white

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Threshold the image to get the black lines
#     _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

#     # Create a 3-channel image with beige color
#     img_colored = np.zeros_like(img)
#     img_colored[:, :] = beige_color

#     # Replace non-white pixels in the original image with beige color
#     result = np.where(thresh[:, :, None] > 0, img_colored, img)

#     # Save the processed image
#     cv2.imwrite(output_path, result)

# # Example usage
# replace_non_white_with_beige("zahra_output_image_sklearn.jpg", "zahra_output2.jpg")