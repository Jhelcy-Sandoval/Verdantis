const btnAgregarLocation =
    document.querySelector(".agregar_ubicacion");

const modalLocation =
    document.getElementById("modal-location");

const cerrarModalLocation =
    document.getElementById("cerrar-modal");

// Modal

if (btnAgregarLocation && modalLocation) {

    btnAgregarLocation.addEventListener(
        "click",
        () => {

            modalLocation.classList.add("show");
            console.log("show modal");

        }
    );

}

if (cerrarModalLocation && modalLocation) {

    cerrarModalLocation.addEventListener(
        "click",
        () => {

            modalLocation.classList.remove("show");

        }
    );

}
