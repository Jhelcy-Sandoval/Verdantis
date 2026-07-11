const btnAgregarMedicion =
    document.querySelector(".agregar_medicion");

const modalMedicion =
    document.getElementById("medicionModal");

const cerrarModalMedicion=
    document.getElementById("cerrar-modal");

// Modal

if (btnAgregarMedicion && modalMedicion) {

    btnAgregarMedicion.addEventListener(
        "click",
        () => {

            modalMedicion.classList.add("show");
            console.log("show modal");

        }
    );

}

if (cerrarModalMedicion && modalMedicion) {

    cerrarModalMedicion.addEventListener(
        "click",
        () => {

            modalMedicion.classList.remove("show");

        }
    );

}

// Grid / List

document.addEventListener(
    "DOMContentLoaded",
    () => {

        const gridBtn =
            document.getElementById("gridMedViewBtn");

        const listBtn =
            document.getElementById("listMedViewBtn");

        const gridView =
            document.getElementById("medicionesGridView");

        const listView =
            document.getElementById("medicionesListView");

        if (
            !gridBtn ||
            !listBtn ||
            !gridView ||
            !listView
        ) {

            console.log(
                "No se encontraron elementos"
            );

            return;

        }

        gridBtn.addEventListener(
            "click",
            () => {

                gridView.classList.remove(
                    "d-none"
                );

                listView.classList.add(
                    "d-none"
                );

                gridBtn.classList.remove(
                    "btn-light"
                );

                gridBtn.classList.add(
                    "btn-success"
                );

                listBtn.classList.remove(
                    "btn-success"
                );

                listBtn.classList.add(
                    "btn-light"
                );

                localStorage.setItem(
                    "medicionView",
                    "grid"
                );

            }
        );

        listBtn.addEventListener(
            "click",
            () => {

                listView.classList.remove(
                    "d-none"
                );

                gridView.classList.add(
                    "d-none"
                );

                listBtn.classList.remove(
                    "btn-light"
                );

                listBtn.classList.add(
                    "btn-success"
                );

                gridBtn.classList.remove(
                    "btn-success"
                );

                gridBtn.classList.add(
                    "btn-light"
                );

                localStorage.setItem(
                    "medicionView",
                    "list"
                );

            }
        );

        const savedView =
            localStorage.getItem(
                "medicionView"
            );

        if (savedView === "grid") {

            gridBtn.click();

        }

    }
);

// medicion plantas

const btnAgregarMedicionPlanta =
    document.querySelector(".agregar_medicion_planta");

const modalMedicionPlanta =
    document.getElementById("medicionPlModal");

const cerrarModalMedicionPlanta=
    document.getElementById("cerrar-modal");

// Modal

if (btnAgregarMedicionPlanta && modalMedicionPlanta) {

    btnAgregarMedicionPlanta.addEventListener(
        "click",
        () => {

            modalMedicionPlanta.classList.add("show");
            console.log("show modal");

        }
    );

}

if (cerrarModalMedicionPlanta && modalMedicionPlanta) {

    cerrarModalMedicionPlanta.addEventListener(
        "click",
        () => {

            modalMedicionPlanta.classList.remove("show");

        }
    );

}

// Grid / List

document.addEventListener(
    "DOMContentLoaded",
    () => {

        const gridBtn =
            document.getElementById("gridMedplViewBtn");

        const listBtn =
            document.getElementById("listMedplViewBtn");

        const gridView =
            document.getElementById("medicionesPlantaGridView");

        const listView =
            document.getElementById("medicionesPlantaListView");

        if (
            !gridBtn ||
            !listBtn ||
            !gridView ||
            !listView
        ) {

            console.log(
                "No se encontraron elementos"
            );

            return;

        }

        gridBtn.addEventListener(
            "click",
            () => {

                gridView.classList.remove(
                    "d-none"
                );

                listView.classList.add(
                    "d-none"
                );

                gridBtn.classList.remove(
                    "btn-light"
                );

                gridBtn.classList.add(
                    "btn-success"
                );

                listBtn.classList.remove(
                    "btn-success"
                );

                listBtn.classList.add(
                    "btn-light"
                );

                localStorage.setItem(
                    "medicionPlView",
                    "grid"
                );

            }
        );

        listBtn.addEventListener(
            "click",
            () => {

                listView.classList.remove(
                    "d-none"
                );

                gridView.classList.add(
                    "d-none"
                );

                listBtn.classList.remove(
                    "btn-light"
                );

                listBtn.classList.add(
                    "btn-success"
                );

                gridBtn.classList.remove(
                    "btn-success"
                );

                gridBtn.classList.add(
                    "btn-light"
                );

                localStorage.setItem(
                    "medicionPlView",
                    "list"
                );

            }
        );

        const savedView =
            localStorage.getItem(
                "medicionPlView"
            );

        if (savedView === "grid") {

            gridBtn.click();

        }

    }
);