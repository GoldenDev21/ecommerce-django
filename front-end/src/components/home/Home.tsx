import "react-responsive-carousel/lib/styles/carousel.min.css";

import Carousel from "./Carousel";
import { Stack } from "@mui/material";

const Home = () => {
  return (
    <Stack justifyContent="center" alignItems="center" spacing={16}>
      <Carousel />
    </Stack>
  );
};

export default Home;
