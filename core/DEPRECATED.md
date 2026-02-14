# DEPRECATED

This directory structure is deprecated. The codebase has been migrated to a proper Python package structure.

**New structure:**
- `src/zone_gpt/` - Main package code
- `tests/` - Test suite

**Migration notes:**
- `core/main.py` → `src/zone_gpt/app.py`
- `core/audit.py` → `src/zone_gpt/audit.py`
- `core/routes/` → `src/zone_gpt/routes/`

This directory will be removed in a future update. Please update any references to use the new structure.
