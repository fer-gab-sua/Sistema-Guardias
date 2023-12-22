/* ESTRUCTURAS DEL IF,ELSE,WHILE  ejemplos*/
IF @k<5
BEGIN
select @k,'Menor que 5'
END
ELSE
BEGIN
select @k, 'Mayor o iual a 5'
END

------------------------------------------------------------
declare @k int
set @k = 1

WHILE @k>5
BEGIN
	set @k = @k+1
END
	SELECT @k
----------------------------------------------