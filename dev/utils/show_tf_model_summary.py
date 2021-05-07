import tensorflow as tf
from IPython.display import Image, display

from dev import IMAGE_DPI


def show_tf_model_summary(model: tf.keras.models.Model):
    model.summary()

    graph_summary_image_path = f".graphsImages/{model.name}_graph_summary.png"
    tf.keras.utils.plot_model(
        model,
        to_file=graph_summary_image_path,
        show_shapes=True,
        dpi=IMAGE_DPI
    )

    display(Image(filename=graph_summary_image_path))
