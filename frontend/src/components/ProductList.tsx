import React, { useState } from "react";
import { Producto } from "../services/productService";

const ProductList: React.FC<{
  products: Producto[];
  onAddProduct: (product: Producto, quantity: number) => void;
}> = ({ products, onAddProduct }) => {
  const [quantities, setQuantities] = useState<{ [key: number]: number }>({});

  const handleIncrease = (product: Producto) => {
    setQuantities((prev) => {
      const currentQuantity = prev[product.id] || 1;
      if (currentQuantity >= product.cantidad_disponible) {
        alert(
          `No puedes agregar más de ${product.cantidad_disponible} unidades de este producto.`
        );
        return prev;
      }
      return {
        ...prev,
        [product.id]: currentQuantity + 1,
      };
    });
  };

  const handleDecrease = (productId: number) => {
    setQuantities((prev) => ({
      ...prev,
      [productId]: Math.max((prev[productId] || 1) - 1, 1),
    }));
  };

  const handleAddProduct = (product: Producto) => {
    const quantity = quantities[product.id] || 1;
    onAddProduct(product, quantity);
  };

  return (
    <div className="mb-4">
      <h2 className="text-lg font-bold">Productos Disponibles</h2>
      <ul>
        {products.map((product) => (
          <li
            key={product.id}
            className="flex justify-between items-center p-2 border-b"
          >
            <div>
              <span>{product.nombre}</span>
              <p className="text-sm text-gray-500">
                Disponibles: {product.cantidad_disponible}
              </p>
            </div>
            <div className="flex items-center gap-2">
              <button
                onClick={() => handleDecrease(product.id)}
                className="bg-gray-300 text-black px-2 py-1 rounded"
              >
                -
              </button>
              <span>{quantities[product.id] || 1}</span>
              <button
                onClick={() => handleIncrease(product)}
                className="bg-gray-300 text-black px-2 py-1 rounded"
              >
                +
              </button>
              <button
                onClick={() => handleAddProduct(product)}
                className="bg-blue-500 text-white px-2 py-1 rounded"
              >
                Agregar
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;
