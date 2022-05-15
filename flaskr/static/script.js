const brightness_slider = document.querySelector("#brightness_slider");
const contrast_slider = document.querySelector("#contrast_slider");
const saturation_slider = document.querySelector("#saturation_slider");
const autofocus_check = document.querySelector("#autofocus_check");
const fixedfocus_slider = document.querySelector("#fixedfocus_slider");

function makeRequest(url, data) {
    httpRequest = new XMLHttpRequest();

    if (!httpRequest) {
        alert('Giving up :( Cannot create an XMLHTTP instance');
        return false;
    }

    httpRequest.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log("Done!");
        }
    };
    httpRequest.open('GET', '/' + url + "/" + data, true);
    httpRequest.send();
}

brightness_slider.addEventListener("change", (e) => {
    console.log("Brightness:" + e.target.value);
    makeRequest("brightness", e.target.value);
});

contrast_slider.addEventListener("change", (e) => {
    console.log("Contrast:" + e.target.value);
    makeRequest("contrast", e.target.value);
});

saturation_slider.addEventListener("change", (e) => {
    console.log("Saturation:" + e.target.value);
    makeRequest("saturation", e.target.value);
});

autofocus_check.addEventListener("change", (e) => {
    console.log("Autofocus:" + e.target.checked);
    makeRequest("autofocus", e.target.checked);
});

fixedfocus_slider.addEventListener("change", (e) => {
    console.log("Fixed Focus:" + e.target.value);
    makeRequest("fixedfocus", e.target.value);
});