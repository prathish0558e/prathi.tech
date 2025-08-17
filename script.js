// Dark mode toggle
function toggleMode(){
  document.body.classList.toggle("light");
  localStorage.setItem("theme",document.body.classList.contains("light")?"light":"dark");
}
if(localStorage.getItem("theme")==="light"){document.body.classList.add("light");}

// Sample tools (later connect to 1 Lakh data from Google Sheet/JSON)
const tools = [
  {name:"Canva",desc:"Free Design & Editing Tool",link:"https://www.canva.com"},
  {name:"Overleaf",desc:"LaTeX Document Writing Tool",link:"https://www.overleaf.com"},
  {name:"Geogebra",desc:"Math Graphing & Geometry",link:"https://www.geogebra.org"},
  {name:"Replit",desc:"Online IDE & Coding Platform",link:"https://replit.com"}
];

const grid=document.getElementById("tools-grid");
tools.forEach(t=>{
  let card=document.createElement("div");
  card.className="card";
  card.innerHTML=`<h3>${t.name}</h3><p>${t.desc}</p><a href="${t.link}" target="_blank">Visit</a>`;
  grid.appendChild(card);
});

// Search filter
function searchTools(){
  let input=document.getElementById("search").value.toLowerCase();
  let cards=document.querySelectorAll(".card");
  cards.forEach(card=>{
    card.style.display=card.innerText.toLowerCase().includes(input)?"block":"none";
  });
}
