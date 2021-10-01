const closeBtn = document.querySelector(".close");
const maximizeBtn = document.querySelector(".maximize");
const minimizeBtn = document.querySelector(".minimize");
const randomCheck = document.querySelector("input[type='checkbox']");
const seedInput = document.querySelector(".seed-input");

randomCheck.onchange = () => {
  if (randomCheck.checked === true) {
    seedInput.disabled = true;
  } else {
    seedInput.disabled = false;
  }
};

const Btn = document.querySelector("form > button");

Btn.onclick = () => {
  pywebview.api.generate("default", 400, 300, "#242424", "./image.png");
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
