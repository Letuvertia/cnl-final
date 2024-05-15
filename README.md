# LocaSync
極短距離的即時通訊社群軟體

## System Design
There are 3 docker containers in this design, `db`, `backend` and `frontend`.

1. `db`

Run the FreeRadius server. `backend` accesses the server within the internal network on port `1812`.

2. `backend`

Run the backend server on http://localhost:5000. `backend` provides APIs for `frontend` to login, getting message feeds, and sending new messages from users. The API server is built with Flask.

3. `frontend`

Run the frontend server on http://localhost:5173. `frontend` serves the LocaSync website for the browser to access. The website is built with Vue.js.

## Quick Start Up
1. Install Docker
2. Run `./build.sh`
2. Run `./run.sh`

## Notes for Developers
**大家看這裡！！**

### Use branch!

Open a new branch and develop features (or add new files if needed) in the corresponding folder. When you're finished, open a pull request and fix merge conflict first before merging the branch into the main branch.


```bash
# Create a new branch
git checkout -b "your-new-branch-name"

# If you finished and want to merge the branch to the main,
# 1. Merge the main into your branch first and resolve conflicts.
git checkout "your-branch-name"
git merge main

# 2. Open a pull request on Github (https://github.com/Letuvertia/cnl-final/pulls)

# 3. Ask other teammates to review your branch before you merge.

# 4. If everything is good, merge the branch on the Github by pressing the merge button. This will close the pull request at the same time.
```

### (Optinal) Develop on Local
If you're developing a feature that is only on `backend` or `frontend` side, it is maybe easier to use local environment instead of the docker environment, which connects everything and is more likely to have bugs.

Here's how to install the dependencie on the local environment:

1. `backend`

Install Python and execute files in `./backend`.

```bash
python3 backend/main.py
```

To test an API, use `curl`.

```bash
# This is an example API `/userdata` with one argument `uid`.
curl "http://localhost:5000/userdata?uid=123"
```

2. `frontend`

Install Node.js and run the server. Make sure that you're located at `./frontend` before running `npm` commands.

```bash
# Install Node.js and npm with nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install lts/hydrogen # v18.20.2

# Go to the root folder for the Vue app
cd frontend

# Install dependencies (re-run if add new dependency in package.json)
npm run install

# Build the Vue app (re-run if vite.config.js is changed)
npm run build

# Start the Vue app
npm run dev
```

Go to http://localhost:5173 to check out the website.
