import ImageCard from "../ImageCard";
import { Carousel as ResponsiveCarousel } from "react-responsive-carousel";

const Carousel = () => {
  return (
    <ResponsiveCarousel
      showThumbs={false}
      infiniteLoop
      autoPlay
      showArrows={false}
      interval={6000}
      showStatus={false}
    >
      <ImageCard
        image="https://images.unsplash.com/photo-1507702553912-a15641e827c8"
        title="SUMMER COLLECTION 2022"
        subtitle="Handbags"
        buttonLabel="SHOP NOW"
        imageAlt="Woman holding pink leather crossbody bag on stairs"
      />
      <ImageCard
        image="https://images.unsplash.com/photo-1496747611176-843222e1e57c"
        title="SUMMER COLLECTION 2022"
        subtitle="Beachwear"
        buttonLabel="SHOP NOW"
        imageAlt="Woman in dress walking along seaside holding a woven bag"
        imageSx={{ transform: "scaleX(-1)" }}
      />
      <ImageCard
        image="https://images.unsplash.com/photo-1502868354157-ec2edd2a1651"
        title="SUMMER COLLECTION 2022"
        subtitle="Dresses & Rompers"
        buttonLabel="SHOP NOW"
        imageAlt="Woman in white and red floral dress standing in field"
      />
    </ResponsiveCarousel>
  );
};

export default Carousel;
