export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    // Extensionless /guides/* paths: fetch the .html asset directly so
    // Cloudflare Pages v3 routing never gets a chance to create the
    // extensionless ↔ .html redirect loop.
    if (
      path.startsWith('/guides/') &&
      !path.match(/\.[^/]+$/) &&
      path.length > '/guides/'.length
    ) {
      const htmlUrl = new URL(request.url);
      htmlUrl.pathname = path.replace(/\/$/, '') + '.html';
      return env.ASSETS.fetch(new Request(htmlUrl.toString(), request));
    }

    return env.ASSETS.fetch(request);
  },
};
