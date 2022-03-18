fetch('http://localhost:7000/numbers.json')
    .then(response => response.json())
    .then(data => console.log(data));