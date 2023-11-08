const agent = document.getElementById("bag");
const client = document.getElementById("bcli");
const logclient = document.getElementById("logcli");
const logagent = document.getElementById("logag");
const container = document.querySelector(".main-contain");
const left = document.querySelector(".arti");
const rigth = document.querySelector(".artd");
const textfield = document.querySelectorAll(".inputWithIcon");
const rocket = document.getElementById("rocket");
const plane = document.getElementById("plane");


agent.addEventListener("click", () => {
    container.classList.add("main-contract");
    left.classList.add("hidden-art");
    logagent.classList.add("a");
  });

client.addEventListener("click", () => {
    container.classList.add("main-contractcl");
    rigth.classList.add("hidden-art");
    logclient.classList.add("l");
    for(var i = 0; i < textfield.length; i++)
    textfield[i].classList.add("blue");
  });

  agent.addEventListener("mouseover", () => {
    rocket.classList.add("deploit");
  });
  agent.addEventListener("mouseleave", () => {
    rocket.classList.remove("deploit");
  });




