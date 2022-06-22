import { ImageList, ImageListItem } from "@mui/material";

import ImageCard from "../ImageCard";
import casualWear from "../../static/images/home/christian-bolt-VW5VjskNXZ8-unsplash.jpg";
import cocktailDress from "../../static/images/home/hanen-souhail-QwfgUwHoJDM-unsplash.jpg";
import officeWear from "../../static/images/home/laura-chouette-WQgvRkmqRrg-unsplash.jpg";
import sandals from "../../static/images/home/irene-kredenets-DDqxX0-7vKE-unsplash.jpg";

const ImageTiles = () => {
  return (
    <ImageList cols={4} rowHeight={590} gap={8}>
      <ImageListItem cols={1}>
        <ImageCard
          image={cocktailDress}
          title="DRESSES"
          subtitle="COCKTAIL & PARTY"
          buttonLabel="SHOP NOW"
          description="Find stunning women's cocktail & party dresses. Stand out in lace
          and metallic from all your favorite brands."
          imageAlt="Women wearing metallic dress"
        />
      </ImageListItem>
      <ImageListItem cols={2}>
        <ImageCard
          image={casualWear}
          title="CASUAL"
          subtitle="ON THE ROAD"
          buttonLabel="SHOP NOW"
          description="Time to relax and get comfy. Get ready for a summer of fun and road trips with our trendiest casualwear."
          imageAlt="Women wearing t-shirt"
        />
      </ImageListItem>
      <ImageListItem cols={1}>
        <ImageCard
          title="SHIRTS"
          subtitle="THE OFFICE LIFE"
          image={officeWear}
          imageAlt="Women wearing white shirt"
        />
        <ImageCard
          title="SHOES"
          subtitle="ECO SANDALS"
          image={sandals}
          imageAlt="Red sandals"
        />
      </ImageListItem>
    </ImageList>
  );
};

export default ImageTiles;
