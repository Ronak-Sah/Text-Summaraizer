async function summarizeText() {
    const inputText = document.getElementById("inputText").value;
    const outputDiv = document.getElementById("output");

    if (inputText.trim() === "") {
        alert("Please enter some text!");
        return;
    }

    outputDiv.innerHTML = "Summarizing... ⏳";

    try {
        const response = await fetch("http://127.0.0.1:5000/summarize", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: inputText })
        });

        const data = await response.json();
        outputDiv.innerHTML = data.summary;

    } catch (error) {
        outputDiv.innerHTML = "Error connecting to model!";
        console.error(error);
    }
}
