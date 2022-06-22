import { Grid, Paper } from "@mui/material";

import { Product } from "../../types/product";
import ProductCard from "../ProductCard";
import { useState } from "react";

type Props = {
  category: string;
};

const ProductPage = (props: Props) => {
  const { category } = props;

  const [products, setProducts] = useState<Product[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  return (
    <Paper>
      <Grid container>
        {products.map((product) => (
          <Grid item md={3} sm={2} xs={1} key={product.id}>
            <ProductCard product={product} />
          </Grid>
        ))}
      </Grid>
    </Paper>
  );
};

export default ProductPage;
