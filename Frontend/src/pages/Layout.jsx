import React from "react";
import Navbar from "../components/Navbar/Navbar";
import { Outlet, Link } from "react-router-dom";
import Footer from "../components/Footer/Footer";
import OrderPopup from "../components/OrderPopup/OrderPopup";

const Layout = ({ showMenu, setShowMenu }) => {
  const [orderPopup, setOrderPopup] = React.useState(false);

  const handleOrderPopup = () => {
    setOrderPopup(!orderPopup);
  };
  return (
    <>
      <Navbar
        handleOrderPopup={handleOrderPopup}
        showMenu={showMenu}
        setShowMenu={setShowMenu}
      />
      <Outlet />
      <Footer />
      <OrderPopup orderPopup={orderPopup} setOrderPopup={setOrderPopup} />
    </>
  );
};

export default Layout;
