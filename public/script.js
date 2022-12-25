function ResourceItem({ name, length }) {
  return `
    <li>
      <a href="${name}">/${name}</a>
      <sup>${length ? `${length}x` : 'object'}</sup>
    </li>
  `
}

function ResourceList({ db }) {
  return `
    <ul>
      ${Object.keys(db)
      .map(name =>
        ResourceItem({
          name,
          length: Array.isArray(db[name]) && db[name].length
        })
      )
      .join('')}
    </ul>
  `
}

function NoResources() {
  return `<p>No resources found</p>`
}

function ResourcesBlock({ db }) {
  return `
    <div>
      ${Object.keys(db).length ? ResourceList({ db }) : NoResources()}
    </div>
  `
}

window
  .fetch('db')
  .then(response => response.json())
  .then(
    db =>
      (document.getElementById('resources').innerHTML = ResourcesBlock({ db }))
  )

window
  .fetch('log.json')
  .then(response => response.json())
  .then(
    log =>
      document.getElementById('last-run').innerHTML =
      `
        <b>Last updated:</b>&nbsp;<i>${log['fetcher_last_run']}</i>
      `
  )

// make link according to the site URL
function usageLink(){
  const url = window.location.href;
  // set the url in usage-link id
  // apend the URL with /data
  document.getElementById("usage-link").innerHTML = url + 'data';
}
usageLink()