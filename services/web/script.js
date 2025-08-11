async function loadStations(){
  const q=document.getElementById("q").value.trim();
  const url=q?`/api/stations?q=${encodeURIComponent(q)}`:"/api/stations";
  const res=await fetch(url); const data=await res.json();
  document.getElementById("count").textContent=`${data.length} station(s)`;
  const tb=document.querySelector("#tbl tbody"); tb.innerHTML="";
  data.forEach(s=>{const tr=document.createElement("tr");
    tr.innerHTML=`<td>${s.name}</td><td>${s.line.join(", ")}</td><td>${s.zone}</td>`; tb.appendChild(tr);});
}
function resetStations(){document.getElementById("q").value="";loadStations();}
async function mockJourney(){
  const from=document.getElementById("from").value.trim();
  const to=document.getElementById("to").value.trim();
  const res=await fetch(`/api/journey-mock?from=${encodeURIComponent(from)}&to=${encodeURIComponent(to)}`);
  document.getElementById("journey").textContent=JSON.stringify(await res.json(),null,2);
}
loadStations();
