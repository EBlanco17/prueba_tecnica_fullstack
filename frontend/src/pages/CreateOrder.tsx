import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import ProductItem from "../components/ProductItem";
import ProductList from "../components/ProductList";
import OrderSummary from "../components/OrderSummary";
import ValidationError from "../components/ValidationError";
import { createOrder } from "../services/orderService";
import { getAllProducts, Producto } from "../services/productService";

const CreateOrder: React.FC = () => {
  const [products, setProducts] = useState<Producto[]>([]);
  const [selectedProducts, setSelectedProducts] = useState<
    { id: number; name: string; quantity: number; price: number }[]
  >([]);
  const [total, setTotal] = useState<number>(0);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const data = await getAllProducts();
        setProducts(data);
      } catch (error) {
        setError(
          "Error al cargar los productos. Por favor, inténtalo más tarde."
        );
        console.error("Error fetching products:", error);
      }
    };
    fetchProducts();
  }, []);

  const addProduct = (product: Producto, quantity: number) => {
    const existingProductIndex = selectedProducts.findIndex(
      (p) => p.id === product.id
    );

    const totalQuantityInCart = selectedProducts.reduce((sum, p) => {
      if (p.id === product.id) {
        return sum + p.quantity;
      }
      return sum;
    }, 0);

    if (totalQuantityInCart + quantity > product.cantidad_disponible) {
      setError(
        `No puedes agregar más de ${product.cantidad_disponible} unidades de este producto.`
      );
      return;
    }

    setError(null); // Limpiar errores si la validación pasa

    if (existingProductIndex !== -1) {
      const updatedProducts = [...selectedProducts];
      updatedProducts[existingProductIndex].quantity += quantity;
      setSelectedProducts(updatedProducts);
    } else {
      setSelectedProducts([
        ...selectedProducts,
        {
          id: product.id,
          name: product.nombre,
          quantity,
          price: product.precio_unitario,
        },
      ]);
    }
    calculateTotal([
      ...selectedProducts,
      {
        id: product.id,
        name: product.nombre,
        quantity,
        price: product.precio_unitario,
      },
    ]);
  };

  const removeProduct = (index: number) => {
    const updatedProducts = selectedProducts.filter((_, i) => i !== index);
    setSelectedProducts(updatedProducts);
    calculateTotal(updatedProducts);
  };

  const updateProduct = (
    index: number,
    field: keyof (typeof selectedProducts)[number],
    value: string | number
  ) => {
    const updatedProducts = [...selectedProducts];

    if (field === "name") {
      return;
    }

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

    setError(null); // Limpiar errores si la validación pasa
    updatedProducts[index][field] = value as never;
    setSelectedProducts(updatedProducts);
    calculateTotal(updatedProducts);
  };

  const calculateTotal = (products: typeof selectedProducts) => {
    const total = products.reduce(
      (sum, product) => sum + product.quantity * product.price,
      0
    );
    setTotal(total);
  };

  const handleSubmit = async () => {
    try {
      const orderDetails = selectedProducts.map((product) => ({
        producto_id: product.id,
        cantidad: product.quantity,
      }));
      await createOrder({ detalles: orderDetails });
      alert("Orden creada exitosamente");
      navigate("/");
    } catch (error) {
      setError("Error al registrar la orden. Por favor, inténtalo más tarde.");
      console.error("Error creating order:", error);
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Crear Orden</h1>
      {error && <ValidationError message={error} />}
      <ProductList products={products} onAddProduct={addProduct} />
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
        className="bg-green-500 text-white px-4 py-2 rounded mt-4"
      >
        Registrar Orden
      </button>
      <button
        onClick={() => navigate("/")}
        className="bg-gray-500 text-white px-4 py-2 rounded mt-4"
      >
        Volver al Inicio
      </button>
    </div>
  );
};

export default CreateOrder;
