// Cookies
function getCookie(name) {
    let matches = document.cookie.match(
        new RegExp(
            "(?:^|; )" +
            name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, "\\$1") +
            "=([^;]*)"
        )
    );
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

function setCookie(name, value, age) {
    let updatedCookie =
        encodeURIComponent(name) + "=" + encodeURIComponent(value);

    for (let optionKey in age) {
        updatedCookie += "; " + optionKey;
        let optionValue = age[optionKey];
        if (optionValue !== true) {
            updatedCookie += "=" + optionValue;
        }
    }

    document.cookie = updatedCookie;
}

function deleteCookie(name) {
    this.setCookie(name, "", {
        "max-age": -1,
    });
}


// API
function post(path, data) {
    return fetch(path, {
        method: "POST",
        headers: {
            accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });
}


function get(path) {
    return fetch(path, {
        method: "GET",
        headers: {
            accept: "application/json",
        },
    });
}


