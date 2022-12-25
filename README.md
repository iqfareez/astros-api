![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
[![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)](#how-it-work)

# astros-api

## To run

### Get AZURE key

Create a new Bing Resource instance. Take the first & secondary key and save them in env `AZURE_KEY1` & `AZURE_KEY2`.

### Get latest astros data

Prerequisites: **Node** & **Python 3.10**

Install required packages

```
pip install requests urllib3
```

Run the fetcher

```
py fetcher.py
```

### Start local server

```
npm install
```

Then

```
npm start
```

## How it work?

```mermaid
flowchart TD
    subgraph "External API"
    A(OpenNotifyAPI) & B(Bing API)
    end
    B <--> C
    A <--> C
    subgraph fetcher.py
    C[[Fetch latest astros data]] --> D[(db.json)] & E[(log.json)] --> F(Commit & push)
    end
    F -->|Heroku build triggered| G[Deployed to Heroku]
```

[![Fetch and deploy](https://github.com/iqfareez/astros-api/actions/workflows/fetcher.yml/badge.svg)](https://github.com/iqfareez/astros-api/actions/workflows/fetcher.yml)

**db.json** contains the actual astronauts' database. **log.json** will store the date & time of the fetcher run.

The [fetcher.py](fetcher.py) is scheduled to run automatically via GitHub [action](https://github.com/iqfareez/mpt-backup-api/actions/workflows/fetcher.yml). The frequency is as defined in [fetcher.yml](.github/workflows/fetcher.yml) script.

Build and hosted by [Heroku](https://www.heroku.com/).

## Honorable mentions

1. http://open-notify.org/Open-Notify-API/People-In-Space/
2. https://www.microsoft.com/en-us/bing/apis/bing-image-search-api
3. [Website template](https://getbootstrap.com/docs/5.1/examples/starter-template)
