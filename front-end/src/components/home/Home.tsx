import "react-multi-carousel/lib/styles.css";

import { Grid, Typography } from "@mui/material";

import FeaturedCollection from "./FeaturedCollection";
import FeaturedProducts from "./FeaturedProducts";
import ImageTiles from "./ImageTiles";

const Home = () => {
  return (
    <>
      <Grid container spacing={2} direction="column">
        <FeaturedCollection />
        <ImageTiles />
        <FeaturedProducts />
        <Grid item container xs={12}>
          <Grid item container xs={6}>
            <Typography>Subscribe to our newsletter</Typography>
            <Typography>
              Get notified of upcoming sales and events. Receive gifts and
              special offers!
            </Typography>
          </Grid>
          <Grid item container xs={6}>
            <Typography></Typography>
          </Grid>
        </Grid>
      </Grid>
    </>
  );
};

export default Home;
