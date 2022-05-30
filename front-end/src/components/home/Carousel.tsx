import { Box, Grid } from "@mui/material";

import { Carousel as ResponsiveCarousel } from "react-responsive-carousel";
import { srcset } from "../../utils/image";

const Carousel = () => {
  return (
    <Grid container item sx={{ width: "80%" }}>
      <ResponsiveCarousel
        showThumbs={false}
        infiniteLoop
        autoPlay
        showArrows={false}
        interval={6000}
      >
        <Box>
          <img
            {...srcset(
              "https://images.unsplash.com/photo-1530377995122-4484c3886b33",
              1600
            )}
            alt="Woman sitting on beach"
          />
        </Box>
        <Box>
          <img
            {...srcset(
              "https://images.unsplash.com/photo-1496747611176-843222e1e57c",
              1600
            )}
            alt="Woman walking near seaside while holding woven bag"
          />
        </Box>
        <Box>
          <img
            {...srcset(
              "https://images.unsplash.com/photo-1469334031218-e382a71b716b",
              1600
            )}
            alt="Woman wearing a green top and glasses"
          />
        </Box>
      </ResponsiveCarousel>
    </Grid>
  );
};

export default Carousel;
