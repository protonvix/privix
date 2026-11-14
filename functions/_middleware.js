// The old address forwards to the domain: vixautomationsportfolio.pages.dev -> design.vixassist.com
export async function onRequest(ctx) {
  const url = new URL(ctx.request.url);
  if (url.hostname === "vixautomationsportfolio.pages.dev") {
    url.hostname = "design.vixassist.com";
    return Response.redirect(url.toString(), 301);
  }
  return ctx.next();
}
