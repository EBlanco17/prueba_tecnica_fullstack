import axios from "axios";

const API_URL = "http://localhost:8000/productos";

/**
 * Representa un producto en el sistema.
 * @typedef {Object} Producto
 * @property {number} id - ID único del producto.
 * @property {string} nombre - Nombre del producto.
 * @property {number} cantidad_disponible - Cantidad disponible en inventario.
 * @property {number} precio_unitario - Precio unitario del producto.
 */
export interface Producto {
  id: number;
  nombre: string;
  cantidad_disponible: number;
  precio_unitario: number;
}

/**
 * Representa un producto destacado en el top 3.
 * @typedef {Object} ProductoTop
 * @property {string} nombre - Nombre del producto.
 * @property {number} total_comprado - Total de unidades compradas.
 * @property {number} precio_unitario - Precio unitario del producto.
 */
export interface ProductoTop {
  nombre: string;
  total_comprado: number;
  precio_unitario: number;
}

/**
 * Obtiene la lista de todos los productos disponibles.
 * @returns {Promise<Producto[]>} Una promesa que resuelve con un arreglo de productos.
 */
export const getAllProducts = async (): Promise<Producto[]> => {
  const response = await axios.get<Producto[]>(API_URL);
  return response.data;
};

/**
 * Obtiene el top 3 de productos más comprados.
 * @returns {Promise<ProductoTop[]>} Una promesa que resuelve con un arreglo de productos destacados.
 */
export const getTop3Products = async (): Promise<ProductoTop[]> => {
  const response = await axios.get<ProductoTop[]>(`${API_URL}/top3`);
  return response.data;
};

/**
 * Descarga un reporte en PDF con el top 3 de productos más comprados.
 * @returns {Promise<Blob>} Una promesa que resuelve con un archivo Blob del PDF.
 */
export const downloadTop3ProductsPDF = async (): Promise<Blob> => {
  const response = await axios.get(`${API_URL}/top3/pdf`, {
    responseType: "blob",
  });
  return response.data;
};
