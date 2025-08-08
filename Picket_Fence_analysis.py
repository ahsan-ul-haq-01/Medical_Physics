## import the liberary
from pylinac import PicketFence

#load the picket fence image
# You can replace 'mypf.dcm' with the path to your DICOM file
pf = PicketFence("mypf.dcm")

# Analyze the picket fence image with specified tolerances
# Adjust the tolerance and action_tolerance as needed
pf.analyze(tolerance=0.5, action_tolerance=0.25)

# Print the results of the analysis
print(pf.results())

# Plot the analyzed image with the picket fence results
pf.plot_analyzed_image()

# Optionally, you can save the results to a PDF
# This will create a PDF file with the analysis results and the plotted image
pf.publish_pdf()
