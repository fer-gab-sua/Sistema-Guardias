/*TRIGGERS*/

CREATE TRIGGER [instancia_enfermero]
ON Enfermeros
AFTER INSERT /*puede ir DELETE o UPDATE y esto se ejecuta cuando se inserta, borra, o se hace un update*/
AS
BEGIN
	UPDATE Enfermeros
	SET enfermeros.instante = GETDATE()
	FROM Enfermeros
	INNER JOIN inserted ON Enfermeros.enf_int_id = inserted.enf_int_id;
END;