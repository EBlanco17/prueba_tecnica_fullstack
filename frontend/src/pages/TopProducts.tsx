import React, { useEffect, useState } from "react";
import {
  getTop3Products,
  downloadTop3ProductsPDF,
  ProductoTop,
} from "../services/productService";
import { useNavigate } from "react-router-dom";

/**
 * Vista para mostrar el top 3 de productos más comprados.
 * @returns {JSX.Element} La vista TopProducts.
 */
const TopProducts: React.FC = () => {
  const [topProducts, setTopProducts] = useState<ProductoTop[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchTopProducts = async () => {
      try {
        const data = await getTop3Products();
        setTopProducts(data);
      } catch (error) {
        console.error("Error al obtener los productos más comprados:", error);
      }
    };

    fetchTopProducts();
  }, []);

  const handleDownloadPDF = async () => {
    try {
      const pdfData = await downloadTop3ProductsPDF();
      const url = window.URL.createObjectURL(new Blob([pdfData]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "top3-productos.pdf");
      document.body.appendChild(link);
      link.click();
    } catch (error) {
      console.error("Error al descargar el PDF:", error);
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Top 3 Productos Más Comprados</h1>
      <ul>
        {topProducts.map((product, index) => (
          <li key={index} className="p-4 border-b">
            <h2 className="text-lg font-semibold">{product.nombre}</h2>
            <p className="text-sm text-gray-500">
              Cantidad vendida: {product.total_comprado}
            </p>
          </li>
        ))}
      </ul>
      <button
        onClick={handleDownloadPDF}
        className="bg-blue-500 text-white px-4 py-2 rounded mt-4"
      >
        Descargar Reporte en PDF
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

export default TopProducts;
