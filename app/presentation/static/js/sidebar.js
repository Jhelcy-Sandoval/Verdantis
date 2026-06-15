const sidebar = document.getElementById("sidebar");
const btn = document.getElementById("toggleSidebar");

if (btn) {
    btn.addEventListener("click", () => {

        sidebar.classList.toggle("collapsed");

        btn.textContent =
            sidebar.classList.contains("collapsed")
                ? "▶"
                : "◀";

    });
}

const currentPath = window.location.pathname;

document.querySelectorAll("#sidebar a").forEach(link => {

    const linkPath = new URL(link.href).pathname;

    if (linkPath === currentPath) {
        link.classList.add("active");
    }

});