let testCount = 0;

document.getElementById("predictBtn").addEventListener("click", async () => {
  const userInput = document.getElementById("userInput").value.trim();
  if (!userInput) {
    alert("Please enter some text first!");
    return;
  }

  const selectedMode = document.querySelector('input[name="mode"]:checked').value;
  const resCard = document.getElementById("resultCard");
  const labelEl = document.getElementById("predLabel");
  const confEl = document.getElementById("predConf");

  // show loading state
  resCard.classList.remove("hidden");
  labelEl.textContent = "Analyzing...";
  confEl.textContent = "";

  try {
    const res = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: userInput, mode: selectedMode }),
    });
    const data = await res.json();

    // update result section
    labelEl.textContent = `Label: ${data.label}`;
    labelEl.className = data.label.includes("Offensive") ? "offensive" : "safe";
    confEl.textContent = `Confidence: ${data.confidence}%`;

    // log the result
    logResult(selectedMode, userInput, data.label, data.confidence);

    // clear text
    document.getElementById("userInput").value = "";
  } catch (err) {
    console.error(err);
    labelEl.textContent = "Error fetching prediction.";
  }
});

function logResult(mode, inputText, label, confidence) {
  testCount++;
  const row = document.createElement("tr");
  row.className = label.includes("Offensive") ? "bg-red-50" : "bg-green-50";

  const barColor = label.includes("Offensive") ? "#dc2626" : "#16a34a";
  row.innerHTML = `
    <td class="p-2 border-t">${testCount}</td>
    <td class="p-2 border-t">${mode}</td>
    <td class="p-2 border-t">${inputText}</td>
    <td class="p-2 border-t font-medium ${label.includes('Offensive') ? 'text-red-600' : 'text-green-600'}">${label}</td>
    <td class="p-2 border-t">
      <div class="w-full bg-gray-200 rounded-full h-2">
        <div class="h-2 rounded-full" style="width:${confidence}%; background:${barColor}"></div>
      </div>
      <p class="text-xs text-gray-600 mt-1">${confidence}%</p>
    </td>
  `;
  document.getElementById("resultBody").appendChild(row);
}
