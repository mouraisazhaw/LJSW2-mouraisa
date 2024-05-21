document.getElementById('textForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const inputText = document.getElementById('inputText').value;

    const response = await fetch('/api/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
    });

    if (response.ok) {
        const result = await response.json();
        document.getElementById('response').innerText = result.message;
    } else {
        document.getElementById('response').innerText = 'Fehler bei der Anfrage';
    }
});