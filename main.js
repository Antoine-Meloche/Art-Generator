const settingsBtn = document.querySelector(".settings-btn");
const htmlTag = document.querySelector("html");
const closeBtn = document.querySelector(".close");
const maximizeBtn = document.querySelector(".maximize");
const minimizeBtn = document.querySelector(".minimize");
const saveBtn = document.querySelector(".save-btn");
const exportPathInput = document.querySelector(".export-path");
const algSelectDiv = document.querySelector("[custom-select]");
const customOptionsList = document.querySelector(
  "[custom-select] .custom-options-list"
);
let algSelectDefault = document.querySelector(
  "[custom-select] .custom-option.default"
);
let algSelectPipes = document.querySelector(
  "[custom-select] .custom-option.pipes"
);
let algSelectWaves = document.querySelector(
  "[custom-select] .custom-option.waves"
);
const widthInput = document.querySelector(".width-input");
const heightInput = document.querySelector(".height-input");
const bkgInput = document.querySelector(".bkg-color-picker");
const lineColorInput = document.querySelector(".line-color-picker");
const startInput = document.querySelector(".start-input");
const iterationInput = document.querySelector(".iteration-input");
const substepsInput = document.querySelector(".substep-input");
const lengthInput = document.querySelector(".length-input");
const angleIncrInput = document.querySelector(".angleincr-input");
const angleInput = document.querySelector(".angle-input");

let selected = "default";
let options;

window.addEventListener("pywebviewready", () => {
  pywebview.api.init().then((response) => {
    console.log(response);
  });
});

settingsBtn.onclick = () => {
  changeTheme();
};

saveBtn.onclick = () => {
  // Defaults "default", 2100, 1300, "#ffffff", "#242424", 50, 10, 30, 100, 10, 0, "./image.png"
  if (selected === "default") {
    options = [
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
      exportPathInput.value,
    ];
  } else if (selected === "pipes") {
    options = [
      widthInput.value,
      heightInput.value,
      bkgInput.value,
      lineColorInput.value,
      pipesInput.value,
      probInput.value,
      exportPathInput.value
    ];
  } else if (selected === "waves") {
    options = [];
  }
  pywebview.api.generate(selected, options);
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

const setOnClicks = () => {
  algSelectDefault.onclick = () => {
    if (selected === "default") {
      algSelectDiv.classList.toggle("expanded");
      return;
    }
    customOptionsList.innerHTML = `<div class="custom-option one default" value="default">Collatz Conjecture (3x+1)</div>
      <div class="custom-option two pipes" value="pipes">Pipes</div>
      <div class="custom-option three waves" value="waves">Waves</div>`;
    algSelectDiv.classList.remove("expanded");
    selected = "default";
    algSelectDefault = document.querySelector(
      "[custom-select] .custom-option.default"
    );
    algSelectPipes = document.querySelector(
      "[custom-select] .custom-option.pipes"
    );
    algSelectWaves = document.querySelector(
      "[custom-select] .custom-option.waves"
    );
    setOnClicks();
  };

  algSelectPipes.onclick = () => {
    if (selected === "pipes") {
      algSelectDiv.classList.toggle("expanded");
      return;
    }
    customOptionsList.innerHTML = `<div class="custom-option one pipes" value="pipes">Pipes</div>
      <div class="custom-option two default" value="default">Collatz Conjecture (3x+1)</div>
      <div class="custom-option three waves" value="waves">Waves</div>`;
    algSelectDiv.classList.remove("expanded");
    selected = "pipes";
    algSelectDefault = document.querySelector(
      "[custom-select] .custom-option.default"
    );
    algSelectPipes = document.querySelector(
      "[custom-select] .custom-option.pipes"
    );
    algSelectWaves = document.querySelector(
      "[custom-select] .custom-option.waves"
    );
    setOnClicks();
  };

  algSelectWaves.onclick = () => {
    if (selected === "waves") {
      algSelectDiv.classList.toggle("expanded");
      return;
    }
    customOptionsList.innerHTML = `<div class="custom-option one waves" value="waves">Waves</div>
      <div class="custom-option two default" value="default">Collatz Conjecture (3x+1)</div>
      <div class="custom-option three pipes" value="pipes">Pipes</div>`;
    algSelectDiv.classList.remove("expanded");
    selected = "waves";
    algSelectDefault = document.querySelector(
      "[custom-select] .custom-option.default"
    );
    algSelectPipes = document.querySelector(
      "[custom-select] .custom-option.pipes"
    );
    algSelectWaves = document.querySelector(
      "[custom-select] .custom-option.waves"
    );
    setOnClicks();
  };
};
setOnClicks();

const catchException = () => {
  pywebview.api.error().catch((response) => {
    console.error(response);
  });
};

const changeTheme = () => {
  if (document.documentElement.classList.contains("dark")) {
    document.documentElement.classList.remove("dark");
  } else {
    document.documentElement.classList.add("dark");
  }
};
