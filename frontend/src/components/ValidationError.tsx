import React from "react";

/**
 * Propiedades del componente ValidationError.
 * @typedef {Object} ValidationErrorProps
 * @property {string} message - Mensaje de error a mostrar.
 */

/**
 * Componente para mostrar mensajes de error de validación.
 * @param {ValidationErrorProps} props - Propiedades del componente.
 * @returns {JSX.Element} El componente ValidationError.
 */
const ValidationError: React.FC<{ message: string }> = ({ message }) => {
  return (
    <div className="text-red-500 text-sm mt-2">
      <p>{message}</p>
    </div>
  );
};

export default ValidationError;
