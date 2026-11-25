"""Selected train/validation split check from R.HOPE.
The evaluation helper below is a generic portfolio adaptation of the original metric calculation.
Use synthetic or authorized data only; no model or counseling records are included.
"""
from sklearn.metrics import precision_recall_fscore_support


def validate_subject_split(train_rows, validation_rows):
    train_ids = {r['subject_id'] for r in train_rows}
    valid_ids = {r['subject_id'] for r in validation_rows}
    if '' in train_ids or '' in valid_ids or 'UNKNOWN' in train_ids or 'UNKNOWN' in valid_ids:
        raise ValueError('Missing subject IDs prevent reliable split validation.')
    if train_ids & valid_ids:
        raise ValueError('Train/Validation subject overlap detected; re-split before training.')


def evaluate_binary_predictions(truth, pred):
    """Return binary classification metrics for supplied labels and predictions."""
    precision, recall, f1, _ = precision_recall_fscore_support(
        truth, pred, average='binary', zero_division=0)
    return {
        'precision': round(float(precision), 4),
        'recall': round(float(recall), 4),
        'f1': round(float(f1), 4),
    }
