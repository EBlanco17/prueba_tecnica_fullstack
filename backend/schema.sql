DROP DATABASE IF EXISTS ordenesdb;
CREATE DATABASE ordenesdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ordenesdb;

CREATE TABLE producto (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  cantidad_disponible INT NOT NULL CHECK (cantidad_disponible >= 0),
  precio_unitario DECIMAL(10,2) NOT NULL CHECK (precio_unitario >= 0),
  INDEX(nombre)
);

CREATE TABLE orden (
  id INT AUTO_INCREMENT PRIMARY KEY,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  total DECIMAL(10,2) NOT NULL CHECK (total >= 0)
);

CREATE TABLE detalle_orden (
  id INT AUTO_INCREMENT PRIMARY KEY,
  orden_id INT NOT NULL,
  producto_id INT NOT NULL,
  cantidad INT NOT NULL CHECK (cantidad > 0),
  precio_unitario DECIMAL(10,2) NOT NULL CHECK (precio_unitario > 0),
  subtotal DECIMAL(10,2) NOT NULL CHECK (subtotal >= 0),
  FOREIGN KEY (orden_id) REFERENCES orden(id) ON DELETE CASCADE,
  FOREIGN KEY (producto_id) REFERENCES producto(id) ON DELETE CASCADE,
  INDEX(orden_id),
  INDEX(producto_id)
);
