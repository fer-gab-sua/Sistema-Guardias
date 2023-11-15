class Guardia:
    def __init__(self,
                movil_guardia,
                medico_guardia,
                paramedico_guardia,
                enfermero_guardia,
                fyh_inicio_guardia,
                fyh_fin_guardia,
                observaciones_guardia,
                estado_guardia
                ) -> None:
        self.movil_guardia = movil_guardia
        self.medico_guardia =  medico_guardia
        self.paramedico_guardia = paramedico_guardia
        self.enfermero_guardia = enfermero_guardia
        self.fyh_inicio_guardia = fyh_inicio_guardia

        
        self.fyh_fin_guardia = fyh_fin_guardia
        self.observaciones_guardia = observaciones_guardia
        self.estado_guardia = estado_guardia