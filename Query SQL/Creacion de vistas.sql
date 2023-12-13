CREATE VIEW Guardias_View AS
SELECT
    grd_int_id as ID_Guardia,
    mov_txt_movil as Movil,
    CONCAT (med_txt_apellido,' ',med_txt_nombre) as Medico,
    CONCAT (par_txt_apellido,' ',par_txt_nombre) as Paramedico,
    CONCAT (enf_txt_apellido,' ',enf_txt_nombre) as Enfermero,
    grd_fyh_inicio as Inicio,
    grd_fyh_fin as Fin,
    grd_int_duracionguardiahs as Duracion_Guardia,
    grd_txt_observaciones as Observacion,
    grd_txt_estado as Estado
FROM GUARDIAS
JOIN Moviles ON grd_int_idmovil = mov_int_id
JOIN Paramedicos ON grd_int_idparamedico = par_int_id
JOIN Medicos ON grd_int_idmedico = med_int_id
JOIN Enfermeros ON grd_int_idenfermero = enf_int_id;