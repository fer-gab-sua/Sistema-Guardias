/*FUNCIONES
CREATE FUNCTION [dbo].[nombre]
(
[@nombre del parametro 1 tipo de dato del parametro 1],
[@nombre del parametro n tipo de dato del parametro n]
)
RETURNS [tipo de dato que la funcion devuelve]
AS
BEGIN
[codigo de la funcion]
RETURN [@valor que devuelve la funcion]
END
EJEMPLO:

CREATE FUNCTION [dbo].[sumame]
(
@a int,
@b int

)
RETURNS int
AS
BEGIN
declare @c int
set @c = @a + @b
RETURN @c
END
*/

CREATE FUNCTION [dbo].[nombre]
(
[@nombre del parametro 1 tipo de dato del parametro 1],
[@nombre del parametro n tipo de dato del parametro n]
)
RETURNS [tipo de dato que la funcion devuelve]
AS
BEGIN
[codigo de la funcion]
RETURN [@valor que devuelve la funcion]
END