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
import { Color } from "../../../types/variant";
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
  const [color, setColor] = useState<Option[]>([]);

  const { brands } = useContext(BrandsContext);

  const sizes = department === Department.Clothing ? clothingSizes : shoeSizes;

  const formatOptions = (rawOptions: { id: number; name: string }[]) => {
    return rawOptions.map((option) => ({
      label: option.name,
      value: option.id,
    }));
  };

  const getParamValue = (filter: Option[]) => {
    return filter.map((f) => f.value).join();
  };

  const brandOptions = formatOptions(brands);
  const colorOptions = Object.entries(Color).map((color) => ({
    label: color[0],
    value: color[1],
  }));

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
      options: sizes as readonly Option[],
    },
    {
      id: "color",
      label: "Color",
      value: color,
      stateSetter: setColor,
      options: colorOptions,
    },
  ];

  const fetchProducts = () => {
    setLoading(true);

    const params = {
      category: category.toString(),
      in_stock: "True",
      active: "True",
      ...(brand.length ? { brand__in: getParamValue(brand) } : {}),
      ...(color.length ? { variants__color__in: getParamValue(color) } : {}),
      ...(size.length ? { variants__size__in: getParamValue(size) } : {}),
      ...(price.length
        ? { price__gte: price[0].toString(), price__lte: price[1].toString() }
        : {}),
    };

    getProducts(new URLSearchParams(params))
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
  }, [category]);

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
                  isOptionEqualToValue={(option: Option, value: Option) =>
                    option.value === value.value
                  }
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
        {products.length && (
          <Grid item container xs={9} spacing={2}>
            {products.map((product) => (
              <Grid item xs={3} key={product.id}>
                <ProductCard product={product} />
              </Grid>
            ))}
          </Grid>
        )}
      </Grid>
      {!loading && products.length === 0 && (
        <Typography>No products found.</Typography>
      )}
    </>
  );
};

export default ProductPage;
