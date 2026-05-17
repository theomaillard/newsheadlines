# Contributing

Feel free to contribute by adding new sources, better parsing, etc...

## Pull Requests

1. Fork the main repository by clicking on the 'Fork' button

2. Clone your fork and add the main repository as `upstream`
```bash
git clone https://github.com/<your-github-user>/newsheadlines.git
cd newsheadlines
git remote add upstream https://github.com/theomaillard/newsheadlines
```

3. Create a branch for your own changes
```bash
git checkout -b my-feature
```

4. Get your development environment by running
```bash
pip install -e .
```

5. Add changes and commit
```bash
git add modified_files
git commit -m "commit message here"
```

6. Sync with base repository
```bash
git fetch upstream
git rebase upstream/main
```

7. Push changes
```bash
git push -u origin my-feature
```

## Tests

Use PyTest for running tests.

1. Install PyTest
```bash
pip install pytest
```
2. Run tests
```bash
pytest
```
