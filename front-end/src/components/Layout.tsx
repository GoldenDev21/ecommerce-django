import { Box, useTheme } from "@mui/material";

import Footer from "./footer/Footer";
import Navigator from "./navigator/Navigator";
import { Outlet } from "react-router-dom";

const Layout = () => {
  const theme = useTheme();

  const styles = {
    container: {
      [theme.breakpoints.down("lg")]: {
        marginRight: 4,
        marginLeft: 4,
      },
      marginRight: 8,
      marginLeft: 8,
    },
  };

  return (
    <>
      <Box sx={styles.container}>
        <Navigator />
        <Outlet />
      </Box>
      <Footer />
    </>
  );
};

export default Layout;
