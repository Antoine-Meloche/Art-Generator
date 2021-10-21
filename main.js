const settingsBtn = document.querySelector(".settings-btn");
const style = document.querySelector("style");
const closeBtn = document.querySelector(".close");
const maximizeBtn = document.querySelector(".maximize");
const minimizeBtn = document.querySelector(".minimize");
const saveBtn = document.querySelector(".save-btn");

const exportPathInput = document.querySelector(".export-path");
const algSelect = document.querySelector(".alg-gen-select");
const widthInput = document.querySelector(".width-input");
const heightInput = docuemnt.querySelector(".height-input");
const bkgInput = document.querySelector(".bkg-color-picker");
const lineColorInput = document.querySelector(".line-color-picker");
const startInput = document.querySelector(".start-input");
const iterationInput = docuemnt.querySelector(".iteration-input");
const substepsInput = document.querySelector(".substep-input");
const lengthInput = document.querySelector(".length-input");
const angleIncrInput = document.querySelector(".angleincr-input");
const angleInput = document.querySelector(".angle-input");

window.addEventListener("pywebviewready", () => {
  pywebview.api.init().then((response) => {
    console.log(response);
  });
});

settingsBtn.onclick = () => {
  changeTheme();
}

saveBtn.onclick = () => {
  // Defaults "default", 2100, 1300, "#ffffff", "#242424", 50, 10, 30, 100, 10, 0, "./image.png"
  pywebview.api.generate(
    algSelect.value,
    widthInput.value,
    heightInput.value,
    bkgInput.value,
    lineColorInput.value,
    startInput.value,
    iterationInput.value,
    substepsInput.value,
    lengthInput.value,
    angleIncrInput.value,
    angleInput.value,
    exportPathInput.value
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

function changeTheme() {
  if ( style.innerHTML !== "" ) {
    style.innerHMTL = "";
    return;
  }
  style.innerHMTL = `
    :root {
      --primary-background: #242424;
      --secondary-background: #3f3f3f;
      --titlebar-color: #121212;
      --titlebar-btn-color: var(--titlebar-color);
      --titlebar-btn-hover-color: #444444;
      --titlebar-btn-indicator-color: #ffffff;
      --close-btn-hover-color: #ff0000;
      --primary-accent-color: greenyellow;
      --secondary-accent-color: #9e9e9e;
      --primary-text-color: #ffffff;
    }`
}