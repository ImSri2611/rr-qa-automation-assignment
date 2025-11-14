# RR QA Automation Assignment — Playwright + pytest

**Maintainer:** Srinivasan  
**Purpose:** Automated UI tests for the TMDB demo site used in the QA assignment.

## What this repo contains
- Playwright (Python) + pytest test suite
- Smoke, Filters/Search, Pagination tests
- HTML reporting, screenshots on failures
- CI workflow for GitHub Actions

## Quick setup (Windows / macOS / Linux)
```bash
# clone
git clone https://github.com/ImSri2611/rr-qa-automation-assignment.git
cd rr-qa-automation-assignment

# create virtualenv
python -m venv .venv
# mac / linux
source .venv/bin/activate
# windows (PowerShell)
.venv\Scripts\Activate.ps1

# install deps
pip install --upgrade pip
pip install -r requirements.txt

# install Playwright browsers
playwright install
s