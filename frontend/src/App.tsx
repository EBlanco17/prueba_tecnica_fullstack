import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import OrderList from "./pages/OrderList";
import CreateOrder from "./pages/CreateOrder";
import EditOrder from "./pages/EditOrder";
import OrderDetail from "./pages/OrderDetail";
import TopProducts from "./pages/TopProducts";

const App: React.FC = () => {
  return (
    <Router>
      <div className="container mx-auto p-4">
        <Routes>
          <Route path="/" element={<OrderList />} />
          <Route path="/create-order" element={<CreateOrder />} />
          <Route path="/orders/:orderId" element={<OrderDetail />} />
          <Route path="/edit-order/:orderId" element={<EditOrder />} />
          <Route path="/top-products" element={<TopProducts />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
