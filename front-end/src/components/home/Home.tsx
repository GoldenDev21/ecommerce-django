import "react-responsive-carousel/lib/styles/carousel.min.css";

import Carousel from "./Carousel";
import ImageQuilt from "../ImageQuilt";
import { Stack } from "@mui/material";
import casualWear from "../../static/images/home/christian-bolt-VW5VjskNXZ8-unsplash.jpg";
import cocktailDress from "../../static/images/home/hanen-souhail-QwfgUwHoJDM-unsplash.jpg";
import officeWear from "../../static/images/home/laura-chouette-WQgvRkmqRrg-unsplash.jpg";
import sandals from "../../static/images/home/irene-kredenets-DDqxX0-7vKE-unsplash.jpg";

const imageData = [
  {
    img: cocktailDress,
    title: "Woman wearing metallic dress",
    rows: 2,
    cols: 1,
  },
  {
    img: casualWear,
    title: "Women wearing casual t-shirt",
    rows: 2,
    cols: 2,
  },
  {
    img: officeWear,
    title: "Women wearing white shirt",
    rows: 1,
    cols: 1,
  },
  {
    img: sandals,
    title: "Red sandals",
    rows: 1,
    cols: 1,
  },
];

const Home = () => {
  return (
    <Stack justifyContent="center" alignItems="center" spacing={16}>
      <Carousel />
      <ImageQuilt imageData={imageData} cols={4} rowHeight={350} />
    </Stack>
  );
};

export default Home;
