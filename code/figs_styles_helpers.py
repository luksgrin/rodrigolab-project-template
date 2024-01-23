import logging
import matplotlib as mpl

# Set standard desired parameters for matplotlib figures
STANDARD_PARAMS = {
    "font.sans-serif" : "Helvetica",
    "axes.linewidth" : 2,
    "axes.labelsize" : 22,
    "axes.spines.top" : False,
    "axes.spines.right" : False,
    "font.size" : 20,
    "xtick.major.width" : 2,
    "ytick.major.width" : 2,
    "xtick.major.size" : 6,
    "ytick.major.size" : 6,
    "legend.frameon" : False
}

def set_style_globally(styles: dict=None):
    """
    Set the standard parameters for matplotlib figures.

    :param styles: An optional dictionary of matplotlib parameters to set on top of the standard parameters.
    """
    
    logging.getLogger('matplotlib.font_manager').disabled = True
    for key, value in STANDARD_PARAMS.items():
        mpl.rcParams[key] = value

    if styles:
        for key, value in styles.items():
            mpl.rcParams[key] = value