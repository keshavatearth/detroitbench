(() => {
  "use strict";
  const root = document.documentElement;
  const button = document.getElementById("site-theme");
  function showTheme() {
    const dark = root.dataset.theme === "dark";
    button.textContent = dark ? "Light" : "Dark";
    button.setAttribute("aria-label", `Switch to ${dark ? "light" : "dark"} theme`);
  }
  button.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
    try { localStorage.setItem("db-theme", root.dataset.theme); } catch { /* Local files may disable storage. */ }
    showTheme();
  });
  window.addEventListener("storage", event => {
    if (event.key === "db-theme") {
      root.dataset.theme = event.newValue === "dark" ? "dark" : "light";
      showTheme();
    }
  });
  function showSection() {
    let section = document.body.dataset.siteSection;
    if (section === "overview" && ["#chapters", "#chapter-view", "#behavior", "#flowchart"].includes(location.hash)) section = "chapters";
    if (section === "results" && location.hash === "#method") section = "method";
    document.querySelectorAll(".site-navigation a").forEach(link => {
      if (link.dataset.siteSection === section) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
  }
  document.querySelectorAll(".site-navigation a").forEach(link => {
    link.addEventListener("click", event => {
      const target = new URL(link.href);
      const home = /\/(?:index|campaign)\.html$/.test(location.pathname) || location.pathname.endsWith("/");
      if (home && target.hash === "#chapters") {
        event.preventDefault();
        location.hash = "chapters";
        document.getElementById("chapters")?.scrollIntoView({ block: "start" });
      }
    });
  });
  window.addEventListener("hashchange", showSection);
  window.addEventListener("popstate", showSection);
  showTheme();
  showSection();
})();
