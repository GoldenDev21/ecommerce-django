import {
  Box,
  Card,
  CardContent,
  CardMedia,
  Fab,
  Grid,
  IconButton,
  Typography,
  Zoom,
} from "@mui/material";
import {
  CartPlus as CartPlusIcon,
  HeartOutline as HeartIcon,
} from "mdi-material-ui";

import { Color } from "../types/variant";
import { Product } from "../types/product";
import { getSwatchColor } from "../utils/color";
import image from "../static/images/home/engin-akyurt-ehdI_89nzMo-unsplash.jpg";
import { useState } from "react";

type Props = {
  product: Product;
};

const ProductCard = (props: Props) => {
  const { product } = props;
  const { name, variants, price } = product;

  const uniqueColors = new Set(variants.map((variant) => variant.color));
  const colors = Array.from(uniqueColors);

  const [selectedColor, setSelectedColor] = useState(colors[0]);

  const styles = {
    card: {
      minWidth: 230,
      boxShadow: "0px 4px 9px -3px rgba(0,0,0,0.3)",
      transition: "all .2s ease-in-out",
      "&:hover": {
        boxShadow: "0px 8px 16px -8px rgba(0,0,0,0.55)",
        transform: "scale(1.05)",
      },
      padding: 2,
    },
    colorSwatch: {
      height: 12,
      width: 12,
      transition: "all .2s ease-in-out",
      "&:hover": {
        cursor: "pointer",
      },
    },
    unselected: {
      "&:hover": {
        boxShadow: "0px 3px 4px 0px rgba(0,0,0,0.3)",
        transform: "scale(1.5)",
      },
    },
    selected: {
      height: 16,
      width: 16,
      boxShadow: "0px 3px 4px 0px rgba(0,0,0,0.3)",
    },
    fab: {
      marginTop: -3,
      marginLeft: -8,
      position: "fixed",
    },
  };

  return (
    <Card sx={styles.card}>
      <Box position={"relative"}>
        <Grid container justifyContent="flex-end">
          <Grid item>
            <IconButton sx={{ position: "absolute", top: 0, right: 0 }}>
              <HeartIcon />
            </IconButton>
          </Grid>
        </Grid>
        <CardMedia component="img" height="300" image={image} alt={name} />
      </Box>
      <Grid container justifyContent="flex-end">
        <Grid item>
          <Zoom in={true}>
            <Fab size="medium" sx={styles.fab} color="primary">
              <CartPlusIcon />
            </Fab>
          </Zoom>
        </Grid>
      </Grid>
      <CardContent>
        <Grid container spacing={1}>
          {colors.map((color, index) => (
            <Grid item key={index}>
              <Box
                sx={[
                  { backgroundColor: getSwatchColor(color as Color) },
                  styles.colorSwatch,
                  color === selectedColor ? styles.selected : styles.unselected,
                ]}
                onClick={(e: any) => setSelectedColor(color)}
              />
            </Grid>
          ))}
        </Grid>
        <Typography color="text.secondary" sx={{ my: 1 }}>
          {name}
        </Typography>
        <Typography fontWeight={600}>{`$${price}`}</Typography>
      </CardContent>
    </Card>
  );
};

export default ProductCard;
