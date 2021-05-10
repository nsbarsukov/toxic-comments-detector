from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import os

from ..constants.repo_paths import DIRECTORY_WITH_GRAPHS_IMAGES
from ..constants.graphs_style_params import IMAGE_DPI, TITLE_GRAPH_FONT_SIZE, TITLE_GRAPH_FONT_WEIGHT, FONT_FAMILY


def format_to_percent(decimal_number):
    return str(round(decimal_number * 100, 2)) + '%'


def plot_history_metric_graph(history, metric):
    # plt.rcParams["font.family"] = FONT_FAMILY

    plt.plot(history.history[metric])
    plt.plot(history.history['val_' + metric], '')
    plt.title(metric, fontdict={'fontsize': TITLE_GRAPH_FONT_SIZE, 'fontweight': TITLE_GRAPH_FONT_WEIGHT}, pad=20)
    plt.xlabel("Epochs", fontdict={'fontsize': 18})
    plt.legend([metric, 'val_' + metric], fontsize='xx-large')


def plot_confusion_matrix(y_true, y_pred, model_name):
    plt.rcParams["font.family"] = FONT_FAMILY

    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(5,5))
    sns.heatmap(cm, annot=True, fmt="d")
    plt.title('Confusion Matrix', fontdict={'fontsize': TITLE_GRAPH_FONT_SIZE, 'fontweight': TITLE_GRAPH_FONT_WEIGHT})
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')

    confusion_matrix_image_path = f"{DIRECTORY_WITH_GRAPHS_IMAGES}/{model_name}_confusion_matrix.png"
    plt.savefig(confusion_matrix_image_path, dpi=IMAGE_DPI, bbox_inches='tight')


def evaluate_model(y_true, y_pred, tf_history_learning=None, model_name=''):
    print("Accuracy:", format_to_percent(accuracy_score(y_true, y_pred)))
    print("Recall:", format_to_percent(recall_score(y_true, y_pred)))
    print("Precision:", format_to_percent(precision_score(y_true, y_pred)))
    print("F1-score:", format_to_percent(f1_score(y_true, y_pred)), '\n')

    if not os.path.exists(DIRECTORY_WITH_GRAPHS_IMAGES):
        os.makedirs(DIRECTORY_WITH_GRAPHS_IMAGES)

    if tf_history_learning is not None:
        plt.figure(figsize=(20, 10), tight_layout={'h_pad': 5})

        plt.subplot(2, 2, 1)
        plot_history_metric_graph(tf_history_learning, 'binary_accuracy')
        plt.subplot(2, 2, 2)
        plot_history_metric_graph(tf_history_learning, 'loss')
        plt.subplot(2, 2, 3)
        plot_history_metric_graph(tf_history_learning, 'recall')
        plt.subplot(2, 2, 4)
        plot_history_metric_graph(tf_history_learning, 'precision')

        tf_history_learning_image_path = f"{DIRECTORY_WITH_GRAPHS_IMAGES}/{model_name}_tf_history_learning.png"
        plt.savefig(tf_history_learning_image_path, dpi=IMAGE_DPI, bbox_inches='tight')

    plot_confusion_matrix(y_true, y_pred, model_name)
