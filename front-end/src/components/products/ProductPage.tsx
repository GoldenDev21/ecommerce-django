import { Grid, Paper } from "@mui/material";
import { useEffect, useState } from "react";

import { Category } from "../../types/category";
import { Product } from "../../types/product";
import ProductCard from "../ProductCard";
import { getProducts } from "../../api/product";

type Props = {
  category: Category;
};

const ProductPage = (props: Props) => {
  const { category } = props;

  const [products, setProducts] = useState<Product[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    getProducts()
      .then((response) => {
        setProducts(response.data);
      })
      .catch((error) => {
        console.error(error);
      })
      .finally(() => {
        setIsLoading(false);
      });
  }, []);

  return (
    <Paper>
      <Grid container>
        {products.map((product) => (
          <Grid item md={3} sm={2} xs={1} key={product.id} sx={{ mx: 1 }}>
            <ProductCard product={product} />
          </Grid>
        ))}
      </Grid>
    </Paper>
  );
};

export default ProductPage;
