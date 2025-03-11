document.getElementById("fetchNotes").addEventListener("click", async () => {  
    const response = await fetch("http://localhost:5000/api/notes");  
    const notes = await response.json();  
    console.log("Processed notes:", notes);
  });