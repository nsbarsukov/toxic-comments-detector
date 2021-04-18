from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt


def format_to_percent(decimal_number):
    return str(round(decimal_number * 100, 2)) + '%'


def plot_history_metric_graph(history, metric):
    plt.plot(history.history[metric])
    plt.plot(history.history['val_' + metric], '')
    plt.title(metric, fontdict={'fontsize': 18, 'fontweight': 500}, pad=20)
    plt.xlabel("Epochs")
    plt.legend([metric, 'val_' + metric])


def evaluate_model(y_true, y_pred, tf_history_learning=None):
    print("Accuracy:", format_to_percent(accuracy_score(y_true, y_pred)))
    print("Recall:", format_to_percent(recall_score(y_true, y_pred)))
    print("Precision:", format_to_percent(precision_score(y_true, y_pred)))
    print("F1-score:", format_to_percent(f1_score(y_true, y_pred)), '\n')

    print('Confusion matrix:')
    print(confusion_matrix(y_true=y_true, y_pred=y_pred))

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