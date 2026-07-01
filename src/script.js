async function analyze() {
    const text = document.getElementById("text").value;

    try {
        const response = await fetch("/api/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text })
        });

        const data = await response.json();

        console.log(data);   // Check response in browser console

        document.getElementById("language").innerText =
            data.language || "No language detected";

        document.getElementById("redacted").innerText =
            data.redacted || "No redacted text";

        document.getElementById("summary").innerText =
            data.summary || "No summary generated";

    } catch (err) {
        console.error(err);

        document.getElementById("language").innerText = "Error";
        document.getElementById("redacted").innerText = err.message;
        document.getElementById("summary").innerText = err.message;
    }
}
