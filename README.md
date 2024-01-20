<h1 align="center" id="mfilipa97-title" style="font-size: 100px; text-decoration: none;"> <img src="https://media.giphy.com/media/xcFJX6T9z2iqiB9Ud9/giphy.gif" width="40"> Photo Editor <img src="https://media.giphy.com/media/YrTAl4OXv5DgBeAHmC/giphy.gif" width="40"> </h1>

 This Python script, utilizing the Pillow (PIL) library, is designed for image-processing tasks. It enhances images by applying a sequence of operations and saves the edited versions in a specified directory.

<h3>Features:</h3>
<h4>Sharpness and Black & White:</h4>

Applies a sharpening filter to enhance image details.
Converts the image to black and white for a classic aesthetic.

<h4>Contrast Adjustment:</h4>

Enhances the contrast of the image to improve visibility.

<h4>Output Directory:</h4>

Creates an output directory for the processed images, if it doesn't exist.


<h1>
How to Use:</h1>
<h3>Install Dependencies:</h3>
Ensure that the  <a href="https://pillow.readthedocs.io/en/stable/index.html" target="_blank" rel="noreferrer">  Pillow  library </a> is installed. You can install it using pip install Pillow.


```python:
pip install Pillow
```

<h3>Set Input and Output Paths:</h3>

<p>Modify the path and pathOut variables to point to your input (original photos) and output (edited photos) directories.<p>

```python:
path: Absolute path to the directory containing original photos.
pathOut: Absolute path to the directory where edited photos will be saved.
```


<h3>Run the Script:</h3>

<p>Execute the script, and it will process each image in the input directory, applying the specified enhancements, and save the edited images in the output directory.</p>
