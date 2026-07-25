# Terminal Session Log — Reference

This log captures the actual commands run and their outputs while setting
up this project, kept here as supporting evidence alongside the required
screenshots.

## Repo setup and initial commits (on `main`)
```
$ git clone git@github.com:veeralakumar/herovired.git
$ cd herovired/
$ echo "# Learning Project with HeroVired" > README.md
$ git add .
$ git commit -m "Initial commit for testinggit add ."
[main c7d2e05] Initial commit for testinggit add .
$ git push origin main
   1ed35ed..c7d2e05  main -> main

$ mkdir assignment1
$ cd assignment1/
$ touch README.md   # placeholder, replaced later on dev
$ cd ..
$ git add assignment1/
$ git commit -m "Assignment 1 Submission git commit .!"
[main 9215697] Assignment 1 Submission git commit .!
$ git push
   c7d2e05..9215697  main -> main
```

## Creating the dev branch and environment
```
$ git checkout -b dev
Switched to a new branch 'dev'

$ cd assignment1/
$ python3 -m venv venv
$ vi requirements.txt        # Flask==3.0.3
$ source venv/bin/activate
$ pip install -r requirements.txt
Successfully installed Flask-3.0.3 Jinja2-3.1.6 MarkupSafe-3.0.3 \
  Werkzeug-3.1.8 blinker-1.9.0 click-8.4.2 itsdangerous-2.2.0
```

## Adding .gitignore
```
$ cat > .gitignore << 'EOF'
venv/
__pycache__/
*.pyc
.env
.DS_Store
EOF

$ git status
On branch dev
Untracked files:
	.gitignore
	app.py
	requirements.txt
```
Confirms `venv/` is correctly excluded from tracking before the first commit.

## Known issue caught and corrected
An early run showed the app serving on port 5001 with "Welcome to the
Infra Inventory App" — this was the bonus extension app
(`extension_v1_app.py`) mistakenly saved as `app.py`. It was identified
via the startup banner and replaced with the correct password manager
`app.py`, which serves on port 5000 with `/`, `/health`, `/add`,
`/get/<username>`.

## Branch comparison before merging dev → main
```
$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```
GitHub showed `dev` as "1 commit ahead, 2 commits behind main" — the 2
commits behind are the two setup commits made directly on `main` (initial
README, assignment1 placeholder) *before* `dev` was branched off. No
conflict expected on merge.
