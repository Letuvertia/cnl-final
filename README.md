# LocaSync
極短距離的即時通訊社群軟體

## System Design
![alt text](figure/cnl-system-design.jpg?raw=true "LocaSync system design.")

There are 2 docker containers in this design, `web` and `radius`.

### Web
1. Frontend
We use `React.js` as web frontend framework. All the Javascript files are stored at `web/frontend/`.

2. Backend
We use `Flask` as web backend framework. All the Python files are stored at `web/backend`.

### Radius
The FreeRadius is running on this `radius` container, with port 1812 exposed for the `web` contianer to access the data.

## Setup
1. Install Docker
2. Run `./run.sh` 
