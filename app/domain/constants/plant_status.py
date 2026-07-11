class PlantStatus:

    GERMINACION = "Germinación"
    CRECIMIENTO = "Crecimiento"
    SALUDABLE = "Saludable"

    OBSERVACION = "Observación"
    TRASPLANTE = "Trasplante"
    RECUPERACION = "Recuperación"

    ALERTA = "Alerta"
    CRITICO = "Crítico"

    TODOS = [
        GERMINACION,
        CRECIMIENTO,
        SALUDABLE,
        OBSERVACION,
        TRASPLANTE,
        RECUPERACION,
        ALERTA,
        CRITICO
    ]

    BUEN_ESTADO = [
        GERMINACION,
        CRECIMIENTO,
        SALUDABLE
    ]

    EN_OBSERVACION = [
        OBSERVACION,
        TRASPLANTE,
        RECUPERACION
    ]

    EN_ALERTA = [
        ALERTA,
        CRITICO
    ]