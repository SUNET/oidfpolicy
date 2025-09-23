def merge_policies(tapolicy: str, iapolicy: str) -> str:
    """Merges tapolicy on top of iapolicy and returns the merged policy.

    :param tapolicy: JSON Policy from Trust Anchor in str
    :param iapolicy: JSON Policy from Trust Anchor in str

    :return: str representation of merged policy.
    """
