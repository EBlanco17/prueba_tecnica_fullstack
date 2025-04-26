import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import OrderList from "./pages/OrderList";
import CreateOrder from "./pages/CreateOrder";

const App: React.FC = () => {
  return (
    <Router>
      <div className="container mx-auto p-4">
        <Routes>
          <Route path="/" element={<OrderList />} />
          <Route path="/create-order" element={<CreateOrder />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
