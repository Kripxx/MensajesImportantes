<?php
include 'conexion.php';

$area_id = $_POST['area_id'];
$motivo_id = $_POST['motivo_id'];
$asunto = $_POST['asunto'];
$contenido = $_POST['contenido'];
$estado = $_POST['estado'];

$sql = "INSERT INTO citaciones (area_id, motivo_id, asunto, contenido, estado)
        VALUES (?, ?, ?, ?, ?)";

$stmt = $conn->prepare($sql);
$stmt->bind_param("iisss", $area_id, $motivo_id, $asunto, $contenido, $estado);

if ($stmt->execute()) {
    echo "Citacion guardada exitosamente.";
    // Puedes redirigir si lo prefieres
    // header("Location: mostrar_citaciones.php");
} else {
    echo "Error al guardar: " . $conn->error;
}
?>
