const SIGN_UP_SUBMIT_BUTTON = document.querySelector("#sign-up-submit");
const SIGN_IN_SUBMIT_BUTTON = document.querySelector("#sign-in-submit");
const LOGIN_INPUT = document.querySelector("input[name='login']");
const PASSWORD_INPUT = document.querySelector("input[name='password']");
const RE_PASSWORD_INPUT = document.querySelector("input[name='re-password']");



if (SIGN_IN_SUBMIT_BUTTON) {
    SIGN_IN_SUBMIT_BUTTON.addEventListener("click", async (e) => {
        e.preventDefault();
        if (LOGIN_INPUT.value.length == 0) {
            return -1;
        }

        if (PASSWORD_INPUT.value.length == 0) {
            return -1;
        }

        let formBody = [];
        const data = {
            "username": LOGIN_INPUT.value,
            "password": PASSWORD_INPUT.value
        };

        for (let property in data) {
            let encodedKey = encodeURIComponent(property);
            let encodedValue = encodeURIComponent(data[property]);
            formBody.push(`${encodedKey}=${encodedValue}`);
        }
        formBody = formBody.join("&");
        const response = await fetch("/token", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            },
            body: formBody
        });

        const response_json = await response.json();

        if (response_json.access_token.length > 0) {
            window.location.reload();
        }
    });
}

if (SIGN_UP_SUBMIT_BUTTON) {
    SIGN_UP_SUBMIT_BUTTON.addEventListener("click", async (e) => {
        e.preventDefault();
        if (LOGIN_INPUT.value.length == 0) {
            return -1;
        }

        if (PASSWORD.value.length == 0 || PASSWORD_INPUT.value != RE_PASSWORD_INPUT.value) {
            return -1;
        }

        const response = await fetch(`/register?username=${LOGIN_INPUT.value}&password=${PASSWORD_INPUT.value}`, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });

        const response_json = await response.json();

        if (response_json.success == true) {
            window.location.reload();
        }
    });
}