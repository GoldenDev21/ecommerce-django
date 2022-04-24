import { Box } from "@mui/material";
import Navigator from "./navigator/Navigator";
import { Outlet } from "react-router-dom";

const Layout = () => {
  return (
    <Box sx={{ mx: 8 }}>
      <Navigator />
      <Outlet />
    </Box>
  );
};

export default Layout;
