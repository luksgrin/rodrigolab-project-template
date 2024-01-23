import pandas as pd
import warnings
from figs_styles_helpers import set_style_globally

# Set standard desired parameters for matplotlib figures
set_style_globally()

# Ignore pandas performance warnings
warnings.simplefilter(
    action="ignore",
    category=pd.errors.PerformanceWarning
)

########################################################
#                      Classes                         #
########################################################

########################################################
#               Data handling functions                #
########################################################

########################################################
#                    Plot functions                    #
########################################################
