function changeEffect() {
    var x = document.getElementById("effect-select").value;
    console.log(x)
    fetch("/set_effect", {
        method: "POST",
        body: JSON.stringify({
            effect: x
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        },
    })
}