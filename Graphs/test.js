data = d3.json('http://127.0.0.1:5000/data');
console.log(data);
console.log("Hi world");
function call_api() {
    const url = 'http://127.0.0.1:5000/data';
    fetch(url)
        .then(response => response.json())
        .then(json => {
            console.log(json[0])
            console.log(typeof (json))
        })
};
call_api();