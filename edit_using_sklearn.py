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
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

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
border_color = (191, 207, 228)
process_image_using_sklearn(
    "zahra.png", "zahra_output_image_sklearn.jpg", border_color=border_color
)
