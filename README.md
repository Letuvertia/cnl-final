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
大家看這裡！！

### Use branch!

Open a new branch and develop features (or add new files if needed) in the corresponding folder. When you're finished, open a pull request and fix merge conflict first before merging the branch into the main branch.

### (Optinal) Develop on Local
If you're developing a feature that is only on `backend` or `frontend` side, it is maybe easier to use local environment instead of the docker environment, which connects everything and is more likely to have bugs.

Here's how to install the dependencie on the local environment:

1. `backend`

Install Python and execute files in `./backend/`.

```bash
python3 backend/main.py
```

To test an API, use `curl`.

```bash
curl "http://localhost:5000/userdata?uid=123"
```

2. `frontend`

Install Node.js and run the server. Make sure that you're located at `./frontend` before running `npm` commands.

```bash
# Setup
apt-get update && apt-get install -y nodejs npm

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
