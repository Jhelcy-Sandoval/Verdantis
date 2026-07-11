const btnAgregarEspecie =
    document.querySelector(".agregar_especie");

const modalEspecie =
    document.getElementById("modal-especie");

const cerrarModalEspecie =
    document.getElementById("cerrar-modal");

// Modal

if (btnAgregarEspecie && modalEspecie) {

    btnAgregarPlanta.addEventListener(
        "click",
        () => {

            modalEspecie.classList.add("show");
            console.log("show modal");

        }
    );

}

if (cerrarModalEspecie && modalEspecie) {

    cerrarModalEspecie.addEventListener(
        "click",
        () => {

            modalEspecie.classList.remove("show");

        }
    );

}

// tabla especies

document.addEventListener(
    "DOMContentLoaded",
    () => {

        const gridBtn =
            document.getElementById("gridEspViewBtn");

        const listBtn =
            document.getElementById("listEspViewBtn");

        const gridView =
            document.getElementById("especieGridView");

        const listView =
            document.getElementById("especieListView");

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
                    "especiesView",
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
                    "especiesView",
                    "list"
                );

            }
        );

        const savedView =
            localStorage.getItem(
                "especiesView"
            );

        if (savedView === "grid") {

            gridBtn.click();

        }

    }
);