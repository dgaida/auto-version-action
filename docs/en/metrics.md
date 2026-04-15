# Documentation Metrics

This page provides an overview of the quality and completeness of our documentation.

<div id="metrics-dashboard">
  <p>Loading metrics...</p>
</div>

<script>
fetch('../assets/metrics.json')
  .then(response => response.json())
  .then(data => {
    const dashboard = document.getElementById('metrics-dashboard');
    dashboard.innerHTML = `
      <table>
        <thead>
          <tr>
            <th>Metric</th>
            <th>Value</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>API Coverage</td>
            <td>${data.api_coverage}%</td>
            <td>${data.api_coverage >= 95 ? '✅' : '❌'}</td>
          </tr>
          <tr>
            <td>Broken Links</td>
            <td>${data.broken_links}</td>
            <td>${data.broken_links === 0 ? '✅' : '❌'}</td>
          </tr>
          <tr>
            <td>Markdown Lint Errors</td>
            <td>${data.lint_errors}</td>
            <td>${data.lint_errors === 0 ? '✅' : '❌'}</td>
          </tr>
        </tbody>
      </table>
      <p><em>Last updated: ${data.last_updated}</em></p>
    `;
  })
  .catch(error => {
    document.getElementById('metrics-dashboard').innerHTML = '<p>Error loading metrics.</p>';
  });
</script>

## Badge Status

- **API Coverage**: ![Interrogate Coverage](../assets/interrogate.svg)
