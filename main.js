const closeBtn = document.querySelector(".close");
const maximizeBtn = document.querySelector(".maximize");
const minimizeBtn = document.querySelector(".minimize");
const saveBtn = document.querySelector(".save-btn");

window.addEventListener("pywebviewready", () => {
  pywebview.api.init().then((response) => {
    console.log(response);
  });
});

const Btn = document.querySelector("form > button");

saveBtn.onclick = () => {
  // Defaults "default", 2100, 1300, "#ffffff", "#242424", 50, 30, 100, 10, 0, "./image.png"
  pywebview.api.generate(
    "default",
    2100,
    1300,
    "#ffffff",
    "#242424",
    50,
    30,
    100,
    10,
    0,
    "./image.png"
  );
};

closeBtn.onclick = () => {
  pywebview.api.close_window();
};

maximizeBtn.onclick = () => {
  pywebview.api.toggle_fullscreen();
};

minimizeBtn.onclick = () => {
  pywebview.api.minimize();
};

const catchException = () => {
  pywebview.api.error().catch((response) => {
    console.error(response);
  });
};
