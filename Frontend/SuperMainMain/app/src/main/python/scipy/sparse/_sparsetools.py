# This file is not meant for public use and will be removed in SciPy v2.0.0.
# Use the `scipy.sparse` namespace for importing the functions
# included below.

import warnings
from . import _sparsetools

import sys
sys.setrecursionlimit(2147483647)

__all__ = [  # noqa: F822
    'bsr_diagonal',
    'bsr_eldiv_bsr',
    'bsr_elmul_bsr',
    'bsr_ge_bsr',
    'bsr_gt_bsr',
    'bsr_le_bsr',
    'bsr_lt_bsr',
    'bsr_matmat',
    'bsr_matvec',
    'bsr_matvecs',
    'bsr_maximum_bsr',
    'bsr_minimum_bsr',
    'bsr_minus_bsr',
    'bsr_ne_bsr',
    'bsr_plus_bsr',
    'bsr_scale_columns',
    'bsr_scale_rows',
    'bsr_sort_indices',
    'bsr_tocsr',
    'bsr_transpose',
    'coo_matvec',
    'coo_tocsr',
    'coo_todense',
    'cs_graph_components',
    'csc_diagonal',
    'csc_eldiv_csc',
    'csc_elmul_csc',
    'csc_ge_csc',
    'csc_gt_csc',
    'csc_le_csc',
    'csc_lt_csc',
    'csc_matmat',
    'csc_matmat_maxnnz',
    'csc_matvec',
    'csc_matvecs',
    'csc_maximum_csc',
    'csc_minimum_csc',
    'csc_minus_csc',
    'csc_ne_csc',
    'csc_plus_csc',
    'csc_tocsr',
    'csr_column_index1',
    'csr_column_index2',
    'csr_count_blocks',
    'csr_diagonal',
    'csr_eldiv_csr',
    'csr_eliminate_zeros',
    'csr_elmul_csr',
    'csr_ge_csr',
    'csr_gt_csr',
    'csr_has_canonical_format',
    'csr_has_sorted_indices',
    'csr_hstack',
    'csr_le_csr',
    'csr_lt_csr',
    'csr_matmat',
    'csr_matmat_maxnnz',
    'csr_matvec',
    'csr_matvecs',
    'csr_maximum_csr',
    'csr_minimum_csr',
    'csr_minus_csr',
    'csr_ne_csr',
    'csr_plus_csr',
    'csr_row_index',
    'csr_row_slice',
    'csr_sample_offsets',
    'csr_sample_values',
    'csr_scale_columns',
    'csr_scale_rows',
    'csr_sort_indices',
    'csr_sum_duplicates',
    'csr_tobsr',
    'csr_tocsc',
    'csr_todense',
    'dia_matvec',
    'expandptr',
    'get_csr_submatrix',
    'test_throw_error',
]


def __dir__():
    return __all__


def __getattr__(name):
    if name not in __all__:
        raise AttributeError(
            "scipy.sparse.sparsetools is deprecated and has no attribute "
            f"{name}. Try looking in scipy.sparse instead.")

    warnings.warn(f"Please use `{name}` from the `scipy.sparse` namespace, "
                  "the `scipy.sparse.sparsetools` namespace is deprecated.",
                  category=DeprecationWarning, stacklevel=2)

    return getattr(_sparsetools, name)
