from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


def format_to_percent(decimal_number):
    return str(round(decimal_number * 100, 2)) + '%'


def plot_history_metric_graph(history, metric):
    plt.plot(history.history[metric])
    plt.plot(history.history['val_' + metric], '')
    plt.title(metric, fontdict={'fontsize': 18, 'fontweight': 500}, pad=20)
    plt.xlabel("Epochs")
    plt.legend([metric, 'val_' + metric])


def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(5,5))
    sns.heatmap(cm, annot=True, fmt="d")
    plt.title('Confusion Matrix', fontdict={'fontsize': 18, 'fontweight': 500})
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')


def evaluate_model(y_true, y_pred, tf_history_learning=None):
    print("Accuracy:", format_to_percent(accuracy_score(y_true, y_pred)))
    print("Recall:", format_to_percent(recall_score(y_true, y_pred)))
    print("Precision:", format_to_percent(precision_score(y_true, y_pred)))
    print("F1-score:", format_to_percent(f1_score(y_true, y_pred)), '\n')

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

    plot_confusion_matrix(y_true, y_pred)
