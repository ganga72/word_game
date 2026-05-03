async function sendGuess() {
    let guess = document.getElementById("guess").value;

    let res = await fetch("/guess", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({guess: guess})
    });

    let data = await res.json();
    document.getElementById("result").innerText = JSON.stringify(data.result);
}
