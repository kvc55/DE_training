-- Listar los nombres de los proveedores cuya ciudad contenga la cadena de texto “Ramos”.
SELECT Nombre, Ciudad
FROM Proveedor
WHERE Ciudad LIKE '%Ramos%'

--  Listar los códigos de los materiales que provea el proveedor 4 y no los provea el proveedor 5. Se debe resolver de 3 formas.
SELECT CodMat
FROM Provisto_Por
WHERE CodProv=4 AND CodMat NOT IN (SELECT CodMat
                                   FROM Provisto_Por
                                   WHERE CodProv=5)

SELECT CodMat
FROM Provisto_Por a
WHERE CodProv=4 AND NOT EXISTS (SELECT CodMat
                                FROM Provisto_Por b
                                WHERE CodProv=5 AND a.CodMat=b.CodMat)

SELECT CodMat
FROM Provisto_Por
WHERE CodProv=4
EXCEPT 
SELECT CodMat
FROM Provisto_Por
WHERE CodProv=5


-- Listar los materiales, código y descripción, provistos por proveedores de la ciudad de Ramos Mejía.
SELECT m.*
FROM Material m 
INNER JOIN Provisto_Por pp ON m.CodMat=pp.CodMat
INNER JOIN Proveedor p ON pp.CodProv=p.CodProv
WHERE Ciudad='Ramos Mejia'


-- Listar los proveedores y materiales que provee. La lista resultante debe incluir a aquellos proveedores que no proveen ningún material.
SELECT p.CodProv, p.Nombre, pp.CodMat, m.Descripcion
FROM Proveedor p 
LEFT JOIN Provisto_Por pp ON p.CodProv=pp.CodProv
LEFT JOIN Material m ON pp.CodMat=m.CodMat

-- Listar los artículos que cuesten más de $30 o que estén compuestos por el material 2.
SELECT a.CodArt
FROM Articulo a 
INNER JOIN Compuesto_Por cp ON a.CodArt=cp.CodArt
WHERE a.Precio>30
UNION 
SELECT cp.CodArt
FROM Compuesto_Por cp
WHERE cp.CodMat='2'


-- Listar los artículos de Mayor precio.
SELECT a.Precio, a.Descripcion
FROM Articulo a
WHERE a.Precio > (SELECT AVG(Precio)
                           FROM Articulo)


-- Listar los proveedores que proveen más de 3 materiales
SELECT pp.CodProv, COUNT(*) AS Total
FROM Provisto_Por pp
GROUP BY pp.CodProv
HAVING COUNT(*)>3
ORDER BY COUNT(*) DESC


-- Crear una vista para el caso de los proveedores que proveen más de 4 materiales. Mostrar la forma de invocar esa vista.
CREATE VIEW v_proveedores_mas_cuatro_materiales AS
SELECT pp.CodProv, COUNT(*) AS Total
FROM Provisto_Por pp
GROUP BY pp.CodProv
HAVING COUNT(*)>4

SELECT *
FROM v_proveedores_mas_cuatro_materiales