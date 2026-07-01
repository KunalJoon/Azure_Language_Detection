async function analyze(){
const text=document.getElementById('text').value;
const r=await fetch('/api/analyze',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text})});
const d=await r.json();
language.textContent=d.language;
redacted.textContent=d.redacted;
summary.textContent=d.summary;
}