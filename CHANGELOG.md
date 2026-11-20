# Unreleased

- Updated `oidfed_metadata_policy` from 0.7.0 to 0.9.0. Client scope policies
  now operate on individual tokens in the space-delimited `scope` string.
  Callers must omit `metadata_policy` when a statement has no policy. Passing
  an explicitly empty policy claim to `apply_policy` raises `RuntimeError`.
- Updated PyO3 to 0.30.1 and the minimum maturin version to 1.9.4.

<a id='changelog-0.1.0'></a>
# 0.1.0 — 2025-12-22

## Added

- Uses latest `0.7.0` of `oidf_metadata_policy` as dependency.
