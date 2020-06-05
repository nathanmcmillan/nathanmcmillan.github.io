const prefer_dark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;

function is_dark_mode() {
  return localStorage.getItem("colors") === "dark";
}

function set_dark_mode() {
  localStorage.setItem("colors", "dark");

  const link = document.createElement("link");
  link.rel = "stylesheet";
}

window.onload = function () {
  if (is_dark_mode()) {
  }
};
