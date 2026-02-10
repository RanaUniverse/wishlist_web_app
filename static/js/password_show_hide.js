function PassShowHideFun() {
    var x = document.getElementById("password")
    var icon = document.getElementById("eyeIcon")
    if (x.type === "password") {
        x.type = "text"
        icon.className = "bi bi-eye-slash"
    } else {
        x.type = "password"
        icon.className = "bi bi-eye"
    }
}