const FOOTER_ASSET_VERSION = '1.5.8';
const DEPLOY_VERSION = '2026.03.05-02';

async function loadAdminFooter() {
  const container = document.getElementById('app-footer');
  if (!container) return;
  try {
    const res = await fetch(`/static/common/html/footer.html?v=${encodeURIComponent(FOOTER_ASSET_VERSION)}`);
    if (!res.ok) return;
    container.innerHTML = await res.text();
    const versionNode = container.querySelector('#app-build-version');
    if (versionNode) {
      versionNode.textContent = `Build ${DEPLOY_VERSION}`;
    }
  } catch (e) {
    // Fail silently to avoid breaking page load
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', loadAdminFooter);
} else {
  loadAdminFooter();
}
