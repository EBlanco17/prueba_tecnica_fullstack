import React from "react";

/**
 * Propiedades del componente OrderSummary.
 * @typedef {Object} OrderSummaryProps
 * @property {number} total - Total de la orden.
 */

/**
 * Componente para mostrar el resumen de la orden.
 * @param {OrderSummaryProps} props - Propiedades del componente.
 * @returns {JSX.Element} El componente OrderSummary.
 */
const OrderSummary: React.FC<{ total: number }> = ({ total }) => {
  return (
    <div className="p-4 bg-gray-100 rounded-lg">
      <h2 className="text-xl font-bold">Resumen de la Orden</h2>
      <p className="text-lg mt-2">Total: ${total.toFixed(2)}</p>
    </div>
  );
};

export default OrderSummary;
