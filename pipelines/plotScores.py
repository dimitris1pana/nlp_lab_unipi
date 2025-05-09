import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

def scoreplots(precision, recall, f1):
    """
    Function to plot precision, recall, and F1 score.

    Args:
        precision (list): List of precision scores.
        recall (list): List of recall scores.
        f1 (list): List of F1 scores.
    """
    scores = {
        'Precision': precision,
        'Recall': recall,
        'F1': f1
    }

    # Create simple bar plot
    plt.figure(figsize=(8, 5))
    plt.bar(scores.keys(), scores.values())

    # Add labels and title
    plt.title('BERT Scores')
    plt.ylabel('Score')

    # Add value labels on top of bars
    for i, v in enumerate(scores.values()):
        plt.text(i, v, f'{v:.3f}', ha='center', va='bottom')

    # Set y-axis limits for better visualization
    plt.ylim(0, 1)

    plt.show()#show bert scores

    # results['precision'][0]/results['recall'][0]/results['f1'][0]