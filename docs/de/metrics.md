# Dokumentations-Metriken

Diese Seite bietet einen Überblick über die Qualität und Vollständigkeit unserer Dokumentation.

<div id="metrics-dashboard">
  <p>Lade Metriken...</p>
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
            <th>Metrik</th>
            <th>Wert</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>API-Abdeckung</td>
            <td>${data.api_coverage}%</td>
            <td>${data.api_coverage >= 95 ? '✅' : '❌'}</td>
          </tr>
          <tr>
            <td>Defekte Links</td>
            <td>${data.broken_links}</td>
            <td>${data.broken_links === 0 ? '✅' : '❌'}</td>
          </tr>
          <tr>
            <td>Markdown-Lint Fehler</td>
            <td>${data.lint_errors}</td>
            <td>${data.lint_errors === 0 ? '✅' : '❌'}</td>
          </tr>
        </tbody>
      </table>
      <p><em>Zuletzt aktualisiert: ${data.last_updated}</em></p>
    `;
  })
  .catch(error => {
    document.getElementById('metrics-dashboard').innerHTML = '<p>Fehler beim Laden der Metriken.</p>';
  });
</script>

## Badge-Status

- **API-Abdeckung**: ![Interrogate Coverage](../assets/interrogate.svg)
