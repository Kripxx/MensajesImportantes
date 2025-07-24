<?php
$host = "localhost";
$user = "root";
$password = "rott";
$database = "mi";

$conn = new mysqli($host, $user, $password, $database);
if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}

// Obtener áreas
$areas = $conn->query("SELECT area_id, nombre FROM areas");

// Obtener motivos
$motivos = $conn->query("SELECT motivo_id, nombre FROM motivos");
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registrar Citación</title>
    <style>
        /* ... Tu mismo CSS de antes ... */
    </style>
</head>
<body>
    <div class="container">
        <h1>Registrar Citación</h1>
        <p>Completa los campos para crear una nueva citación.</p>

        <form action="procesar_citacion.php" method="POST">
            <!-- Área -->
            <label for="area_id">Área:</label>
            <select name="area_id" required>
                <option value="">Selecciona un área</option>
                <?php while ($row = $areas->fetch_assoc()): ?>
                    <option value="<?= $row['area_id'] ?>"><?= htmlspecialchars($row['nombre']) ?></option>
                <?php endwhile; ?>
            </select>

            <!-- Motivo -->
            <label for="motivo_id">Motivo:</label>
            <select name="motivo_id" required>
                <option value="">Selecciona un motivo</option>
                <?php while ($row = $motivos->fetch_assoc()): ?>
                    <option value="<?= $row['motivo_id'] ?>"><?= htmlspecialchars($row['nombre']) ?></option>
                <?php endwhile; ?>
            </select>

            <!-- Asunto -->
            <label for="asunto">Asunto del correo:</label>
            <input type="text" name="asunto" placeholder="Ej. Recordatorio de reunión" required>

            <!-- Contenido -->
            <label for="contenido">Contenido del mensaje:</label>
            <textarea name="contenido" rows="5" placeholder="Escribe aquí los detalles de la citación..." required></textarea>

            <!-- Estado oculto -->
            <input type="hidden" name="estado" value="activo">

            <button type="submit">Guardar citación</button>
        </form>
    </div>
</body>
</html>
