import {
  Autocomplete,
  Button,
  Grid,
  LinearProgress,
  Paper,
  Slider,
  Stack,
  TextField,
  Typography,
  alpha,
} from "@mui/material";
import { Category, Department } from "../../../types/category";
import { SyntheticEvent, useContext, useEffect, useState } from "react";
import { clothingSizes, shoeSizes } from "../../../options/variant";

import { BrandsContext } from "../../../contexts/BrandsContext";
import { Product } from "../../../types/product";
import ProductCard from "../../ProductCard";
import { getProducts } from "../../../api/product";

type Props = {
  category: Category;
  department: Department;
};

type Option = {
  label: string;
  value: string | number;
};

const ProductPage = (props: Props) => {
  const { category, department } = props;

  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);

  const [sortBy, setSortBy] = useState<Option[]>([]);
  const [brand, setBrand] = useState<Option[]>([]);
  const [price, setPrice] = useState<number[]>([0, 100]);
  const [size, setSize] = useState<Option[]>([]);

  const { brands } = useContext(BrandsContext);

  const sizes = department === Department.Clothing ? clothingSizes : shoeSizes;

  const formatOptions = (rawOptions: { id: number; name: string }[]) => {
    return rawOptions.map((option) => ({
      label: option.name,
      value: option.id,
    }));
  };

  const brandOptions = formatOptions(brands);

  const filters = [
    {
      id: "sort_by",
      label: "Sort By",
      value: sortBy,
      stateSetter: setSortBy,
      options: [],
    },
    {
      id: "brand",
      label: "Brand",
      value: brand,
      stateSetter: setBrand,
      options: brandOptions,
    },
    {
      id: "size",
      label: "Size",
      value: size,
      stateSetter: setSize,
      options: sizes as readonly { label: string; value: string }[],
    },
  ];

  const fetchProducts = () => {
    setLoading(true);

    console.log(brand, sortBy, price, size, category); // TODO: Connect filters once back-end is in place

    getProducts()
      .then((response) => {
        setProducts(response.data);
      })
      .catch((error) => {
        console.error(error);
      })
      .finally(() => {
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchProducts();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const styles = {
    container: {
      mb: 3,
      p: 4,
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
    textField: {
      my: 1,
    },
    searchButtonContainer: {
      mt: 3,
    },
    label: {
      mt: 1.5,
      mb: 0.5,
    },
    sliderLabel: {
      color: alpha("#000", 0.8),
    },
  };

  return (
    <>
      {loading && <LinearProgress />}
      {products.length && !loading && (
        <Grid container spacing={2}>
          <Grid item xs={3} sx={styles.container}>
            <Paper sx={styles.container}>
              <Grid container direction="column">
                <Typography variant="h5">Filters</Typography>
                {filters.map(({ id, stateSetter, label, value, options }) => (
                  <Autocomplete
                    key={id}
                    multiple
                    onChange={(
                      event: SyntheticEvent<Element, Event>,
                      newValue: Option[]
                    ) => stateSetter(newValue)}
                    options={options}
                    value={value}
                    renderInput={(params) => (
                      <TextField
                        {...params}
                        variant="standard"
                        label={label}
                        placeholder={label}
                        sx={styles.textField}
                      />
                    )}
                  />
                ))}
                <Typography color="textSecondary" sx={styles.label}>
                  Price
                </Typography>
                <Stack spacing={2} direction="row" alignItems="center">
                  <Typography
                    sx={styles.sliderLabel}
                  >{`$${price[0]}`}</Typography>
                  <Slider
                    value={price}
                    onChange={(event: Event, newValue: number | number[]) =>
                      setPrice(newValue as number[])
                    }
                    valueLabelDisplay="off"
                  />
                  <Typography
                    sx={styles.sliderLabel}
                  >{`$${price[1]}`}</Typography>
                </Stack>
                <Grid
                  item
                  container
                  justifyContent="flex-end"
                  sx={styles.searchButtonContainer}
                >
                  <Button onClick={fetchProducts} variant="contained">
                    Search
                  </Button>
                </Grid>
              </Grid>
            </Paper>
          </Grid>
          <Grid item container xs={9} spacing={2}>
            {products.map((product) => (
              <Grid item xs={3} key={product.id}>
                <ProductCard product={product} />
              </Grid>
            ))}
          </Grid>
        </Grid>
      )}
      {!loading && !products.length && (
        <Typography>No products found.</Typography>
      )}
    </>
  );
};

export default ProductPage;
