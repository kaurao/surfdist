import nibabel as nib
import numpy as np


def load_freesurfer_label(annot_input, label_name, cortex=None):
    """
    Get source node list for freesurfer label.
    """

    if cortex:
        print("Warning: cortex is not used to load the freesurfer label")

    labels, color_table, names = nib.freesurfer.read_annot(annot_input)
    label_index = names.index(label_name)
    label_nodes = np.array(np.where(np.in1d(labels, label_index)), dtype=np.int32)

    return label_nodes


def get_freesurfer_label(annot_input):
    """
    Print freesurfer label names.
    """
    labels, color_table, names = nib.freesurfer.read_annot(annot_input)
    print names
