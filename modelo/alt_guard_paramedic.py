from modelo.Conect import ConexionConBase

class AltaGuardiaMovilParamedico(ConexionConBase):
    def fill_Bases_sql(self):
        consulta = "SELECT mov_int_id , mov_txt_movil, mov_txt_patente FROM Moviles"
        return self.ejecutar_consulta(consulta)

    def movil_datos(self, base):
        consulta = "SELECT mov_int_id ,mov_txt_movil , mov_txt_patente FROM Moviles WHERE mov_int_id = ?"
        return self.ejecutar_consulta(consulta, base)

    def alta_movil(self, movil, patente):
        consulta = "INSERT INTO [GuardiasMedicas].[dbo].[Moviles] ([mov_txt_movil], [mov_txt_patente]) VALUES (?, ?)"
        self.ejecutar_consulta(consulta, movil, patente)

    def borrar_movil(self,movil):
        consulta = "DELETE FROM [GuardiasMedicas].[dbo].[Moviles] WHERE mov_txt_movil = (?)"
        self.ejecutar_consulta(consulta, movil)

    def fill_paramedicos_sql(self):
        consulta = "SELECT par_int_id , par_int_legajo, par_txt_nombre, par_txt_apellido, par_fch_vencimientolicencia FROM Paramedicos"
        return self.ejecutar_consulta(consulta)

    def paramedicos_datos(self, legajo):
        consulta = "SELECT par_int_id , par_int_legajo, par_txt_nombre, par_txt_apellido, par_fch_vencimientolicencia FROM Paramedicos WHERE par_int_id = (?)"
        return self.ejecutar_consulta(consulta, legajo)

    def alta_paramedico(self, legajo,nombre,apellido,fechavencimiento):
        consulta = "INSERT INTO [GuardiasMedicas].[dbo].[Paramedicos] ([par_int_legajo],[par_txt_nombre],[par_txt_apellido],[par_fch_vencimientolicencia]) VALUES (?, ?, ?, ?)"
        self.ejecutar_consulta(consulta, legajo,nombre,apellido,fechavencimiento)

    def borrar_paramedico(self,movil):
        consulta = "DELETE FROM [GuardiasMedicas].[dbo].[Paramedicos] WHERE par_int_legajo = (?)"
        self.ejecutar_consulta(consulta, movil)

    def fill_table_guard_adg(self):
        consulta = """SELECT grd_int_id , mov_txt_movil , par_txt_apellido , par_txt_nombre , grd_fyh_inicio , grd_fyh_fin
                FROM Guardias 
                JOIN Paramedicos on grd_int_idparamedico = par_int_id
                JOIN Moviles on grd_int_idmovil = mov_int_id
                WHERE grd_txt_estado = 'incompleta' OR grd_txt_estado = 'completa'"""
        return self.ejecutar_consulta(consulta)

    def alta_guardia_movil(self,idmovil,idparamedico,fyh_inicio,fyh_fin):
        consulta = "INSERT INTO [GuardiasMedicas].[dbo].[Guardias] ([grd_int_idmovil],[grd_int_idparamedico],[grd_fyh_inicio],[grd_fyh_fin],[grd_txt_estado]) VALUES (?, ?, ?, ? , ?)"
        self.ejecutar_consulta(consulta, idmovil,idparamedico,fyh_inicio,fyh_fin,"incompleta")

    def update_movil(self,id_guardia,id_movil):
        consulta="UPDATE  [GuardiasMedicas].[dbo].[Guardias] SET grd_int_idmovil = ? WHERE grd_int_id = ?"
        self.ejecutar_consulta(consulta,id_movil,id_guardia)

    def update_paramedico(self,id_guardia,id_movil):
        consulta="UPDATE  [GuardiasMedicas].[dbo].[Guardias] SET grd_int_idparamedico= ? WHERE grd_int_id = ?"
        self.ejecutar_consulta(consulta,id_movil,id_guardia)