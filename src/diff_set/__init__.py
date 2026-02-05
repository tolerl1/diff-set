'''
diff-set

A backend-agnostic diff engine for comparing two datasets and determining
which records are new, changed, or deleted. Designed for syncing external
systems or performing pure comparison.

Primary API:
    diff() — compute differences between source and target datasets.
'''

from .diff import diff
from .models import (
	DiffError,
	DataTypeMismatchError,
	MissingColumnError,
	NewItem,
	ChangedItem,
	DeletedItem,
	DiffResult,
)

__all__ = [
	'diff',
	'DiffError',
	'DataTypeMismatchError',
	'MissingColumnError',
	'NewItem',
	'ChangedItem',
	'DeletedItem',
	'DiffResult',
]
