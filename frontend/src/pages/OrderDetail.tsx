import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getOrderById, deleteOrder, OrdenOut } from "../services/orderService";

/**
 * Vista para mostrar los detalles de una orden específica.
 * @returns {JSX.Element} La vista OrderDetail.
 */
const OrderDetail: React.FC = () => {
  const { orderId } = useParams<{ orderId: string }>();
  const [order, setOrder] = useState<OrdenOut | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchOrder = async () => {
      try {
        if (orderId) {
          const data = await getOrderById(Number(orderId));
          setOrder(data);
        }
      } catch (error) {
        console.error("Error al obtener los detalles de la orden:", error);
      }
    };

    fetchOrder();
  }, [orderId]);

  const handleDelete = async () => {
    if (!orderId) return;

    const confirmDelete = window.confirm(
      "¿Estás seguro de que deseas borrar esta orden?"
    );
    if (!confirmDelete) return;

    try {
      await deleteOrder(Number(orderId));
      alert("Orden borrada exitosamente");
      navigate("/");
    } catch (error) {
      console.error("Error al borrar la orden:", error);
      alert(
        "Hubo un error al intentar borrar la orden. Por favor, inténtalo más tarde."
      );
    }
  };

  if (!order) {
    return <p>Cargando detalles de la orden...</p>;
  }

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Detalles de la Orden</h1>
      <p>
        <strong>ID:</strong> {order.id}
      </p>
      <p>
        <strong>Fecha:</strong> {new Date(order.fecha).toLocaleString()}
      </p>
      <p>
        <strong>Total:</strong> ${order.total.toFixed(2)}
      </p>
      <h2 className="text-lg font-bold mt-4">Productos:</h2>
      <ul>
        {order.detalles.map((detalle) => (
          <li key={detalle.id} className="p-2 border-b">
            <p>
              <strong>Producto ID:</strong> {detalle.producto_id}
            </p>
            <p>
              <strong>Cantidad:</strong> {detalle.cantidad}
            </p>
            <p>
              <strong>Precio Unitario:</strong> $
              {detalle.precio_unitario.toFixed(2)}
            </p>
            <p>
              <strong>Subtotal:</strong> ${detalle.subtotal.toFixed(2)}
            </p>
          </li>
        ))}
      </ul>
      <button
        onClick={() => navigate(`/edit-order/${order.id}`)}
        className="bg-blue-500 text-white px-4 py-2 rounded mt-4"
      >
        Editar Orden
      </button>
      <button
        onClick={handleDelete}
        className="bg-red-500 text-white px-4 py-2 rounded mt-4 ml-4"
      >
        Borrar Orden
      </button>
      <button
        onClick={() => navigate("/")}
        className="bg-gray-500 text-white px-4 py-2 rounded mt-4 ml-4"
      >
        Volver al Inicio
      </button>
    </div>
  );
};

export default OrderDetail;
