from app.infrastructure.models.medicionplanta_model import MedicionPlanta
from app.infrastructure.repositories.medicionplanta_repository import MedicionPlantaRepository
from app.infrastructure.storage.supabase_storage import SupabaseStorage


class MedicionPlantaService:

    def __init__(self):
        self.repository = MedicionPlantaRepository()
        self.storage = SupabaseStorage()
        
    def listar_todas(
        self,
        user_id
    ):
        return self.repository.listar_todas(
            user_id
        )

    def listar_por_planta(
        self,
        planta_id,
        search=None,
        salud=None,
        plagas=None,
        enfermedad=None
    ):

        return self.repository.listar_por_planta(
            planta_id,
            search=search,
            salud=salud,
            plagas=plagas,
            enfermedad=enfermedad
        )

    def obtener_resumen(
        self,
        planta_id
    ):

        mediciones = self.repository.listar_por_planta(
            planta_id
        )

        total_mediciones = len(mediciones)

        if total_mediciones == 0:

            return {
                "total_mediciones": 0,
                "ultima_altura": 0,
                "ultima_humedad": 0,
                "estado_actual": "Sin registros"
            }

        ultima = mediciones[0]

        return {

            "total_mediciones": total_mediciones,

            "ultima_altura": ultima.altura,

            "ultima_humedad": ultima.humedad_sustrato,

            "estado_actual": ultima.salud
        }

    def ultima_medicion(
        self,
        planta_id
    ):

        return self.repository.ultima_medicion(
            planta_id
        )

    def crear_medicion(
        self,
        user_id,
        planta_id,
        altura,
        numero_hojas,
        diametro_tallo,
        humedad_sustrato,
        desarrollo,
        numero_flores,
        numero_frutos,
        color_hojas,
        plagas,
        enfermedad,
        observaciones=None,
        photo=None
    ):
        
        photo_url = None

        if photo and photo.filename:
            photo_url = self.storage.upload_image(photo)
        
        estado = self._calcular_estado(
            humedad_sustrato=humedad_sustrato,
            desarrollo=desarrollo,
            color_hojas=color_hojas,
            plagas=plagas,
            enfermedad=enfermedad
        )

        medicion = MedicionPlanta(
            user_id=user_id,
            planta_id=planta_id,
            altura=altura,
            numero_hojas=numero_hojas,
            diametro_tallo=diametro_tallo,
            humedad_sustrato=humedad_sustrato,
            desarrollo=desarrollo,
            numero_flores=numero_flores,
            numero_frutos=numero_frutos,
            color_hojas=color_hojas,
            plagas=plagas,
            enfermedad=enfermedad,
            salud=estado,
            observaciones=observaciones,
            foto_url=photo_url
        )

        return self.repository.guardar(
            medicion
        )
        
        
    def _calcular_estado(
        self,
        humedad_sustrato,
        desarrollo,
        color_hojas,
        plagas,
        enfermedad
    ):

        alertas = 0

        if plagas:
            alertas += 1

        if enfermedad:
            alertas += 1

        if humedad_sustrato is not None:
            if humedad_sustrato < 40 or humedad_sustrato > 80:
                alertas += 1

        if desarrollo is not None:
            if desarrollo < 60:
                alertas += 1

        if color_hojas:

            colores_alerta = [
                "Amarillo",
                "Marrón",
                "Negro"
            ]

            if color_hojas in colores_alerta:
                alertas += 1

        if alertas == 0:
            return "Óptima"

        if alertas == 1:
            return "Atención"

        return "Crítica"

    def detalle_medicion(
        self,
        medicion_id,
        user_id
    ):

        return self.repository.obtener_por_id(
            medicion_id,
            user_id
        )

    def eliminar_medicion(
        self,
        medicion_id,
        user_id
    ):

        medicion = self.repository.obtener_por_id(
            medicion_id,
            user_id
        )

        if medicion:

            self.repository.eliminar(
                medicion
            )

            return True

        return False
    
    def obtener_resumen_home(
        self,
        user_id
    ):

        mediciones = self.repository.listar_todas(
            user_id
        )

        total_inspecciones = len(mediciones)

        if total_inspecciones == 0:

            return {

                "total_inspecciones": 0,

                "vs_mes_anterior": "+0%",

                "inspecciones_optimas": 0,
                "porcentaje_optimas": "0%",

                "inspecciones_atencion": 0,
                "porcentaje_atencion": "0%",

                "inspecciones_criticas": 0,
                "porcentaje_criticas": "0%",

                "altura_promedio": 0,
                "desarrollo_promedio": 0,
                "humedad_promedio": 0,

                "con_plagas": 0,
                "con_enfermedad": 0

            }

        inspecciones_optimas = len([
            medicion
            for medicion in mediciones
            if medicion.salud == "Óptima"
        ])

        inspecciones_atencion = len([
            medicion
            for medicion in mediciones
            if medicion.salud == "Atención"
        ])

        inspecciones_criticas = len([
            medicion
            for medicion in mediciones
            if medicion.salud == "Crítica"
        ])

        altura_promedio = round(
            sum(
                m.altura or 0
                for m in mediciones
            ) / total_inspecciones,
            1
        )

        desarrollo_promedio = round(
            sum(
                m.desarrollo or 0
                for m in mediciones
            ) / total_inspecciones,
            1
        )

        humedad_promedio = round(
            sum(
                m.humedad_sustrato or 0
                for m in mediciones
            ) / total_inspecciones,
            1
        )

        con_plagas = len([
            m
            for m in mediciones
            if m.plagas
        ])

        con_enfermedad = len([
            m
            for m in mediciones
            if m.enfermedad
        ])

        return {

            "total_inspecciones": total_inspecciones,

            "vs_mes_anterior": "+0%",

            "inspecciones_optimas": inspecciones_optimas,
            "porcentaje_optimas": f"{round(inspecciones_optimas / total_inspecciones * 100,1)}%",

            "inspecciones_atencion": inspecciones_atencion,
            "porcentaje_atencion": f"{round(inspecciones_atencion / total_inspecciones * 100,1)}%",

            "inspecciones_criticas": inspecciones_criticas,
            "porcentaje_criticas": f"{round(inspecciones_criticas / total_inspecciones * 100,1)}%",

            "altura_promedio": altura_promedio,

            "desarrollo_promedio": desarrollo_promedio,

            "humedad_promedio": humedad_promedio,

            "con_plagas": con_plagas,

            "con_enfermedad": con_enfermedad

        }