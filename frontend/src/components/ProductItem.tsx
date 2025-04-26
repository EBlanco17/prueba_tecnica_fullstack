import React from "react";

/**
 * Propiedades del componente ProductItem.
 * @typedef {Object} ProductItemProps
 * @property {string} name - Nombre del producto.
 * @property {number} quantity - Cantidad del producto.
 * @property {number} price - Precio unitario del producto.
 * @property {() => void} onRemove - Función para eliminar el producto.
 * @property {(field: "name" | "quantity" | "price", value: string | number) => void} onUpdate - Función para actualizar los datos del producto.
 */

/**
 * Componente para mostrar los detalles de un producto.
 * @param {ProductItemProps} props - Propiedades del componente.
 * @returns {JSX.Element} El componente ProductItem.
 */
const ProductItem: React.FC<{
  name: string;
  quantity: number;
  price: number;
  onRemove: () => void;
  onUpdate: (
    field: "name" | "quantity" | "price",
    value: string | number
  ) => void;
}> = ({ name, quantity, price, onRemove, onUpdate }) => {
  const subtotal = quantity * price;

  return (
    <div className="flex justify-between items-center p-4 border-b">
      <div>
        <input
          type="text"
          value={name}
          onChange={(e) => onUpdate("name", e.target.value)}
          placeholder="Nombre del producto"
          className="border p-2 rounded w-full"
        />
        <input
          type="number"
          value={quantity}
          onChange={(e) => onUpdate("quantity", parseInt(e.target.value, 10))}
          placeholder="Cantidad"
          className="border p-2 rounded w-full mt-2"
        />
        <input
          type="number"
          value={price}
          onChange={(e) => onUpdate("price", parseFloat(e.target.value))}
          placeholder="Precio unitario"
          className="border p-2 rounded w-full mt-2"
        />
      </div>
      <div>
        <p className="text-lg font-bold">Subtotal: ${subtotal.toFixed(2)}</p>
        <button
          onClick={onRemove}
          className="text-red-500 hover:underline mt-2"
        >
          Eliminar
        </button>
      </div>
    </div>
  );
};

export default ProductItem;
