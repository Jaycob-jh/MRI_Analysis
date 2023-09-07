# MRI_Analysis
It contains some MRI processing scripts and analysis.

When using DSI Studio to track and reconstruct white matter fiber tracts, you can follow the steps below:

1. Install DSI Studio: First, you need to download and install the DSI Studio software, the latest version can be found on its official website.

2. Prepare diffusion MRI data: Prepare your diffusion MRI data (including DICOM or NIfTI format), and make sure that the data has been preprocessed, such as correcting distortion and motion estimation.

3. Import diffusion MRI data: In DSI Studio, select "File" -> "Open" and import your diffusion MRI data.

4. Create ROI (Region of Interest): In the "ROIs" tab, select "New ROI" and then select the area of interest in the image, such as the seed region or region of interest. .

5. Set fiber tract tracking parameters: In the "Tracking" tab, set the parameters of fiber tract tracking, such as tracking algorithm, step size, threshold, etc. You can adjust it as needed.

6. Run fiber bundle tracking: Click the "Run" button to start fiber bundle tracking. DSI Studio will trace fiber bundles starting from the seed region according to the parameters you set.

7. Visualize and analyze results: In the "Results" tab, you can view and analyze the results of fiber tract tracing. DSI Studio provides a variety of visualization and analysis tools, such as fiber bundle visualization, fiber bundle length distribution, etc.

Please note that the above steps are just a general operation process, and the specific operations and parameter settings may vary depending on the data and research needs. It is recommended that you refer to the official documentation and tutorials of DSI Studio for more detailed operation steps and code samples.
