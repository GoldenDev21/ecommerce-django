import { Button, Grid, Typography, alpha } from "@mui/material";

import ImageCard from "../ImageCard";
import casualWear from "../../static/images/home/christian-bolt-VW5VjskNXZ8-unsplash.jpg";
import cocktailDress from "../../static/images/home/hanen-souhail-QwfgUwHoJDM-unsplash.jpg";
import featured from "../../static/images/carousel/carousel-2.jpg";
import officeWear from "../../static/images/home/laura-chouette-WQgvRkmqRrg-unsplash.jpg";
import sandals from "../../static/images/home/irene-kredenets-DDqxX0-7vKE-unsplash.jpg";

const Home = () => {
  return (
    <>
      <Grid container sx={{ mb: 10 }}>
        <Grid
          item
          container
          xs={12}
          sx={{
            backgroundImage: `url(${featured})`,
            backgroundSize: "cover",
            backgroundPosition: "top right",
            height: "60vh",
            width: "100%",
          }}
        >
          <Grid
            item
            container
            direction="column"
            justifyContent="center"
            xs={12}
            md={5}
            sx={{ backgroundColor: alpha("#ecf1ef", 0.7), px: 5 }}
          >
            <Grid item>
              <Typography>SUMMER COLLECTION 2022</Typography>
            </Grid>
            <Grid item>
              <Typography variant="h4" fontWeight={600}>
                Embrace the sun with our new beachwear
              </Typography>
            </Grid>
            <Grid item>
              <Button
                variant="contained"
                size="large"
                sx={{ color: "#FFF" }}
                disableElevation
              >
                Learn more
              </Button>
            </Grid>
          </Grid>
          <Grid item xs={12} md={7} />
        </Grid>
      </Grid>
      <Grid container sx={{ height: 700, mb: 10 }}>
        <ImageCard
          image={cocktailDress}
          title="DRESSES"
          subtitle="COCKTAIL & PARTY"
          buttonLabel="SHOP NOW"
          description="Find stunning women's cocktail & party dresses. Stand out in lace
          and metallic from all your favorite brands."
          imagePosition="bottom right"
          xs={12}
          md={3}
        />
        <ImageCard
          image={casualWear}
          title="CASUAL"
          subtitle="ON THE ROAD"
          buttonLabel="SHOP NOW"
          description="Time to relax and get comfy. Get ready for a summer of fun and road trips with our trendiest casualwear."
          imagePosition="top right"
          xs={12}
          md={6}
        />
        <Grid item container xs={12} md={3} sx={{ pt: 0 }}>
          <ImageCard
            title="SHIRTS"
            subtitle="THE OFFICE LIFE"
            image={officeWear}
            xs={12}
          />
          <ImageCard
            title="SHOES"
            subtitle="ECO SANDALS"
            image={sandals}
            imagePosition="center"
            xs={12}
          />
        </Grid>
      </Grid>
    </>
  );
};

export default Home;
