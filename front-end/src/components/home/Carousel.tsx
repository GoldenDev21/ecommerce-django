import { Box, Grid, Typography } from "@mui/material";

import MuiCarousel from "react-material-ui-carousel";
import ProductCard from "../ProductCard";

type CarouselProps = {
  items: any[];
  title?: string;
  visibleSlides?: 1 | 2 | 3 | 4 | 5 | 6;
};

const Carousel = (props: CarouselProps) => {
  const { title, items, visibleSlides = 4 } = props;

  const getChunks = (items: any[], chunkSize: number) => {
    let chunks = [];
    for (let i = 0; i < items.length; i += chunkSize) {
      const chunk = items.slice(i, i + chunkSize);
      chunks.push(chunk);
    }
    return chunks;
  };

  const styles = {
    carouselItem: {
      maxWidth: 350,
      mx: 2,
    },
  };

  return (
    <>
      {title && (
        <Grid item container justifyContent="center">
          <Typography variant="h5" fontWeight={600} sx={{ mb: 5 }}>
            {title}
          </Typography>
        </Grid>
      )}
      <Box>
        <MuiCarousel
          autoPlay={false}
          navButtonsAlwaysVisible
          height={500}
          indicators={false}
          animation="fade"
        >
          {getChunks(items, visibleSlides).map((subChunk, index) => (
            <Box display="flex" justifyContent="center" key={index}>
              {subChunk.map((chunk, idx) => (
                <Box sx={styles.carouselItem} key={idx}>
                  <ProductCard product={chunk} />
                </Box>
              ))}
            </Box>
          ))}
        </MuiCarousel>
      </Box>
    </>
  );
};

export default Carousel;
