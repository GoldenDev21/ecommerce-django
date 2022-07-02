import { Category, Department } from "../../../types/category";
import {
  Checkbox,
  FormControlLabel,
  FormGroup,
  Grid,
  Paper,
  TextField,
  Typography,
} from "@mui/material";
import { Fragment, useContext, useEffect, useState } from "react";
import { clothingSizes, shoeSizes } from "../../../options/variant";

import { BrandsContext } from "../../../contexts/BrandsContext";
import FilterLabel from "./filters/FilterLabel";
import { Product } from "../../../types/product";
import ProductCard from "../../ProductCard";
import { getProducts } from "../../../api/product";

type Props = {
  category: Category;
  department: Department;
};

const ProductPage = (props: Props) => {
  const { category, department } = props;

  const [products, setProducts] = useState<Product[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  const { brands } = useContext(BrandsContext);

  const sizes = department === Department.Clothing ? clothingSizes : shoeSizes;

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

  const styles = {
    container: {
      mb: 3,
    },
    filterContainer: {
      p: 2,
    },
    priceRangeText: {
      display: "flex",
      alignItems: "center",
      mx: 2,
    },
    productCardContainer: {
      mx: 2,
    },
  };

  return (
    <Paper sx={styles.container}>
      <Grid container>
        <Grid
          item
          container
          xs={3}
          sx={styles.filterContainer}
          direction="column"
          justifyContent="space-between"
        >
          <Grid item container direction="column">
            <Grid item>
              <FilterLabel>Brand</FilterLabel>
            </Grid>
            <FormGroup>
              {brands.map((brand) => (
                <Fragment key={brand.id}>
                  <FormControlLabel
                    control={<Checkbox defaultChecked />}
                    label={brand.name}
                  />
                </Fragment>
              ))}
            </FormGroup>
          </Grid>
          <Grid item container>
            <Grid item xs={12}>
              <FilterLabel>Price</FilterLabel>
            </Grid>
            <Grid item xs={4}>
              <TextField
                inputMode="numeric"
                margin="dense"
                size="small"
                placeholder="Min $"
              />
            </Grid>
            <Typography sx={styles.priceRangeText}>to</Typography>
            <Grid item xs={4}>
              <TextField
                inputMode="numeric"
                margin="dense"
                size="small"
                placeholder="Max $"
              />
            </Grid>
          </Grid>
          <Grid item container>
            <Grid item xs={12}>
              <FilterLabel>Size</FilterLabel>
            </Grid>
            <FormGroup>
              {sizes.map((size) => (
                <Fragment key={size.label}>
                  <FormControlLabel
                    control={<Checkbox defaultChecked />}
                    label={size.label}
                  />
                </Fragment>
              ))}
            </FormGroup>
          </Grid>
          <Grid item>Material</Grid>
          <Grid item>Color</Grid>
        </Grid>
        <Grid item container xs={9}>
          {products.map((product) => (
            <Grid item key={product.id} xs={3} sx={styles.productCardContainer}>
              <ProductCard product={product} />
            </Grid>
          ))}
        </Grid>
      </Grid>
    </Paper>
  );
};

export default ProductPage;
