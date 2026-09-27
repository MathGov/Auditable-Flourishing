# Preserved publication provenance

ORIGINAL_REPOSITORY_SHA256.json records SHA-256 hashes of files in the repository immediately before this publication-maintenance change, read from Git HEAD. Text files stored with LF are normalized from CRLF to LF when checking a Windows checkout; binary files are hashed exactly. Intentional changes to repository-level publication guidance are listed explicitly in scripts/verify_publication.py. Research files retain their original contents.

The separate original release ZIP is checked byte-for-byte against its fixed SHA-256 and its unchanged full verifier runs in an isolated temporary directory. These are artifact integrity checks, not new empirical validation or a new visual inspection of the papers.
