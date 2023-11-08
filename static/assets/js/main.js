/*Expandir Menu*/
var i;
let ban=0;
const showMenu = (toggleId, navbarId, bodyId, navtop) => {
  const toggle = document.getElementById(toggleId),
    navbar = document.getElementById(navbarId),
    bodypadding = document.getElementById(bodyId);
    hidename = document.getElementById(navtop);

  if (toggle && navbar) {
     toggle.addEventListener('click', ()=>{
        navbar.classList.toggle('expander')
        bodypadding.classList.toggle('body-pd')
        hidename.classList.toggle('hide-name')
        
        ResetMenu()
    })

   /*  navbar.addEventListener("mouseenter", () => {
      navbar.classList.toggle("expander");
      bodypadding.classList.toggle("body-pd");
      hidename.classList.toggle(hide-name)
      ResetMenu();
    });

    navbar.addEventListener("mouseleave", () => {
      navbar.classList.toggle("expander");
      bodypadding.classList.toggle("body-pd");
      hidename.classList.toggle(hide-name)
      ResetMenu();
    }); */
  }
};
showMenu("LogoToggle", "navbar", "body-pd", "navtop");

/*Opcion activada*/
const linkColor = document.querySelectorAll(".nav__link");
console.log(linkColor);
function colorLink() {
  linkColor.forEach((l) => l.classList.remove("active"));
  this.classList.add("active");
}
linkColor.forEach((l) => l.addEventListener("click", colorLink));

/*Colapsar submenu*/
const linkCollapse = document.getElementsByClassName("collapse__link");

for (i = 0; i < linkCollapse.length; i++) {
  linkCollapse[i].addEventListener("click", ColapsarMenu);
}

function ColapsarMenu() {
  const collapseMenu = this.nextElementSibling;
  collapseMenu.classList.toggle("showCollapse");
  const rotate = collapseMenu.previousElementSibling;
  rotate.classList.toggle("rotate");
  console.log("Mostrar menu");
  console.log(linkCollapse);
  ban=1;
}

function ResetMenu() {
  const menuReset = document.querySelectorAll(".collapse__menu");
  const RotateState = document.querySelectorAll(".collapse__link");
  console.log("Entro");
  menuReset.forEach((l) => l.classList.remove("showCollapse"));
  RotateState.forEach((l) => l.classList.remove("rotate"));
}


/* Boton de busqueda */
const icon=document.querySelector(".icons");
const search=document.querySelector(".search");
icon.onclick = function(){
  search.classList.toggle("activate");
}




