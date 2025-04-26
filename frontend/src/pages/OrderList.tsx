import React, { useEffect, useState } from "react";
import { getOrders, OrdenOut } from "../services/orderService";
import { useNavigate } from "react-router-dom";

/**
 * Vista para mostrar la lista de órdenes.
 * @returns {JSX.Element} La vista OrderList.
 */
const OrderList: React.FC = () => {
  const [orders, setOrders] = useState<OrdenOut[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const data = await getOrders();
        setOrders(data);
      } catch (error) {
        console.error("Error al obtener las órdenes:", error);
      }
    };

    fetchOrders();
  }, []);

  const handleViewDetails = (orderId: number) => {
    navigate(`/orders/${orderId}`);
  };

  const handleCreateOrder = () => {
    navigate("/create-order");
  };

  const handleViewTopProducts = () => {
    navigate("/top-products");
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Lista de Órdenes</h1>
      <div className="flex gap-4 mb-4">
        <button
          onClick={handleCreateOrder}
          className="bg-green-500 text-white px-4 py-2 rounded"
        >
          Crear Nueva Orden
        </button>
        <button
          onClick={handleViewTopProducts}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Ver Top 3 Productos
        </button>
      </div>
      {orders.length === 0 ? (
        <p>No hay órdenes registradas.</p>
      ) : (
        <ul>
          {orders.map((order) => (
            <li
              key={order.id}
              className="p-2 border-b flex justify-between items-center"
            >
              <div>
                <p>
                  <strong>ID:</strong> {order.id}
                </p>
                <p>
                  <strong>Fecha:</strong>{" "}
                  {new Date(order.fecha).toLocaleString()}
                </p>
                <p>
                  <strong>Total:</strong> ${order.total.toFixed(2)}
                </p>
              </div>
              <button
                onClick={() => handleViewDetails(order.id)}
                className="bg-blue-500 text-white px-4 py-2 rounded"
              >
                Ver Detalles
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default OrderList;
