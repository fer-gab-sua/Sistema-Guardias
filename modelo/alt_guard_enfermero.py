from modelo.Conect import ConexionConBase


class AltaGuardiasEnfermero(ConexionConBase):

    def fill_table_guard_ide(self):
        consulta = """SELECT grd_int_id , mov_txt_movil , CONCAT(par_txt_apellido , ' ',par_txt_nombre) , grd_fyh_inicio , grd_fyh_fin , CONCAT(med_txt_nombre, ' ', med_txt_apellido) , CONCAT(enf_txt_nombre, ' ', enf_txt_apellido)
                FROM Guardias 
                JOIN Paramedicos on grd_int_idparamedico = par_int_id
                JOIN Moviles on grd_int_idmovil = mov_int_id
                LEFT JOIN Medicos on grd_int_idmedico = med_int_id
                LEFT JOIN Enfermeros on grd_int_idenfermero = enf_int_id
                WHERE grd_txt_estado = 'incompleta' OR grd_txt_estado = 'completa'"""
        return self.ejecutar_consulta(consulta)
    
    def fill_table_enfermero_ide(self):
        consulta = """SELECT enf_int_id , enf_txt_nombre , enf_txt_apellido , enf_int_matricula
                FROM Enfermeros
                """
        return self.ejecutar_consulta(consulta)
    
    def fill_table_enfermero_idm_search(self,valor):
        consulta = """SELECT enf_int_id , enf_txt_nombre , enf_txt_apellido , enf_int_matricula
                FROM Enfermeros
                WHERE enf_txt_apellido LIKE ?
                """
        valor = ('%'+valor+'%')
        return self.ejecutar_consulta(consulta,valor)
        #HASTA ACA LLEGUE
    def to_assign_enfermero(self,id_enfermero , id_guardia):
        consulta = "UPDATE Guardias SET grd_int_idenfermero = ? WHERE grd_int_id = ?"
        self.ejecutar_consulta(consulta,id_enfermero,id_guardia)

    def alta_enfermero(self, nombre,apellido,matricula):
            consulta = "INSERT INTO [GuardiasMedicas].[dbo].[Enfermeros] ([enf_txt_nombre],[enf_txt_apellido],[enf_int_matricula]) VALUES (?, ?, ?)"
            self.ejecutar_consulta(consulta, nombre,apellido,matricula)

    def borrar_enfermero(self,id_enfermero):
            consulta = "DELETE FROM [GuardiasMedicas].[dbo].[Enfermeros] WHERE enf_int_id = (?)"
            self.ejecutar_consulta(consulta, id_enfermero)

    def update_enfermero(self,id_guardia,id_movil):
        consulta="UPDATE  [GuardiasMedicas].[dbo].[Guardias] SET grd_int_idenfermero = ? WHERE grd_int_id = ?"
        self.ejecutar_consulta(consulta,id_movil,id_guardia)