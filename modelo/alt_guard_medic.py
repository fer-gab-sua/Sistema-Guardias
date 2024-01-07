from modelo.Conect import ConexionConBase

class AltaGuardiasMedicos(ConexionConBase):

    def fill_table_guard_idm(self):
        consulta = """SELECT grd_int_id , mov_txt_movil , CONCAT(par_txt_apellido , ' ',par_txt_nombre) , grd_fyh_inicio , grd_fyh_fin , CONCAT(med_txt_nombre, ' ', med_txt_apellido)
                FROM Guardias 
                JOIN Paramedicos on grd_int_idparamedico = par_int_id
                JOIN Moviles on grd_int_idmovil = mov_int_id
                LEFT JOIN Medicos on grd_int_idmedico = med_int_id
                WHERE grd_txt_estado = 'incompleta' OR grd_txt_estado = 'completa'"""
        return self.ejecutar_consulta(consulta)
    
    def fill_table_medico_idm(self):
        consulta = """SELECT med_int_id , med_txt_nombre , med_txt_apellido , med_int_matricula
                FROM Medicos
                """
        return self.ejecutar_consulta(consulta)
    
    def fill_table_medicos_idm_search(self,valor):
        consulta = """SELECT med_int_id , med_txt_nombre , med_txt_apellido , med_int_matricula
                FROM Medicos
                WHERE med_txt_apellido LIKE ?
                """
        valor = ('%'+valor+'%')
        return self.ejecutar_consulta(consulta,valor)
        
    def to_assign_medico(self,id_medico , id_guardia):
        print(id_medico +  id_guardia)
        consulta = "UPDATE Guardias SET grd_int_idmedico = ? WHERE grd_int_id = ?"
        self.ejecutar_consulta(consulta,int(id_medico),int(id_guardia))

    def alta_medico(self, nombre,apellido,matricula):
            consulta = "INSERT INTO [GuardiasMedicas].[dbo].[Medicos] ([med_txt_nombre],[med_txt_apellido],[med_int_matricula]) VALUES (?, ?, ?)"
            self.ejecutar_consulta(consulta, nombre,apellido,matricula)

    def borrar_medico(self,id_medico):
            consulta = "DELETE FROM [GuardiasMedicas].[dbo].[Medicos] WHERE med_int_id = (?)"
            self.ejecutar_consulta(consulta, id_medico)