import React, { useEffect, useState, useCallback } from "react";
import { useParams, useNavigate } from "react-router-dom";
import ProductItem from "../components/ProductItem";
import OrderSummary from "../components/OrderSummary";
import ValidationError from "../components/ValidationError";
import {
  getOrderById,
  updateOrder,
  OrdenCreate,
} from "../services/orderService";
import { getAllProducts, Producto } from "../services/productService";

/**
 * Vista para editar una orden existente.
 * @returns {JSX.Element} La vista EditOrder.
 */
const EditOrder: React.FC = () => {
  const { orderId } = useParams<{ orderId: string }>();
  const [selectedProducts, setSelectedProducts] = useState<
    { id: number; name: string; quantity: number; price: number }[]
  >([]);
  const [products, setProducts] = useState<Producto[]>([]);
  const [total, setTotal] = useState<number>(0);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const calculateTotal = useCallback((products: typeof selectedProducts) => {
    const total = products.reduce(
      (sum, product) => sum + product.quantity * product.price,
      0
    );
    setTotal(total);
  }, []);

  useEffect(() => {
    const fetchOrder = async () => {
      try {
        if (orderId) {
          const order = await getOrderById(Number(orderId));
          const allProducts = await getAllProducts();
          setProducts(allProducts);

          const productsInOrder = order.detalles.map((detalle) => {
            const product = allProducts.find(
              (p) => p.id === detalle.producto_id
            );
            return {
              id: detalle.producto_id,
              name: product
                ? product.nombre
                : `Producto ${detalle.producto_id}`,
              quantity: detalle.cantidad,
              price: detalle.precio_unitario,
            };
          });
          setSelectedProducts(productsInOrder);
          calculateTotal(productsInOrder);
        }
      } catch (error) {
        setError("Error al cargar la orden. Por favor, inténtalo más tarde.");
        console.error("Error fetching order:", error);
      }
    };

    fetchOrder();
  }, [orderId, calculateTotal]);

  const updateProduct = (
    index: number,
    field: keyof (typeof selectedProducts)[number],
    value: string | number
  ) => {
    const updatedProducts = [...selectedProducts];

    // No permitir cambiar el nombre del producto
    if (field === "name") {
      return;
    }

    // Validar cantidad mínima y máxima
    if (field === "quantity" && typeof value === "number") {
      const product = products.find((p) => p.id === updatedProducts[index].id);
      if (!product) return;

      if (value > product.cantidad_disponible) {
        setError(
          `No puedes agregar más de ${product.cantidad_disponible} unidades de este producto.`
        );
        return;
      }

      if (value < 1) {
        setError("La cantidad no puede ser menor que 1.");
        return;
      }
    }

    // Validar que el precio unitario no sea menor que 0
    if (field === "price" && typeof value === "number") {
      if (value < 0) {
        setError("El precio unitario no puede ser menor que 0.");
        return;
      }
    }

    setError(null); // Limpiar errores si la validación pasa
    updatedProducts[index][field] = value as never;
    setSelectedProducts(updatedProducts);
    calculateTotal(updatedProducts);
  };

  const removeProduct = (index: number) => {
    const updatedProducts = selectedProducts.filter((_, i) => i !== index);
    setSelectedProducts(updatedProducts);
    calculateTotal(updatedProducts);
  };

  const handleSubmit = async () => {
    try {
      const orderDetails = selectedProducts.map((product) => ({
        producto_id: product.id,
        cantidad: product.quantity,
        precio_unitario: product.price, // Enviar el precio unitario actualizado
      }));
      const updatedOrder: OrdenCreate = { detalles: orderDetails };

      if (orderId) {
        await updateOrder(Number(orderId), updatedOrder);
        alert("Orden actualizada exitosamente");
        navigate("/");
      }
    } catch (error) {
      setError("Error al actualizar la orden. Por favor, inténtalo más tarde.");
      console.error("Error al actualizar la orden:", error);
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Editar Orden</h1>
      {error && <ValidationError message={error} />}
      {selectedProducts.map((product, index) => (
        <ProductItem
          key={index}
          name={product.name}
          quantity={product.quantity}
          price={product.price}
          onRemove={() => removeProduct(index)}
          onUpdate={(field, value) => updateProduct(index, field, value)}
        />
      ))}
      <OrderSummary total={total} />
      <button
        onClick={handleSubmit}
        className="bg-blue-500 text-white px-4 py-2 rounded mt-4"
      >
        Guardar Cambios
      </button>
      <button
        onClick={() => navigate("/")}
        className="bg-gray-500 text-white px-4 py-2 rounded mt-4 ml-4"
      >
        Cancelar
      </button>
    </div>
  );
};

export default EditOrder;
