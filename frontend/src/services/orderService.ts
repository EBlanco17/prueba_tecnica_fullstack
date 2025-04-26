import axios from "axios";

const API_URL = "http://localhost:8000/ordenes";

/**
 * Representa un detalle de una orden.
 * @typedef {Object} DetalleOrden
 * @property {number} producto_id - ID del producto.
 * @property {number} cantidad - Cantidad del producto en la orden.
 */
export interface DetalleOrden {
  producto_id: number;
  cantidad: number;
}

/**
 * Representa los datos necesarios para crear una orden.
 * @typedef {Object} OrdenCreate
 * @property {DetalleOrden[]} detalles - Lista de detalles de la orden.
 */
export interface OrdenCreate {
  detalles: DetalleOrden[];
}

/**
 * Representa un detalle de una orden en la respuesta del backend.
 * @typedef {Object} DetalleOrdenOut
 * @property {number} id - ID del detalle.
 * @property {number} producto_id - ID del producto.
 * @property {number} cantidad - Cantidad del producto.
 * @property {number} precio_unitario - Precio unitario del producto.
 * @property {number} subtotal - Subtotal del detalle.
 */
export interface DetalleOrdenOut {
  id: number;
  producto_id: number;
  cantidad: number;
  precio_unitario: number;
  subtotal: number;
}

/**
 * Representa una orden completa en la respuesta del backend.
 * @typedef {Object} OrdenOut
 * @property {number} id - ID de la orden.
 * @property {string} fecha - Fecha de creación de la orden (ISO string).
 * @property {number} total - Total de la orden.
 * @property {DetalleOrdenOut[]} detalles - Lista de detalles de la orden.
 */
export interface OrdenOut {
  id: number;
  fecha: string;
  total: number;
  detalles: DetalleOrdenOut[];
}

/**
 * Crea una nueva orden.
 * @param {OrdenCreate} orderData - Datos de la orden a crear.
 * @returns {Promise<OrdenOut>} Una promesa que resuelve con la orden creada.
 */
export const createOrder = async (
  orderData: OrdenCreate
): Promise<OrdenOut> => {
  const response = await axios.post<OrdenOut>(API_URL, orderData);
  return response.data;
};

/**
 * Obtiene todas las órdenes registradas.
 * @returns {Promise<OrdenOut[]>} Una promesa que resuelve con un arreglo de órdenes.
 */
export const getOrders = async (): Promise<OrdenOut[]> => {
  const response = await axios.get<OrdenOut[]>(API_URL);
  return response.data;
};

/**
 * Obtiene una orden específica por su ID.
 * @param {number} id - ID de la orden a consultar.
 * @returns {Promise<OrdenOut>} Una promesa que resuelve con los datos de la orden.
 */
export const getOrderById = async (id: number): Promise<OrdenOut> => {
  const response = await axios.get<OrdenOut>(`${API_URL}/${id}`);
  return response.data;
};

/**
 * Actualiza una orden existente.
 * @param {number} id - ID de la orden a actualizar.
 * @param {OrdenCreate} orderData - Datos actualizados de la orden.
 * @returns {Promise<OrdenOut>} Una promesa que resuelve con la orden actualizada.
 */
export const updateOrder = async (
  id: number,
  orderData: OrdenCreate
): Promise<OrdenOut> => {
  const response = await axios.put<OrdenOut>(`${API_URL}/${id}`, orderData);
  return response.data;
};

/**
 * Elimina una orden por su ID.
 * @param {number} id - ID de la orden a eliminar.
 * @returns {Promise<void>} Una promesa que resuelve cuando la orden ha sido eliminada.
 */
export const deleteOrder = async (id: number): Promise<void> => {
  await axios.delete(`${API_URL}/${id}`);
};
