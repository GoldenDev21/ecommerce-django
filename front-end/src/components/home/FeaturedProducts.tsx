import { Box, Grid, Typography } from "@mui/material";

import Carousel from "react-material-ui-carousel";
import ProductCard from "../ProductCard";
import { mockProducts as products } from "../../mockData";

const FeaturedProducts = () => {
  const styles = {
    carouselItem: {
      maxWidth: 350,
      mx: 2,
    },
  };

  // TODO: Remove repetitive code, split products into chunks of 4

  return (
    <>
      <Grid item container justifyContent="center">
        <Typography variant="h5" fontWeight={600} sx={{ mb: 5 }}>
          Mix and match
        </Typography>
      </Grid>
      <Box>
        <Carousel
          autoPlay={false}
          navButtonsAlwaysVisible
          height={500}
          indicators={false}
        >
          <Box display="flex" justifyContent="center">
            <Box sx={styles.carouselItem}>
              <ProductCard product={products[0]} />
            </Box>
            <Box sx={styles.carouselItem}>
              <ProductCard product={products[1]} />
            </Box>
            <Box sx={styles.carouselItem}>
              <ProductCard product={products[2]} />
            </Box>
            <Box sx={styles.carouselItem}>
              <ProductCard product={products[3]} />
            </Box>
          </Box>
          <Box display="flex" justifyContent="center">
            <Box sx={styles.carouselItem}>
              <ProductCard product={products[4]} />
            </Box>
            <Box sx={styles.carouselItem}>
              <ProductCard product={products[5]} />
            </Box>
            <Box sx={styles.carouselItem}>
              <ProductCard product={products[6]} />
            </Box>
            <Box sx={styles.carouselItem}>
              <ProductCard product={products[7]} />
            </Box>
          </Box>
        </Carousel>
      </Box>
    </>
  );
};

export default FeaturedProducts;
