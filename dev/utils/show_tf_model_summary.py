import os
import tensorflow as tf
from IPython.display import Image, display

from ..constants.graphs_style_params import IMAGE_DPI
from ..constants.repo_paths import DIRECTORY_WITH_GRAPHS_IMAGES


def show_tf_model_summary(model: tf.keras.models.Model):
    model.summary()

    if not os.path.exists(DIRECTORY_WITH_GRAPHS_IMAGES):
        os.makedirs(DIRECTORY_WITH_GRAPHS_IMAGES)

    graph_summary_image_path = f"{DIRECTORY_WITH_GRAPHS_IMAGES}/{model.name}_graph_summary.png"
    tf.keras.utils.plot_model(
        model,
        to_file=graph_summary_image_path,
        show_shapes=True,
        dpi=IMAGE_DPI
    )

    display(Image(filename=graph_summary_image_path))
