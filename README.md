[![api fetcher](https://github.com/iqfareez/mpt-backup-api/actions/workflows/fetcher.yml/badge.svg)](https://github.com/iqfareez/mpt-backup-api/actions/workflows/fetcher.yml)

# mpt-backup-api

**Attention** :exclamation: This API is meant to be used by the [Malaysia Prayer Time app](https://github.com/iqfareez/app_waktu_solat_malaysia) **as a backup** if JAKIM's API is unreachable.

To **start a local server**, run `npm install`, then `npm start` and go to `localhost:3000`.
_Make sure node is installed on your machine_

## How it works?

![mpt backup api process drawio](https://user-images.githubusercontent.com/60868965/134902938-35a365b2-7314-4b97-86e8-8b447e2d0db4.png)

`db.json` database is created from a **python** script. Supposed to run once every month via GitHub [action](https://github.com/iqfareez/mpt-backup-api/actions/workflows/fetcher.yml).

Build and hosted by [Heroku](https://www.heroku.com/)

## Honourable mentions

1. [The idea behind automatic fetching and deploy using Python and GitHub](https://canovasjm.netlify.app/2020/11/29/github-actions-run-a-python-script-on-schedule-and-commit-changes/)
2. [The idea of this simple API architecture](https://youtu.be/FLnxgSZ0DG4)
3. [Website template](https://getbootstrap.com/docs/5.1/examples/starter-template)
