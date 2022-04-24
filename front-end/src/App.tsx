import { Route, Routes } from "react-router-dom";
import { ThemeProvider, createTheme } from "@mui/material/styles";

import Home from "./components/home/Home";
import Layout from "./components/Layout";

const theme = createTheme({
  palette: {
    primary: {
      main: "#5ece7b",
    },
  },
});

const App = () => {
  return (
    <ThemeProvider theme={theme}>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
        </Route>
      </Routes>
    </ThemeProvider>
  );
};

export default App;
