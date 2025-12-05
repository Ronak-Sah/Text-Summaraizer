
const maxLengthSlider = document.getElementById("maxLength");
const maxLengthValue = document.getElementById("maxLengthValue");
maxLengthSlider.oninput = () => maxLengthValue.innerText = maxLengthSlider.value;

const numBeamsSlider = document.getElementById("numBeams");
const numBeamsValue = document.getElementById("numBeamsValue");
numBeamsSlider.oninput = () => numBeamsValue.innerText = numBeamsSlider.value;
async function summarizeText() {
    const inputText = document.getElementById("inputText").value;
    const outputDiv = document.getElementById("output");
    const maxLength = parseInt(maxLengthSlider.value);
    const numBeams = parseInt(numBeamsSlider.value);

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
            body: JSON.stringify({ text: inputText, max_length: maxLength, num_beams: numBeams })
        });

        const data = await response.json();
        outputDiv.innerHTML = data.summary;

    } catch (error) {
        outputDiv.innerHTML = "Error connecting to model!";
        console.error(error);
    }
}
