CREATE DATABASE IF NOT EXISTS gestor_tareas_db;
USE gestor_tareas_db;


CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE estados_tarea (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Inserción de estados iniciales
INSERT INTO estados_tarea (nombre) VALUES 
('Pendiente'),
('En Progreso'),
('Completada'),
('Cancelada');


CREATE TABLE prioridades_tarea (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Inserción de prioridades iniciales
INSERT INTO prioridades_tarea (nombre) VALUES
('Baja'),
('Media'),
('Alta');

CREATE TABLE tareas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descripcion TEXT,
    fecha_vencimiento DATE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_creador INT NOT NULL,
    id_asignado INT,
    id_estado INT NOT NULL,
    id_prioridad INT NOT NULL,
    FOREIGN KEY (id_creador) REFERENCES usuarios(id),
    FOREIGN KEY (id_asignado) REFERENCES usuarios(id),
    FOREIGN KEY (id_estado) REFERENCES estados_tarea(id),
    FOREIGN KEY (id_prioridad) REFERENCES prioridades_tarea(id)
);


