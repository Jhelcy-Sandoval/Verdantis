const btnAgregarPlanta =
    document.querySelector(".agregar_planta");

const modal =
    document.getElementById("modal-planta");

const cerrarModal =
    document.getElementById("cerrar-modal");

// Modal

if (btnAgregarPlanta && modal) {

    btnAgregarPlanta.addEventListener(
        "click",
        () => {

            modal.classList.add("show");
            console.log("show modal");

        }
    );

}

if (cerrarModal && modal) {

    cerrarModal.addEventListener(
        "click",
        () => {

            modal.classList.remove("show");

        }
    );

}

// Grid / List

document.addEventListener(
    "DOMContentLoaded",
    () => {

        const gridBtn =
            document.getElementById("gridViewBtn");

        const listBtn =
            document.getElementById("listViewBtn");

        const gridView =
            document.getElementById("plantsGridView");

        const listView =
            document.getElementById("plantsListView");

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
                    "plantsView",
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
                    "plantsView",
                    "list"
                );

            }
        );

        const savedView =
            localStorage.getItem(
                "plantsView"
            );

        if (savedView === "grid") {

            gridBtn.click();

        }

    }
);